import pandas as pd

# Load the data
df = pd.read_csv('assessments.csv')

# Fill missing values with an empty string
df.fillna('', inplace=True)

# Combine relevant text fields for TF-IDF
df['combined'] = df['name'] + ' ' + df['test_type']

# Save the cleaned data
df.to_csv('cleaned_assessments.csv', index=False)