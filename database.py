import config
import pymssql

server = config.DB_SERVER
user = config.DB_USER
password = config.DB_PASSWORD
database = config.DB_NAME


def get_connection():
    return pymssql.connect(server, user, password, database)


def get_connection_cursor(conn):
    return conn.cursor()


def close(obj):
    obj.close()


def json_data_to_insert_queries(json_data, table_name):
    queries = []
    #TODO: Cram style, checking for primary keys that already exist
    for row in json_data:
        columns = ', '.join(list(row.keys()))
        values = ', '.join(["'" + value + "'" if value else 'NULL' for value in list(row.values())])
        query = 'INSERT INTO ' + table_name + ' (' + columns + ') VALUES (' + values + ')'
        queries.append(query)
    return queries


def execute_query(conn, curr, query):
    curr.execute(query)
    conn.commit()


