import pandas as pd
from connection_script import SqlConnection

def main():
    conn = SqlConnection().mdbdw_connection()
    query_string = "SELECT TOP 10 * FROM DWInternal.FactTransaction"
    results_table = pd.read_sql(query_string,conn)
    print(results_table.head())

if __name__ == '__main__':
    main()