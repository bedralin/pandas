# Import libraries
import pandas as pd
import sys

print 'Python version ' + sys.version
print 'Pandas version: ' + pd.__version__

# Our small data set
d = [0,1,2,3,4,5,6,7,8,9]

# Create dataframe
df = pd.DataFrame(d)
print d
print df

# Lets change the name of the column
df.columns = ['Rev']
print "Lets change name of column"
print df

# Lets add a column
df['NewCol'] = 5
print "Lets add a column"
print df

# Lets modify our new column
df['NewCol'] = df['NewCol'] + 1
print "Lets modify our new column"
print df

# We can delete columns
del df['NewCol']
print "We can delete columns"
print df

# Lets add a couple of columns
df['test'] = 3
df['col'] = df['Rev']
print "Lets add a couple of columns"
print df

# If we wanted, we could change the name of the index
i = ['a','b','c','d','e','f','g','h','i','j']
df.index = i
print "We can change name of index"
print df

print "We can now start to select pieces of the dataframe using loc"
print df.loc['a']

# df.loc[inclusive:inclusive]
print "df.loc[inclusive:inclusive]"
print df.loc['a':'d']

# df.iloc[inclusive:exclusive]
# Note: .iloc is strictly integer position based. It is available from [version 0.11.0] (http://pandas.pydata.org/pandas-docs/stable/whatsnew.html#v0-11-0-april-22-2013) 
print "df.iloc[inclusive:exclusive] but integer position based"
print df.iloc[0:3]

print "df['Rev']"
print df['Rev']

print "df[['Rev', 'test']]"
print df[['Rev', 'test']]

# df['ColumnName'][inclusive:exclusive]
print "df['ColumnName'][inclusive:exclusive]"
print df['Rev'][0:3]

print "df['col'][5:]"
print df['col'][5:]

print "df[['col', 'test']][:3]"
print df[['col', 'test']][:3]

# Select top N number of records (default = 5)
print "df.head() to select top N number of records"
print df.head()

# Select bottom N number of records (default = 5)
print "df.tail() to select bottom N number of records"
print df.tail()







