# Import modules
import datadotworld as dw
import sys

# Import a dataset
refugee_dataset = dw.load_dataset('nripper/refugee-host-nations')

# Get size of dataset
sys.getsizeof(refugee_dataset)

# List of all the data files in the set
dataframes = refugee_dataset.dataframes
for df in dataframes:
    pp.pprint(df)

# print all of the files in the dataset
resources = refugee_dataset.describe()['resources']
pp.pprint('name:')
for r in resources:
    pp.pprint(r['format'])
pp.pprint('\ntype of file:')
for r in resources:
    pp.pprint(r['format'])    
