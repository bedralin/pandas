import pandas as pd
import sys

print 'Python version ' + sys.version
print 'Pandas version: ' + pd.__version__

# Create a dataframe with dates as your index
States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL'] 
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = pd.date_range('1/1/2012', periods=10, freq='MS')
print "idx: ",idx
df1 = pd.DataFrame(data, index=idx, columns=['Revenue'])
print "df1: ",df1
df1['State'] = States

# Create a second dataframe
data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = pd.date_range('1/1/2013', periods=10, freq='MS')
df2 = pd.DataFrame(data2, index=idx2, columns=['Revenue'])
df2['State'] = States

print "\n1st DataFrame:"
print df1
print "\n2nd DataFrame:"
print df2

print "Combine DataFrames using df=pd.concat([df1,df2])"
df=pd.concat([df1,df2])
print df

print "\nWAYS TO CALCULATE OUTLIERS\n"

# Method 1

# make a copy of original df
newdf = df.copy()

newdf['x-Mean'] = abs(newdf['Revenue'] - newdf['Revenue'].mean())
newdf['1.96*std'] = 1.96*newdf['Revenue'].std()  
newdf['Outlier'] = abs(newdf['Revenue'] - newdf['Revenue'].mean()) > 1.96*newdf['Revenue'].std()
print "Method 1 to make a copy of original df!"
print newdf


 



