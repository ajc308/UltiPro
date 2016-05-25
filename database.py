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


def generate_insert_queries(json_data, table_name, table_keys, cram=False):
    queries = []

    for row in json_data:
        columns = ', '.join(list(row.keys()))
        values = ', '.join(["'" + value.replace("'", "''") + "'" if value else 'NULL' for value in list(row.values())])

        query = 'INSERT INTO ' + table_name + ' (' + columns + ') SELECT ' + values + ' '
        if cram:
            query_key_values = [key + "='" + row[key] + "'" for key in table_keys]
            query_where = ' AND '.join(query_key_values)
            query += 'WHERE NOT EXISTS (SELECT 1 FROM ' + table_name + ' WHERE ' + query_where + ")"
        queries.append(query)
    return queries


def execute_query(conn, curr, query):
    curr.execute(query)
    conn.commit()


