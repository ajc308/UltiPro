import shared
from database import *
from services.login import LoginService
from services.employee_person import EmployeePersonService

l = LoginService()
e = EmployeePersonService(l.token)
params = {
    'CompanyCode': '=NETS',
    'Status': '=A',
    # 'PageNumber': '1',
    # 'PageSize': '1000'
}
results = e.find_people(params)
json_data = shared.iterate_xml_results(results)

conn = get_connection()
curr = get_connection_cursor(conn)

insert_queries = json_data_to_insert_queries(json_data, 'EmployeePerson')

for query in insert_queries:
    try:
        execute_query(conn, curr, query)
    except Exception as e:
        print(e)
        print(query)