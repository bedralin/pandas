# Import libraries
import pandas as pd
import sys

print 'Python version ' + sys.version
print 'Pandas version: ' + pd.__version__

# Our small data set
d = {'one':[1,1],'two':[2,2]}
i = ['a','b']

# Create dataframe
df = pd.DataFrame(data = d, index = i)
print "index: ",i
print "data: ",d
print "New dataframe"
print  df

print "df.index"
print df.index

# Bring the columns and place them in the index
stack = df.stack()
print "Bring columns and place them in index"
print stack

# The index now includes the column names
print "stack.index shows that index now includes column names"
print stack.index

unstack = df.unstack()
print "unstack=df.unstack()"
print unstack

print "unstack.index"
print unstack.index

transpose = df.T
print "transpose=df.T"
print transpose

print "transpose.index"
print transpose.index









