import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataGraph:

    def plot_results(self, dataframe, column_name, chart_type = "line"):
        fig, ax = plt.subplots()
        first_column = dataframe.iloc[:,0]
        x_axis = np.arange(len(first_column))
        x_axis_labels = first_column
        x_axis_name = dataframe.dtypes.index[0]
        if chart_type == "line":
            ax.plot(x_axis, dataframe[column_name])
        else:
            ax.bar(x_axis, dataframe[column_name])
        plt.xticks(x_axis, x_axis_labels, rotation = 45)
        ax.set(xlabel = x_axis_name, title = column_name)
        return plt.show()

    def generate_graphs(self, dataframe, chart_type = "line"):
        for column_name in dataframe.dtypes.index[1:]:
            graph = self.plot_results(dataframe, column_name, chart_type)
        return graph