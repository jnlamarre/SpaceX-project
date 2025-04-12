import pandas as pd

# Load SpaceX launch data directly using pandas
url = 'https://api.spacexdata.com/v4/launches'
df = pd.read_json(url)

# Print first five rows
print("Preview of SpaceX launches:")
print(df.head())

# Print column names
print("\nColumns:")
print(df.columns)

# Print data types of each column
print("\nData types:")
print(df.dtypes)
