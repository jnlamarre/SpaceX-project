import pandas as pd

# Create initial data as a dictionary
data = {
    'rocket': ['Falcon 1', 'Falcon 9', 'Falcon Heavy'],
    'launches': [5, 100, 3]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Print the full DataFrame
print(df)

# Select and print the 'rocket' column
print(df['rocket'])

# Filter the DataFrame for rockets with more than 5 launches
filtered_df = df[df['launches'] > 5]
print(filtered_df)

# Add a new column for launch success rate
df['success_rate'] = [0.4, 0.98, 1.0]
