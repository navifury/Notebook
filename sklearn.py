from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load the correct CSV
df = pd.read_csv("sample_data.csv.txt")  # <-- Correct file name

# Make a copy
df_label = df.copy()

# Initialize label encoder
le = LabelEncoder()

# Encode Gender and Passed columns
df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender'])
df_label['Passed_Encoded'] = le.fit_transform(df_label['Passed'])  # Corrected column name

# Show encoded data
print('\nLabel Encoded Data')
print(df_label[['Name','Gender','Gender_Encoded','Passed','Passed_Encoded']])
