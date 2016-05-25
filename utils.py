import requests
from database import *
from lxml import etree
from lxml.etree import Element, SubElement, QName, tostring


class XMLNamespaces:
    a = 'http://www.w3.org/2005/08/addressing'
    b = 'http://www.ultipro.com/contracts'
    h = 'http://www.ultipro.com/services/loginservice'
    i = 'http://www.w3.org/2001/XMLSchema-instance'
    k = 'http://www.ultimatesoftware.com/foundation/authentication/clientaccesskey'
    s = 'http://www.w3.org/2003/05/soap-envelope'
    t = 'http://www.ultimatesoftware.com/foundation/authentication/ultiprotoken'

    ns = {
        'a': a,
        'b': b,
        'h': h,
        'i': i,
        'k': k,
        's': s,
        't': t
    }


def find(service_instance, params={}, page_number='1', page_size='1000'):
        envelope = create_request_envelope(
            token=service_instance.token,
            action_url=service_instance.action_url,
            namespace=service_instance.namespace,
            find_element=service_instance.find_element,
            params=params,
            page_number=page_number,
            page_size=page_size
        )

        response = make_service_request(
            request_url=service_instance.request_url,
            envelope=envelope
        )

        results = parse_response_for_results(
            response=response,
            result_element=service_instance.result_element
        )

        return results


def create_request_envelope(token, action_url, namespace, find_element, params, page_number, page_size):

    root = Element(QName(XMLNamespaces.s, 'Envelope'), nsmap={'s':XMLNamespaces.s, 'a':XMLNamespaces.a})

    header = SubElement(root, QName(XMLNamespaces.s, 'Header'))

    action = SubElement(header, QName(XMLNamespaces.a, 'Action'))
    action.attrib[QName(XMLNamespaces.s, 'mustUnderstand')] = "1"
    action.text = action_url

    ulti_pro_token = SubElement(header, 'UltiProToken', xmlns=XMLNamespaces.t)
    ulti_pro_token.text = token

    client_access_key = SubElement(header, 'ClientAccessKey', xmlns=XMLNamespaces.k)
    client_access_key.text = config.CLIENT_ACCESS_KEY

    body = SubElement(root, QName(XMLNamespaces.s, 'Body'))

    find = SubElement(body, find_element, xmlns=namespace)
    query = SubElement(find, 'query', nsmap={'b':XMLNamespaces.b, 'i':XMLNamespaces.i})

    page_number_param = SubElement(query, QName(XMLNamespaces.b, 'PageNumber'))
    page_number_param.text = page_number

    page_size_param = SubElement(query, QName(XMLNamespaces.b, 'PageSize'))
    page_size_param.text = page_size

    for key in params:
        query_param = SubElement(query, QName(XMLNamespaces.b, key))
        query_param.text = params[key]

    return root


def make_service_request(request_url, envelope):
    return requests.request("POST", request_url, data=tostring(envelope), headers=config.HTTP_HEADERS)


def parse_response_for_results(response, result_element):
    response_root = etree.fromstring(response.text)
    results = response_root.xpath('//b:{}'.format(result_element), namespaces=XMLNamespaces.ns)

    page_total = response_root.xpath('//b:PageTotal', namespaces=XMLNamespaces.ns)[0].text
    total_items = response_root.xpath('//b:TotalItems', namespaces=XMLNamespaces.ns)[0].text
    print('Pages:', page_total, 'Results:', total_items)

    return results


def xml_to_flat_json(root, data):
    if len(root.getchildren()) > 0:
        for element in root.getchildren():
            data = xml_to_flat_json(element, data)
    else:
        tag = root.tag.replace('{%s}' % root.nsmap[root.prefix], '')
        data[tag] = root.text
    return data


def iterate_xml_results(results):
    return [xml_to_flat_json(result, {}) for result in results]


def results_to_database(results, table_name, table_keys, cram=False):
    data = iterate_xml_results(results)

    conn = get_connection()
    curr = get_connection_cursor(conn)

    queries = generate_insert_queries(data, table_name, table_keys, cram)

    for query in queries:
        try:
            execute_query(conn, curr, query)
        except Exception as e:
            print(e)
            print(query)

    curr.close()
    conn.close()