import sys
import pandas as pd
from connection_script import SqlConnection

def main(filename):
    conn = SqlConnection().mdbdw_connection()
    file = open(filename, "r")
    query_string = file.read()
    results_table = pd.read_sql(query_string,conn)
    print(results_table.head())

if __name__ == '__main__':
    main(sys.argv[1])