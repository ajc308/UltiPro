import config
import requests
from lxml import etree
from lxml.etree import SubElement, QName, tostring
from shared import XMLNamespaces, create_request_envelope

from rinse.util import printxml

REQUEST_URL = 'https://service4.ultipro.com/services/EmployeePerson'

class EmployeePersonService:

    def __init__(self, token):
        self.token = token

    def find_people(self, params={}):
        action_url = 'http://www.ultipro.com/services/employeeperson/IEmployeePerson/FindPeople'

        root = create_request_envelope(token=self.token, action_url=action_url)

        body = SubElement(root, QName(XMLNamespaces.s, 'Body'))

        find_people = SubElement(body, 'FindPeople', xmlns=XMLNamespaces.e)
        query = SubElement(find_people, 'query', nsmap={'b':XMLNamespaces.b, 'i':XMLNamespaces.i})

        for key in params:
            query_param = SubElement(query, QName(XMLNamespaces.b, key))
            query_param.text = params[key]

        response = requests.request("POST", REQUEST_URL, data=tostring(root), headers=config.HTTP_HEADERS)

        root = etree.fromstring(response.text)
        results = root.xpath('//b:Results', namespaces=XMLNamespaces.ns)[0].getchildren()

        #TODO: Pagination

        return results



