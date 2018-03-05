import sys
import pandas as pd
from db_query import DatabaseQuery
from graph_data import DataGraph
import matplotlib.pyplot as plt
import numpy as np

def main(sql_file, chart_type = "line"):
    sql_query = DatabaseQuery().read_sql_query(sql_file)
    sql_results = DatabaseQuery().execute_sql_query(sql_query)
    graphs = DataGraph().generate_graphs(sql_results, chart_type)
    return graphs

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])