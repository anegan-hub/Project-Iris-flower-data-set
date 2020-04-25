# Andrea Egan Project 2020 - The Iris Flower Data Set 
# Objective - output a summary of each variable to a single txt file
# analysis this data by using histograms and scatter plots 

import pandas as pd
import sys as sy
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

# testing the output of file.txt
col = ['sepal_length', 'sepal_width','petal_length', 'petal_width','species'] #Creating Column names for dataset 
d = pd. read_csv ("iris.txt", names=col) # reads txt file within the saved within directory including the column names.
sy.stdout = open("output.txt", "w") # opens and writes to file output.txt

pd.set_option('display.max_rows', 10) # displays 10 rows when printed 
pd.set_option('display.max_column', 5) # displays 5 columns when printed

# "\n" creates a new line 
print("SUMMARY OF DATA: ", "\n", d.groupby('species').size(), "\n") 
print("Count of Columns and Rows: ", d.shape,"\n")
print("Sample of Data: ", "\n", d.head(10),"\n")  
print("Description of Data: " "\n", d[d.columns[0:]].describe())

#sy.stdout.close() # Closing output.txt file )

# Plots
# Writing a program to create a histogram 
# of each variable within the iris dataset. 
# each histogram will be saved automatically when running the program

d.plot.hist( subplots=True, bins=30, layout=(2,2)) #creates multiple histograms
plt.savefig("Histogram of each variable.png") # saves histogram
plt.show() 




