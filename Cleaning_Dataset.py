import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the dataset
dataset_path = r"C:\Users\PC\Desktop\Best_Intern\Applications_for_Machine_Learning_internship_edited.xlsx - Sheet1.csv"
df = pd.read_csv(dataset_path)

# Convert all columns to numeric
df = df.apply(pd.to_numeric, errors='coerce')

# Handling Missing Values
df = df.fillna(df.mean())  # Fill missing values with the mean

# Handling Duplicates
df = df.drop_duplicates()

# Data Transformation
df = pd.get_dummies(df)  # Convert categorical variables to one-hot encoding

# Scale numerical variables using StandardScaler
scaler = StandardScaler()
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Save the cleaned dataset
cleaned_dataset_path = r"C:\Users\PC\Desktop\Best_Intern\Cleaned_Dataset.xlsx"
df.to_excel(cleaned_dataset_path, index=False)

# Print the first few rows of the cleaned dataset
print(df.head())
