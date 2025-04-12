import requests
import pandas as pd

# Step 1: Fetch data from the SpaceX API
url = 'https://api.spacexdata.com/v4/launches'
response = requests.get(url)
data = response.json()

# Step 2: Convert the JSON data to a DataFrame
df = pd.DataFrame(data)

# Step 3: Print the first five rows
print(df.head())
