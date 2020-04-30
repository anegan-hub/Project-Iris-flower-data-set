# Andrea Egan Project 2020 - The Iris Flower Data Set 
# Objective - output a summary of each variable to a single txt file
# analysis this data by using histograms and scatter plots 

import pandas as pd
import sys as sy
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns


col = ['sepal_length', 'sepal_width','petal_length', 'petal_width','species'] # creating column names for dataset 
d = pd. read_csv ("iris.txt", names=col) # reads txt file within the saved directory, adding column names
sy.stdout = open("output.txt", "w") # opens file and writes the command print to file output.txt 

pd.set_option('display.max_rows', 10) # displays 10 rows when printed 
pd.set_option('display.max_column', 5) # displays 5 columns when printed

# Using pandas built in functions. Adding "\n" (creates a new line) to tidy output display 
print("SUMMARY OF DATA: ", "\n", d.groupby('species').size(), "\n") # returns species by group including values
print("Count of Columns and Rows: ", d.shape,"\n") # returns the number of columns and rows
print("Sample of Data: ", "\n", d.head(10),"\n")  # returns the the top rows of data, here i have specified 10
print("Description of Data: " "\n", d[d.columns[0:]].describe()) # returns a summary of the dataset 

sy.stdout.close() # Closing output.txt file )

# Plots
# Writing a program to create a histogram 
# of each variable within the iris dataset 
# Each histogram will be saved automatically when running the program

d.plot.hist( subplots=True, bins = 20, layout=(2,2)) # creating a histogram subplot adjusting bins & layout
plt.suptitle("Iris Flower Variables", fontsize = 12) # allows you to add a subtitle to histogram
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # prevents layout overlapping on png file. To realign subtitle use 'rect'  
plt.savefig("Histogram.png") # automatically saves png to directory. 
plt.show() 

# Scattered plots of each pair of variables using seaborn

#sns = seaborn library, hue is a built in function of seaborn to colour code species.
sns.scatterplot(data = d, x = "sepal_length", y = "sepal_width",  hue="species")
plt.title ("Sepal length vs Sepal width")
sns.scatterplot(data = d, x = "petal_length", y = "petal_width",  hue="species")
plt.title ("Petal length vs Petal width")
plt.show()