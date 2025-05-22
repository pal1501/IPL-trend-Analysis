import pandas as pd
'''
# Load Excel file
df = pd.read_excel("dataset_ipl.xlsx", engine="openpyxl")

print("Before Cleaning: ", df.columns.tolist())
# Clean column names
df.columns = df.columns.str.strip().str.lower()
print("After Cleaning: ", df.columns.tolist())

# Display the first few rows and summary info
df.head(), df.info()
# Step 1: Drop unnecessary or mostly-null columns
matches_cleaned = df.drop(columns=['method'])

# Step 2: Handle missing values
# Fill missing 'city' with 'Unknown'
matches_cleaned['city'] = matches_cleaned['city'].fillna('Unknown')

# Fill missing 'player_of_match' and 'winner' with 'Not Awarded' / 'No Result'
matches_cleaned['player_of_match'] = matches_cleaned['player_of_match'].fillna('Not Awarded')
matches_cleaned['winner'] = matches_cleaned['winner'].fillna('No Result')

# Fill missing result_margin, target_runs, target_overs with 0 for simplicity
matches_cleaned['result_margin'] = matches_cleaned['result_margin'].fillna(0)
matches_cleaned['target_runs'] = matches_cleaned['target_runs'].fillna(0)
matches_cleaned['target_overs'] = matches_cleaned['target_overs'].fillna(0)

# Step 3: Standardize team names (e.g., remove extra spaces, make consistent casing)
matches_cleaned['team1'] = matches_cleaned['team1'].str.strip()
matches_cleaned['team2'] = matches_cleaned['team2'].str.strip()
matches_cleaned['toss_winner'] = matches_cleaned['toss_winner'].str.strip()
matches_cleaned['winner'] = matches_cleaned['winner'].str.strip()

# Step 4: Check for and remove any duplicate rows
matches_cleaned = matches_cleaned.drop_duplicates()

# Step 5: Reset index after cleaning
matches_cleaned.reset_index(drop=True, inplace=True)

# Display cleaned dataset info
matches_cleaned.info()

# Save cleaned data
df.to_excel("cleaned_dataset_ipl.xlsx", index=False, engine="openpyxl")

print("Data cleaning completed!")
'''


# Load the dataset
file_path = "playoffs_dataset.xlsx"
df = pd.read_excel(file_path)

# Step 1: Rename Columns for Better Readability
df.columns = ["year", "position", "team", "matches played", "won", "lost", "net run rate", "for", "against", "points"]

# Step 2: Handle Missing Values (Fill with placeholders or drop if necessary)
df.fillna({"net run rate": 0, "for": "Unknown", "against": "Unknown"}, inplace=True)

# Step 3: Standardize Team Names (Ensure consistency)
df["team"] = df["team"].str.strip().str.upper()

# Step 4: Extract Runs and Overs Separately from "For" and "Against" columns
df[["for Runs", "for Overs"]] = df["for"].str.split("/", expand=True)
df[["against Runs", "against Overs"]] = df["against"].str.split("/", expand=True)

# Convert Runs & Overs to Numeric
df["for Runs"] = pd.to_numeric(df["for Runs"], errors='coerce')
df["for Overs"] = pd.to_numeric(df["for Overs"], errors='coerce')
df["against Runs"] = pd.to_numeric(df["against Runs"], errors='coerce')
df["against Overs"] = pd.to_numeric(df["against Overs"], errors='coerce')

# Drop the old "For" and "Against" columns
df.drop(columns=["for", "against"], inplace=True)

# Step 5: Remove Duplicates
df.drop_duplicates(inplace=True)

# Step 6: Save the Cleaned Dataset
cleaned_file_path = "playoffs_dataset_cleaned.xlsx"
df.to_excel(cleaned_file_path, index=False)

print(f"Playoffs dataset cleaned and saved as {cleaned_file_path}!")
