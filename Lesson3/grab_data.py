# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys

print 'Python version ' + sys.version
print 'Pandas version: ' + pd.__version__

# Location of file
Location ='./Lesson3.xlsx'

# Parse a specific sheet
df = pd.read_excel(Location, 0, index_col='StatusDate')
print "df.dtypes is:"
print df.dtypes

print "df.index is:"
print df.index

print "df.head() is:"
print df.head()

print "\n PREPARE DATA!"

print df['State'].unique()

# Only grab where Status == 1
mask = df['Status'] == 1
df = df[mask]

print df  #Only with Status=1

# Convert NJ to NY
mask = df.State == 'NJ'
df['State'][mask] = 'NY'

print df['State'].unique()

df['CustomerCount'].plot(figsize=(15,5));
#plt.show()

print "There are lot of subsets for States"
sortdf = df[df['State']=='NY'].sort(axis=0)
print sortdf.head(10)

print "Aggregating data using groupby()"
# Group by State and StatusDate
Daily = df.reset_index().groupby(['State','StatusDate']).sum()
print Daily.head()

print "Deleting 'Status'"
del Daily['Status']
print Daily.head()

print "Index of dataframe is: "
# What is index of the dataframe
print Daily.index

print "Select State Index Daily.index.levels[0]"
# Select the State index
print Daily.index.levels[0]

print "Select StatusDate Index Daily.index.levels[1]"
print Daily.index.levels[1]

# Plot graph with State
Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot();
plt.show()
