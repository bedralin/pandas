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
#plt.show()

print "Data for 2012 only now"
Daily.loc['FL']['2012':].plot()
Daily.loc['GA']['2012':].plot()
Daily.loc['NY']['2012':].plot()
Daily.loc['TX']['2012':].plot();

print "We will be using the attribute transform instead of apply. The reason is that transform will keep the shape(# of rows and columns) of the dataframe the same and apply will not. By looking at the previous graphs, we can realize they are not resembling a gaussian distribution, this means we cannot use summary statistics like the mean and stDev. We use percentiles instead. Note that we run the risk of eliminating good data.\n"
# Calculate Outliers
StateYearMonth = Daily.groupby([Daily.index.get_level_values(0), Daily.index.get_level_values(1).year, Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Upper'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper']) 

# Remove Outliers
Daily = Daily[Daily['Outlier'] == False]

print "The dataframe named Daily will hold customer counts that have been aggregated per day. The original data (df) has multiple records per day. We are left with a data set that is indexed by both the state and the StatusDate. The Outlier column should be equal to False signifying that the record is not an outlier.\n"

print "With Outliers:"
print Daily.head()

print "Combine all Markets"
# Combine all markets

# Get the max customer count by Date
ALL = pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount'] # rename column

# Group by Year and Month
YearMonth = ALL.groupby([lambda x: x.year, lambda x: x.month])

# What is the max customer count per Year and Month
ALL['Max'] = YearMonth['CustomerCount'].transform(lambda x: x.max())
print ALL.head()

print "Create BHAG dataframe"
# Create the BHAG dataframe
data = [1000,2000,3000]
idx = pd.date_range(start='12/31/2011', end='12/31/2013', freq='A')
BHAG = pd.DataFrame(data, index=idx, columns=['BHAG'])
print BHAG

print "Combine BHAG and the ALL data set"
# Combine the BHAG and the ALL data set 
combined = pd.concat([ALL,BHAG], axis=0)
combined = combined.sort(axis=0)
print combined.tail()

fig, axes = plt.subplots(figsize=(12, 7))

combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
combined['Max'].plot(color='blue', label='All Markets')
plt.legend(loc='best');

# Group by Year and then get the max value per year
Year = combined.groupby(lambda x: x.year).max()
print Year

# Add a column representing the percent change per year
Year['YR_PCT_Change'] = Year['Max'].pct_change(periods=1)
print Year

print "\nPRESENT DATA\n"
# First Graph
ALL['Max'].plot(figsize=(10, 5), label='ALL Markets');#plt.title('ALL Markets')

# Last four Graphs
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
fig.subplots_adjust(hspace=1.0) ## Create space between plots

Daily.loc['FL']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0],label='FL')
Daily.loc['GA']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,1]) 
Daily.loc['TX']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,0]) 
Daily.loc['NY']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,1]) 

# Add titles
axes[0,0].set_title('Florida')
axes[0,1].set_title('Georgia')
axes[1,0].set_title('Texas')
axes[1,1].set_title('North East');

plt.show()
