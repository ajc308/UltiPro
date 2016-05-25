import config
import requests
from lxml import html
from lxml.etree import Element, SubElement, QName, tostring
from utils import XMLNamespaces

REQUEST_URL = 'https://service4.ultipro.com/services/LoginService'


class LoginService:
    def authenticate(self):
        action_url = 'http://www.ultipro.com/services/loginservice/ILoginService/Authenticate'

        root = Element(QName(XMLNamespaces.s, 'Envelope'), nsmap={'s':XMLNamespaces.s, 'a':XMLNamespaces.a})

        header = SubElement(root, QName(XMLNamespaces.s, 'Header'))

        action = SubElement(header, QName(XMLNamespaces.a, 'Action'))
        action.attrib[QName(XMLNamespaces.s, 'mustUnderstand')] = "1"
        action.text = action_url

        client_access_key = SubElement(header, QName(XMLNamespaces.h, 'ClientAccessKey'), nsmap={'h':XMLNamespaces.h})
        client_access_key.text = config.CLIENT_ACCESS_KEY

        password = SubElement(header, QName(XMLNamespaces.h, 'Password'), nsmap={'h':XMLNamespaces.h})
        password.text = config.PASSWORD

        user_access_key = SubElement(header, QName(XMLNamespaces.h, 'UserAccessKey'), nsmap={'h':XMLNamespaces.h})
        user_access_key.text = config.USER_ACCESS_KEY

        user_name = SubElement(header, QName(XMLNamespaces.h, 'UserName'), nsmap={'h':XMLNamespaces.h})
        user_name.text = config.USER_NAME

        body = SubElement(root, QName(XMLNamespaces.s, 'Body'))

        SubElement(body, 'TokenRequest', xmlns=XMLNamespaces.b)

        response = requests.request("POST", REQUEST_URL, data=tostring(root), headers=config.HTTP_HEADERS)
        response_tree = html.fromstring(response.content)
        token = response_tree.xpath('//token/text()')[0]

        return token


    def __init__(self):
        self.token = self.authenticate()

