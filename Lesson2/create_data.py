# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number

# Enable inline plotting
#matplotlib inline

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

print "\nCreate Data!"
# The inital set of baby names
names = ['Bob','Jessica','Mary','John','Mel']

random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

# Print first 10 records
print random_names[:10]

# The number of births per name for the year 1880
births = [random.randint(low=0,high=1000) for i in range(1000)]
print births[:10]
print len(births)
print type(births)

BabyDataSet = zip(random_names,births)
print BabyDataSet[:10]

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print "Creating DataFrame (pandas) object in a format similar to a sql table or excel spreadsheet:\n",df[:10]

print "Export DataFrame object to txt file"
df.to_csv('births1880.txt',index=False,header=False)

