from tkinter import ttk
import tkinter as tk
from tkinter import *
from Graph import Graph

class UI:
    blackboard = None

    def __init__(self, df):
        self.df = df
        self.root = tk.Tk()
        self.root.title("Asynchronous Programming")
        self.root.geometry('600x400')
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tab5 = ttk.Frame(self.tabControl)
        self.tab6 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text=df.columns[1])
        self.tabControl.add(self.tab2, text=df.columns[2])
        self.tabControl.add(self.tab3, text=df.columns[3])
        self.tabControl.add(self.tab4, text=df.columns[4])
        self.tabControl.add(self.tab5, text=df.columns[5])
        self.tabControl.add(self.tab6, text=df.columns[6])
        self.tabControl.pack(expand = 1, fill ="both")

    def run(self):
        g = Graph(self.df)
        g.display_lin_reg(self.tab1, 0, 1)
        g.display_lin_reg(self.tab2, 0, 2)
        g.display_lin_reg(self.tab3, 0, 3)
        g.display_lin_reg(self.tab4, 0, 4)
        g.display_lin_reg(self.tab5, 0, 5)
        g.display_lin_reg(self.tab6, 0, 6)
        self.root.mainloop()