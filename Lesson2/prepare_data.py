# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number

# Enable inline plotting
#matplotlib inline

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

print "\nPrepare Data!"

Location="./births1880.txt"
df=pd.read_csv(Location,names=['Names','Births'])

# Method 1:
print "Unique names: "
df['Names'].unique()

# If you actually want to print the unique values:
for x in df['Names'].unique():
    print x

# Method 2:
print df['Names'].describe()

print "Since we have multiple values per baby name, we must aggregate this data so only one baby name appear once by using groupby function!"
# Create a groupby object
name = df.groupby('Names')

# Apply the sum function to the groupby object
df = name.sum()
print df
