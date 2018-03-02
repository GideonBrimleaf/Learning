import sys
import pandas as pd
from connection_script import SqlConnection

def main(query_string):
    conn = SqlConnection().mdbdw_connection()
    results_table = pd.read_sql(query_string,conn)
    print(results_table.head())

if __name__ == '__main__':
    main(sys.argv[1])