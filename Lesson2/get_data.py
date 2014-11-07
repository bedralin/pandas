# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number

# Enable inline plotting
#matplotlib inline

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

print "\nGet Data!"

Location="./births1880.txt"
df=pd.read_csv(Location)

print "df.info() is now"
print df.info()

print "df.head() will print only first 5 records"
print df.head()

df = pd.read_csv(Location, header=None)
print "df.info() is now with no header"
print df.info()

print "df.tail() will look at last 5 items"
print df.tail()

df = pd.read_csv(Location, names=['Names','Births'])
print "df.heads(7) with specific names"
print df.head(7)


