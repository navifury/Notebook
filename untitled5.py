from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load dataset
df = pd.read_csv("sample_data.csv.txt")

# Copy DataFrame
df_label = df.copy()

# Create encoder
le = LabelEncoder()

# Encode columns
df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender'])
df_label['Passed_Encoded'] = le.fit_transform(df_label['passed'])

# Print only first 5 rows
print('\nLabel Encoded Data (First 5 Rows)')
print(df_label[['Name', 'Gender', 'Gender_Encoded', 'passed', 'Passed_Encoded']].head())
