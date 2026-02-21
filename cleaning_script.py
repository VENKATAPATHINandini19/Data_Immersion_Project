import pandas as pd

# Load dataset
df = pd.read_excel("sales_dataset_raw.xlsx")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing Age
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing Gender
df["Gender"].fillna("unknown", inplace=True)

# Standardize Gender
df["Gender"] = df["Gender"].str.lower().replace({"m": "male", "f": "female"})

# Standardize Country
df["Country"] = df["Country"].str.lower().replace({"u.s.a": "usa", "india": "india"})

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Total_Sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Save cleaned dataset
df.to_csv("cleaned_sales_dataset.csv", index=False)

print("Data cleaning completed successfully!")