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

print "\n"+"Create Data Now:"

# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

#zip?

BabyDataSet = zip(names,births)
print BabyDataSet

print "csv file created..."
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print "df is: \n",df
df.to_csv('births1880.csv',index=False,header=False)


