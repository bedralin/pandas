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

print "\n"+"Prepare Data Now:"
Location = "./births1880.csv"
df = pd.read_csv(Location, names=['Names','Births'])
# Check data type of the columns
print "Check data type of colums:\n",df.dtypes

# Check data type of Births column
print "Check data type of Births column:\n",df.Births.dtype




