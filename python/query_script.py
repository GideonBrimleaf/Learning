import sys
import pandas as pd
from connection_script import SqlConnection

#file = open("sql_string.sql", "r") or r+ - not sure yet
#sql string = file.read()

def main(filename):
    conn = SqlConnection().mdbdw_connection()
    file = open(filename, "r+")
    query_string = file.read()
    results_table = pd.read_sql(query_string,conn)
    print(results_table.head())

if __name__ == '__main__':
    main(sys.argv[1])