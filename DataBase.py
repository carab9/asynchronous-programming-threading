from FileIO import FileIO
from SqliteDB import SqliteDB
from DBThread import DBThread
import numpy as np
import pandas as pd

class DataBase:
    def __init__(self):
        self.db = SqliteDB()
        self.db.connect("CIS41b")
        self.df = None

    def build(self, website):
        df = FileIO.scrape_page(website)
        print(df)
        col_names = list(df.columns[0:7])
        print(col_names)

        cols = list()
        cols.append((col_names[0], "INTEGER"))
        for i in range(1, len(col_names)):
            cols.append((col_names[i], "REAL"))
        print(cols)

        self.db.createTable(cols)

        for index, row in df.iterrows():
            row_list = list(row[0:7])
            print("row list:", row_list)
            self.db.insert(tuple(row_list))

        print(self.db.readTableToDf())

    def get_db_by_threading(self):
        column_names = self.db.get_column_names()
        print(column_names)
        years = np.arange(1990, 2020, 1)
        print(years)

        self.df = pd.DataFrame(columns=column_names)
        for year in years:
            print([year] + [0] * (len(column_names) - 1))
            self.df.loc[len(self.df.index)] = [year] + [0] * (len(column_names) - 1)
        print(self.df)

        threads = []
        for name in column_names[1:]:
            print(name)
            thread = DBThread(name, years, self)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        print(self.df)
        return self.df