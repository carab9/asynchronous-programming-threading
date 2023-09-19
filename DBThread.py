import threading
import time

globalLock = threading.Lock()

class DBThread (threading.Thread):
    def __init__(self, name, years, db):
        threading.Thread.__init__(self)
        self.name = name
        self.years = years
        self.db = db
    def run(self):
        print("Starting thread", self.name)
        self.threadfunc()
        print("Ending thread", self.name)
    def threadfunc(self):
        print(">>>>" + self.name)
        for year in self.years:
            globalLock.acquire()
            data = self.db.db.search(year, self.name)
            self.db.df.loc[self.db.df["Year"] == year, self.name] = data[0][0]
            print("Thread", self.name, "extracted", year, self.name, data[0][0])
            globalLock.release()
            time.sleep(0.1)
        print("<<<<" + self.name)