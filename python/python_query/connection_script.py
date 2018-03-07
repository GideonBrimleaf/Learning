#You need top add an ODBC driver (called 'Python' here) to the ODBC Data Sources (64 Bit) application.  Used SQL Server driver for setup here
#In Anaconda prompt - conda install pyodbc, this is the ODBC connection module which will use the driver to connect to the system

import pyodbc
import pandas as pd
import os

class SqlConnection:

	def mdbdw_connection(self):	
		
		driver = 'SQL Server Native Client 11.0' 
		server_name = os.environ['MDBDW_DBServerIP']
		database_name = 'MDBDW'
		username = 'DWReadOnly'
		password = os.environ['MDBDW_DWReadOnlyPWD']

		credentials = "DRIVER={0}; SERVER={1};DATABASE={2};UID={3};PWD={4}".format(driver, server_name, database_name, username, password)
		conn = pyodbc.connect(credentials)

		return conn