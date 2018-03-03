import sys
import pandas as pd
from connection_script import SqlConnection

def read_sql_query(filename):
    file = open(filename, "r")
    query_string = file.read()
    return query_string

def execute_sql_query(query_string):
    conn = SqlConnection().mdbdw_connection()
    results_table = pd.read_sql(query_string,conn)
    return(results_table.head())

def main():
    sql_query = read_sql_query(sys.argv[1])
    sql_results = execute_sql_query(sql_query)
    return sql_results

if __name__ == '__main__':
    print(main())