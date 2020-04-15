# Andrea Egan Project 2020 - The Iris Flower Data Set 
# Objective - output a file as txt ( The Iris data) 
# analysis this data by using histograms and scatter plots 

import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns 
import pandas as pd 

# testing the output file.txt
d = pd. read_csv ("iris.txt") # reads txt file saved within directory. 
pd.set_option('display.max_rows', 150) # displays all rows when printed 
pd.set_option('display.max_column', 5) # displays all columns when printed 

print(d)
#print (d.shape)
#print(d.columns)

# *** PLEASE BE AWARE THIS PROGRAM IS STILL BEING BUILT, ADDITIONAL CODE TO BE ADDED***