import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "playoffs_dataset.xlsx"
df = pd.read_excel(file_path)

# Step 1: Rename Columns for Better Readability
df.columns = ["Year", "Position", "Team", "Matches Played", "Won", "Lost", "Net Run Rate","Points", "For Runs","For Overs", "Against Runs", "Against Overs"]

print(df.columns)

# Step 2: Convert Runs & Overs to Numeric
df["For Runs"] = pd.to_numeric(df["For Runs"], errors='coerce')
df["For Overs"] = pd.to_numeric(df["For Overs"], errors='coerce')
df["Against Runs"] = pd.to_numeric(df["Against Runs"], errors='coerce')
df["Against Overs"] = pd.to_numeric(df["Against Overs"], errors='coerce')

# Step 3: Basic Statistics and Overview
print("Dataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Step 4: Visualizations
plt.figure(figsize=(12, 6))
sns.barplot(x="Year", y="Points", data=df, ci=None)
plt.xticks(rotation=45)
plt.title("Total Points per Year")
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x="Net Run Rate", y="Points", hue="Team", data=df)
plt.title("Net Run Rate vs. Points")
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(x="Year", y="Won", data=df, estimator="sum", ci=None)
plt.title("Total Wins Over the Years")
plt.show()

# Step 5: Save Cleaned & Processed Dataset
cleaned_file_path = "playoffs_dataset_cleaned.xlsx"
df.to_excel(cleaned_file_path, index=False)

print(f"EDA completed! The cleaned dataset has been saved as {cleaned_file_path}.")
