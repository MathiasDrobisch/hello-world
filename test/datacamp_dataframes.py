# datadotworld module has been imported as dw
import datadotworld as dw

# We've loaded two datasets to use 'int_dataset' and 'fipsCodes_dataset'
int_dataset = dw.load_dataset('https://data.world/jonloyens/intermediate-data-world')
fipsCodes_dataset = dw.load_dataset('https://data.world/uscensusbureau/fips-state-codes')

## Create two dataframes: police_shootings from the 'fatal_police_shootings_data' table of int_dataset and state_abbrvs, from the 'statesfipscodes' table of fipsCodes_dataset
police_shootings = int_dataset.dataframes['fatal_police_shootings_data']
state_abbrvs = fipsCodes_dataset.dataframes['statesfipscodes']
pp.pprint(police_shootings.head(10))

## Merge the two datasets together on the state and stusab fields. Assign to a merged_dataframe variable.
merged_dataframe = police_shootings.merge(state_abbrvs, how = 'left', left_on = 'state', right_on='stusab')


## Add a 'citystate' column to the merged_dataframe dataframe, populating it with the concatinated values from the 'city' and 'state_name' columns, separated by ', '.
merged_dataframe["citystate"]=merged_dataframe["city"] + ", " + merged_dataframe["state_name"]

## Print first 5 rows of merged_dataframe
pp.pprint(merged_dataframe.head(5))


# datadotworld module has been imported as dw
import datadotworld as dw

## Complete the SQL query to select all rows from the `unhcr_all` table where `Year` equals 2010. Assign the query string to a `sql_query` variable.
sql_query = "SELECT * FROM unhcr_all WHERE Year = 2010"

## Use the `query` method of the datadotworld module to run the `sql_query` against the `https://data.world/nrippner/refugee-host-nations` dataset. Assign the results to a `query2010` variable.
query2010 = dw.query('https://data.world/nrippner/refugee-host-nations',sql_query)

## Use the dataframe property of the resulting query to create a dataframe variable named `unhcr2010`
unhcr2010 = query2010.dataframe

## Print the first 5 rows using the head method.
pp.pprint(unhcr2010.head(5))
