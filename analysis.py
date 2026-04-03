import pandas as pd

# Simple script to display dataset details

df = pd.read_csv("dataset.csv")

print("===== HEAD =====")
print(df.head())
print()

print("===== COLUMN NAMES =====")
print(df.columns.tolist())
print()

print("===== DATA TYPES =====")
print(df.dtypes)
print()

print("===== MISSING VALUES =====")
print(df.isnull().sum())
print()

print("===== SUMMARY STATISTICS =====")
print(df.describe())
print()

print("===== UNIQUE VALUE COUNTS =====")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")