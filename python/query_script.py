import sys
import pandas as pd
from db_query import DatabaseQuery
from graph_data import DataGraph
import matplotlib.pyplot as plt
import numpy as np

# def plot_results(dataframe, column_name, chart_type = "line"):
#     fig, ax = plt.subplots()
#     first_column = dataframe.iloc[:,0]
#     x_axis = np.arange(len(first_column))
#     x_axis_labels = first_column
#     x_axis_name = dataframe.dtypes.index[0]
#     if chart_type == "line":
#         ax.plot(x_axis, dataframe[column_name])
#     else:
#         ax.bar(x_axis, dataframe[column_name])
#     plt.xticks(x_axis, x_axis_labels, rotation = 45)
#     ax.set(xlabel = x_axis_name, title = column_name)
#     return plt.show()

# def generate_graphs(dataframe, chart_type = "line"):
#     for column_name in dataframe.dtypes.index[1:]:
#         graph = plot_results(dataframe, column_name, chart_type)
#     return graph

def main(sql_file, chart_type = "line"):
    sql_query = DatabaseQuery().read_sql_query(sql_file)
    sql_results = DatabaseQuery().execute_sql_query(sql_query)
    # graphs = generate_graphs(sql_results, chart_type) 
    graphs = DataGraph().generate_graphs(sql_results, chart_type)
    return graphs

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])