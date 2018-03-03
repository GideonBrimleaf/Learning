import sys
import pandas as pd
from connection_script import SqlConnection

def main(filename):
    conn = SqlConnection().mdbdw_connection()
    file = open(filename, "r")
    query_string = file.read()
    results_table = pd.read_sql(query_string,conn)
    return(results_table.head())

if __name__ == '__main__':
    print(main(sys.argv[1]))