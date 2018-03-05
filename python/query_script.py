import sys
from db_query import DatabaseQuery
from graph_data import DataGraph

def main(sql_file, chart_type = "line"):
    sql_results = DatabaseQuery().execute_sql_query(sql_file)
    graphs = DataGraph().generate_graphs(sql_results, chart_type)
    return graphs

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])