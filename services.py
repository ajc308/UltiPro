class EmployeePersonService:

    def __init__(self, token):
        self.token = token
        self.request_url = 'https://service4.ultipro.com/services/EmployeePerson'
        self.action_url = 'http://www.ultipro.com/services/employeeperson/IEmployeePerson/FindPeople'
        self.namespace = 'http://www.ultipro.com/services/employeeperson'
        self.find_element = 'FindPeople'
        self.result_element = 'Person'
        self.table_name = 'EmployeePerson'
        self.table_keys = ['EmployeeNumber', 'CompanyCode']


class EmployeeAddressService:

    def __init__(self, token):
        self.token = token
        self.request_url = 'https://service4.ultipro.com/services/EmployeeAddress'
        self.action_url = 'http://www.ultipro.com/services/employeeaddress/IEmployeeAddress/FindAddresses'
        self.namespace = 'http://www.ultipro.com/services/employeeaddress'
        self.find_element = 'FindAddresses'
        self.result_element = 'Address'
        self.table_name = 'EmployeeAddress'
        self.table_keys = ['EmployeeNumber', 'CompanyCode']


class EmployeeContactsService:

    def __init__(self, token):
        self.token = token
        self.request_url = 'https://service4.ultipro.com/services/EmployeeContacts'
        self.action_url = 'http://www.ultipro.com/services/employeecontacts/IEmployeeContacts/FindContacts'
        self.namespace = 'http://www.ultipro.com/services/employeecontacts'
        self.find_element = 'FindContacts'
        self.result_element = 'Contact'
        self.table_name = 'EmployeeContacts'
        self.table_keys = ['EmployeeNumber', 'CompanyCode', 'ContactId']


class EmployeeJobService:

    def __init__(self, token):
        self.token = token
        self.request_url = 'https://service4.ultipro.com/services/EmployeeJob'
        self.action_url = 'http://www.ultipro.com/services/employeejob/IEmployeeJob/FindJobs'
        self.namespace = 'http://www.ultipro.com/services/employeejob'
        self.find_element = 'FindJobs'
        self.result_element = 'Job'
        self.table_name = 'EmployeeJob'
        self.table_keys = ['EmployeeNumber', 'CompanyCode']


class EmployeeCompensationService:

    def __init__(self, token):
        self.token = token
        self.request_url = 'https://service4.ultipro.com/services/EmployeeCompensation'
        self.action_url = 'http://www.ultipro.com/services/employeecompensation/IEmployeeCompensation/FindCompensations'
        self.namespace = 'http://www.ultipro.com/services/employeecompensation'
        self.find_element = 'FindCompensations'
        self.result_element = 'Compensations'
        self.table_name = 'EmployeeCompensation'
        self.table_keys = ['EmployeeNumber', 'CompanyCode']


class EmployeePhoneInformationService:

    def __init__(self, token):
        self.token = token
        self.request_url = 'https://service4.ultipro.com/services/EmployeePhoneInformation'
        self.action_url = 'http://www.ultipro.com/services/employeephoneinformation/IEmployeePhoneInformation/FindPhoneInformations'
        self.namespace = 'http://www.ultipro.com/services/employeephoneinformation'
        self.find_element = 'FindPhoneInformations '
        self.result_element = 'PhoneInformations'
        self.table_name = 'EmployeePhoneInformation'
        self.table_keys = ['EmployeeNumber', 'CompanyCode']


class EmployeeEmploymentInformationService:

    def __init__(self, token):
        self.token = token
        self.request_url = 'https://service4.ultipro.com/services/EmployeeEmploymentInformation'
        self.action_url = 'http://www.ultipro.com/services/employeeemploymentinformation/IEmployeeEmploymentInformation/FindEmploymentInformations'
        self.namespace = 'http://www.ultipro.com/services/employeeemploymentinformation'
        self.find_element = 'FindEmploymentInformations  '
        self.result_element = 'EmploymentInformations '
        self.table_name = 'EmployeeEmploymentInformation'
        self.table_keys = ['EmployeeNumber', 'CompanyCode']