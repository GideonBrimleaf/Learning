import pandas as pd
from python_query.connection_script import SqlConnection

class DatabaseQuery:

    def read_sql_query(self, filename):
        file = open(filename, "r")
        query_string = file.read()
        return query_string

    def execute_sql_query(self, filename):
        conn = SqlConnection().mdbdw_connection()
        query_string = self.read_sql_query(filename)
        results_table = pd.read_sql(query_string,conn)
        return results_table