import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding='ISO-8859-1')

print("SUPERSTORE DATA PROFILING REPORT ")

print("Dataset Shape")
print(f"rows--- {df.shape[0]}")
print(f"columns---{df.shape[1]} \n")

print(df.dtypes)

print((df.isnull().mean() * 100) )

print(df.duplicated().sum(), "\n")


print(f"Discount vs Profit: {df['Discount'].corr(df['Profit']):.3f}")
print(f"Sales vs Quantity: {df['Sales'].corr(df['Quantity']):.3f}")