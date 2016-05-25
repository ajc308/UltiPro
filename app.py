import utils
import services
from login import LoginService
from rinse.util import printxml

token = LoginService().token
page_number = 1
page_size = 1000
max_page_number = 3
params = {}
web_service = services.EmployeeContactsService

service = web_service(token)

for page in range(page_number, max_page_number):
    print(page)
    results = utils.find(service, params, str(page), str(page_size))
    utils.results_to_database(results, service.table_name, service.table_keys, cram=False)
