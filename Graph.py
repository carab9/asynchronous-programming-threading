from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from RunLR import RunLR

class Graph:
    def __init__(self, df):
        self.data = df

    def display_lin_reg(self, tab, col1, col2):
        print('Linear Regression result:')

        lr = RunLR()
        lr.run(self.data, col1, col2)
        intercept = lr.get_intercept()
        slope = lr.get_slope()
        print('intercept:', intercept)
        print('slope:', slope)

        x = self.data[self.data.columns[col1]].to_numpy()
        y = self.data[self.data.columns[col2]].to_numpy()

        fig = Figure(figsize=(8, 6), dpi=100)
        plot = fig.add_subplot()
        canvas = FigureCanvasTkAgg(fig, master=tab)

        plot.scatter(x, y, color="blue")
        y_pred = intercept + slope * x
        plot.plot(x, y_pred, color="green")

        plot.set_xlabel(self.data.columns[col1])
        plot.set_ylabel(self.data.columns[col2])
        plot.set_title(self.data.columns[col2] + "/" + self.data.columns[col1])

        # Show plot
        canvas.draw()
        canvas.get_tk_widget().pack()