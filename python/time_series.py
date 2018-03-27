import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('passengers.csv', parse_dates=['Month'], index_col=['Month'],date_parser=dateparse)
data.index

ts = data['PassengerCount']
ts.head(10)
