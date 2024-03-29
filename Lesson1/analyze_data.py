#!/usr/bin/env python

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number

# Enable inline plotting
#%matplotlib inline

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

print "\n"+"Analyze and Present Data Now:"
Location = "./births1880.csv"
df = pd.read_csv(Location, names=['Names','Births'])

# Method 1:
Sorted = df.sort(['Births'], ascending=False)
print Sorted.head(1)

# Method 2:
print df['Births'].max()
#if df['Births'].max() ==df['Births']:


print "\nLets Present Data!"
# Create graph
df['Births'].plot()

# Maximum value in the data set
MaxValue = df['Births'].max()

# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print "The most popular name"
print df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used

plt.show()

