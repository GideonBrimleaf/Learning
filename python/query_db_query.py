import pandas as pd
from connection_script import SqlConnection

class DatabaseQuery:

    def read_sql_query(self, filename):
        file = open(filename, "r")
        query_string = file.read()
        return query_string

    def execute_sql_query(self, query_string):
        conn = SqlConnection().mdbdw_connection()
        results_table = pd.read_sql(query_string,conn)
        return results_table