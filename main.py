import requests
import shutil
import sys
import sys
import re
from DataBase import DataBase
from UI import UI

def main():
    db = DataBase()
    db.build("https://gml.noaa.gov/aggi/aggi.html")
    df = db.get_db_by_threading()

    ui = UI(df)
    ui.run()

if __name__ == '__main__':
    main()