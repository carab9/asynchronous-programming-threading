# Asynchronous Programming - Threading

This project is a multithreading, web scraping, and data visualization program. The goal of this project is to extract yearly data of the levels of 6 different glasses (from 1979 to 2022) and display them in separate graphs. The data is first scraped from a webpage called “THE NOAA ANNUAL GREENHOUSE GAS INDEX (AGGI)”. The program parses and processes the data and stores it into the database. The data is then retrieved from the database using 6 separate threads, one for each type of gas. Each thread only retrieves a year’s data and uses thread lock to synchronize the shared access to the database. The data for each gas is plotted. Each graph can be accessed on a separate tab in the user interface.

## Architecture

My code has an architecture with 3 layers: a UI layer that contains components required to enable user interaction with the application; a Business Layer that processes the input data; and a Data Layer that controls access logic components to access the data.

![image](https://github.com/carab9/asynchronous-programming-threading/blob/main/architecture.png?raw=true)


The UI layer consists of the UI and Graph classes. The Graph Class creates and displays the graphs. The UI class creates the interface that the user interacts with: the main window and the tabs.

The Business layer consists of the FileIO, Database, RunLR, and DBThread classes. The FileIO class scrapes the necessary data from the webpage and processes it. The Database class creates a database and stores the data into the database. It then returns the database as a dataframe using threading. The RunLR class performs a linear regression between the data for that graph’s gas and the year. The DBThread class runs the thread and accesses the requested data from the database.

The Data layer consists of the SqliteDB class, which provides the SQL APIs to create, store and access the SQLite database.

## Requirements

Python
Python Libraries: numpy, pandas, sqlite3, matplotlib.figure, matplotlib.backends.backend_tkagg, tkinter, urllib.request, bs4, threading, time
Run the program: python main.py

## Technical Skills

urllib and BeautifulSoup for web scraping, pandas dataframe for data processing, SQLite for database, threading and time for threading, thread lock for multithreading synchronization, matplotlib Figure and FigureCanvasTkAgg for plotting graphs. Tkinter for GUIs.

## Results

This chart shows the linear regression between CO2 levels and year, displayed alongside a scatter plot.

![image](https://github.com/carab9/asynchronous-programming-threading/blob/main/co2.png?raw=true)

This chart shows the linear regression between CH4 levels and year, displayed alongside a scatter plot.

![image](https://github.com/carab9/asynchronous-programming-threading/blob/main/ch4.png?raw=true)

This chart shows the linear regression between N2O levels and year, displayed alongside a scatter plot.

![image](https://github.com/carab9/asynchronous-programming-threading/blob/main/n2o.png?raw=true)

This chart shows the linear regression between CFCs levels and year, displayed alongside a scatter plot.

![image](https://github.com/carab9/asynchronous-programming-threading/blob/main/cfcs.png?raw=true)

This chart shows the linear regression between HCFCs levels and year, displayed alongside a scatter plot.

![image](https://github.com/carab9/asynchronous-programming-threading/blob/main/hcfcs.png?raw=true)

This chart shows the linear regression between HCFCS* levels and year, displayed alongside a scatter plot.

![image](https://github.com/carab9/asynchronous-programming-threading/blob/main/hfcs.png?raw=true)

