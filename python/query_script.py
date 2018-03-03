import sys
import pandas as pd
from connection_script import SqlConnection
import matplotlib.pyplot as plt
import numpy as np

def read_sql_query(filename):
    file = open(filename, "r")
    query_string = file.read()
    return query_string

def execute_sql_query(query_string):
    conn = SqlConnection().mdbdw_connection()
    results_table = pd.read_sql(query_string,conn)
    return(results_table.head())

sql_query = read_sql_query("sql_string.sql")
sql_results = execute_sql_query(sql_query)

def plot_results(dataframe):
    fig, ax = plt.subplots()
    first_column = dataframe.iloc[:,0]
    x_axis = np.arange(len(first_column))
    ax.plot(x_axis, dataframe.userCount)
    plt.show()

def main():
    sql_query = read_sql_query(sys.argv[1])
    sql_results = execute_sql_query(sql_query)
    graph = plot_results(sql_results)
    return graph

if __name__ == '__main__':
    main()