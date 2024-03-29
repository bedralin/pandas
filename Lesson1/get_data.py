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

print "\n"+"Get Data Now:"
Location = r'./births1880.csv'
df = pd.read_csv(Location)

print df

print "\nTry again, because there was no header:"
df = pd.read_csv(Location, header=None)
print df

print "\nTry again with a header header:"
df = pd.read_csv(Location, names=['Names','Births'])
print df



