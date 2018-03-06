import pandas as pd

class SaveResults:

    def save_to_excel(self, dataframe, filename):
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        dataframe.to_excel(writer)
        return writer.save()