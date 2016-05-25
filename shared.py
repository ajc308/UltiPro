import config
from lxml.etree import Element, SubElement, QName


class XMLNamespaces:
    a = 'http://www.w3.org/2005/08/addressing'
    b = 'http://www.ultipro.com/contracts'
    e = 'http://www.ultipro.com/services/employeeperson'
    h = 'http://www.ultipro.com/services/loginservice'
    i = 'http://www.w3.org/2001/XMLSchema-instance'
    k = 'http://www.ultimatesoftware.com/foundation/authentication/clientaccesskey'
    s = 'http://www.w3.org/2003/05/soap-envelope'
    t = 'http://www.ultimatesoftware.com/foundation/authentication/ultiprotoken'

    ns = {
        'a': a,
        'b': b,
        'e': e,
        'h': h,
        'i': i,
        'k': k,
        's': s,
        't': t
    }


def create_request_envelope(token, action_url):

    root = Element(QName(XMLNamespaces.s, 'Envelope'), nsmap={'s':XMLNamespaces.s, 'a':XMLNamespaces.a})

    header = SubElement(root, QName(XMLNamespaces.s, 'Header'))

    action = SubElement(header, QName(XMLNamespaces.a, 'Action'))
    action.attrib[QName(XMLNamespaces.s, 'mustUnderstand')] = "1"
    action.text = action_url

    ulti_pro_token = SubElement(header, 'UltiProToken', xmlns=XMLNamespaces.t)
    ulti_pro_token.text = token

    client_access_key = SubElement(header, 'ClientAccessKey', xmlns=XMLNamespaces.k)
    client_access_key.text = config.CLIENT_ACCESS_KEY

    return root


def xml_to_flat_json(xml, data):
    for element in xml.getchildren():
        tag = element.tag.replace('{%s}' % element.nsmap[element.prefix], '')

        children = element.getchildren()
        if len(children) > 0:
            for child in children:
                data = xml_to_flat_json(child, data)
        else:
            data[tag] = element.text
    return data


def iterate_xml_results(results):
    return [xml_to_flat_json(result, {}) for result in results]