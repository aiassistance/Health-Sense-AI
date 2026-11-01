import pandas as pd
from sklearn.model_selection import StratifiedKFold

# Load training dataset
df = pd.read_csv("data/raw/Training.csv")

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

# Remove exact duplicate rows
df = df.drop_duplicates()

# Separate features and target
X = df.drop(columns=["prognosis"])
y = df["prognosis"]

# Display dataset information
print("Dataset shape:", df.shape)
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Unique diseases:", y.nunique())
print("Unique symptom patterns:", X.drop_duplicates().shape[0])
# Check records available for each disease
print("\nRecords per disease:")
print(y.value_counts().sort_values())
disease_counts = y.value_counts()

print("\nMinimum records:", disease_counts.min())
print("Maximum records:", disease_counts.max())
print("Average records:", disease_counts.mean())
print("Diseases with fewer than 6 records:",
      (disease_counts < 6).sum())
print("\nComplete disease distribution:")
print(disease_counts.sort_values())

print("\nMinimum:", disease_counts.min())
print("Maximum:", disease_counts.max())
print(disease_counts.min())
# Create 5-fold stratified cross-validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for fold, (train_index, val_index) in enumerate(skf.split(X, y), 1):
    print(f"\nFold {fold}")
    print("Training records:", len(train_index))
    print("Validation records:", len(val_index))