from db_query import DatabaseQuery
from graph_data import DataGraph
from export_results import SaveResults

df = DatabaseQuery().execute_sql_query("bennet_credit_card_transactions.sql")

graph = DataGraph().generate_graphs(df)

excel_file = SaveResults().save_to_excel(df, "testblah.xlsx")
