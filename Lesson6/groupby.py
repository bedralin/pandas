# Import libraries
import pandas as pd
import sys

print 'Python version ' + sys.version
print 'Pandas version: ' + pd.__version__

# Our small data set
d = {'one':[1,1,1,1,1],
     'two':[2,2,2,2,2],
     'letter':['a','a','b','b','c']}
print "New data (dict): ",d

# Create dataframe
df = pd.DataFrame(d)
print "New DataFrame df=pd.DataFrame(d)"
print df

# Create group object
print "one=df.groupby('letter')"
one = df.groupby('letter')

# Apply sum function
print "one.sum()"
one.sum()
print one.sum()

print "one"
print one

print "letterone = df.groupby(['letter','one']).sum()"
letterone = df.groupby(['letter','one']).sum()
print letterone

print "letterone.index"
print letterone.index

print "letterone = df.groupby(['letter','one'], as_index=False).sum()"
letterone = df.groupby(['letter','one'], as_index=False).sum()
print letterone

print "letterone.index"
print letterone.index

