# Andrea Egan Project 2020 - The Iris Flower Data Set 
# Objective - output a summary of each variable to a single txt file
# analysis this data by using histograms and scatter plots 

import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns 
import pandas as pd
import sys as sy 

# testing the output of file.txt
d = pd. read_csv ("iris.txt") # reads txt file saved within directory. 
sy.stdout = open("output.txt", "w") # opens and writes to file output.txt

pd.set_option('display.max_rows', 10) # displays 10 rows when printed 
pd.set_option('display.max_column', 5) # displays 5 columns when printed

# "\n" creates a new line 
print("SUMMARY OF DATA: ", "\n", d.groupby('species').size(), "\n") 
print("Count of Columns and Rows: ", d.shape,"\n")
print("Sample of Data: ", "\n", d.head(10),"\n")  
print("Description of Data: " "\n", d[d.columns[0:]].describe()) 

sy.stdout.close() # Closing output.txt file )
