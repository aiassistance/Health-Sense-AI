import pandas as pd

# Load the training dataset
df = pd.read_csv("data/raw/Training.csv")

# Display first 5 rows
print(df.head())
# Dataset dimensions
print("Dataset Shape:", df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()

# Disease categories
print("\nDisease Categories:")
print(df["prognosis"].unique())

# Total number of diseases
print("\nTotal Diseases:", df["prognosis"].nunique())
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Count records for each disease
print("\nDisease Distribution:")
print(df["prognosis"].value_counts())

# Check data types
print("\nData Types:")
print(df.dtypes.value_counts())
# Find columns containing missing values
print("\nColumns with Missing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Check columns with all values missing
print("\nCompletely Empty Columns:")
print(df.columns[df.isnull().all()].tolist())

# Display duplicate examples
print("\nDuplicate Examples:")
print(df[df.duplicated()].head())

# Check disease record counts
print("\nDisease Counts:")
print(df["prognosis"].value_counts().head(10))
# Remove the completely empty column for analysis only
clean_check = df.drop(columns=["Unnamed: 133"])

# Count unique complete records
print("\nUnique Complete Records:")
print(clean_check.drop_duplicates().shape[0])

# Count unique symptom combinations
X = clean_check.drop(columns=["prognosis"])
print("\nUnique Symptom Combinations:")
print(X.drop_duplicates().shape[0])

# Count unique disease labels
print("\nUnique Diseases:")
print(clean_check["prognosis"].nunique())

# Check minimum and maximum disease records
print("\nDisease Distribution Summary:")
print(clean_check["prognosis"].value_counts().describe())

# Check whether duplicate records have different labels
print("\nDifferent labels for identical symptom combinations:")
print(
    clean_check.groupby(list(X.columns))["prognosis"]
    .nunique()
    .gt(1)
    .sum()
)
# Load testing dataset
test_df = pd.read_csv("data/raw/Testing.csv")

# Inspect testing dataset
print("\n========== TESTING DATASET ==========")

print("Testing Shape:", test_df.shape)

print("\nMissing Values:")
print(test_df.isnull().sum().sum())

print("\nDuplicate Records:")
print(test_df.duplicated().sum())

print("\nUnique Diseases:")
print(test_df["prognosis"].nunique())

print("\nDisease Distribution:")
print(test_df["prognosis"].value_counts())

# Check completely empty columns
print("\nCompletely Empty Columns:")
print(test_df.columns[test_df.isnull().all()].tolist())

# Compare training and testing columns
train_columns = set(df.dropna(axis=1, how="all").columns)
test_columns = set(test_df.dropna(axis=1, how="all").columns)

print("\nColumns missing from Testing:")
print(train_columns - test_columns)

print("\nExtra columns in Testing:")
print(test_columns - train_columns)
# Remove completely empty training column
train_clean = df.dropna(axis=1, how="all")

# Separate symptom columns
X_train = train_clean.drop(columns=["prognosis"])
X_test = test_df.drop(columns=["prognosis"])

# Check whether symptom columns match
print("\nFeature columns match:",
      list(X_train.columns) == list(X_test.columns))

# Find overlapping symptom patterns
train_patterns = set(
    map(tuple, X_train.drop_duplicates().values)
)

test_patterns = set(
    map(tuple, X_test.values)
)

overlap = train_patterns.intersection(test_patterns)

print("\nUnique training patterns:", len(train_patterns))
print("Unique testing patterns:", len(test_patterns))
print("Overlapping patterns:", len(overlap))
# Check whether overlapping patterns have matching disease labels

train_clean = df.dropna(axis=1, how="all")

train_compare = train_clean.drop_duplicates(
    subset=X_train.columns
)

test_compare = test_df.copy()

comparison = test_compare.merge(
    train_compare,
    on=list(X_train.columns),
    how="inner",
    suffixes=("_test", "_train")
)

print("\nOverlapping rows:", len(comparison))

print(
    "Matching disease labels:",
    (comparison["prognosis_test"] ==
     comparison["prognosis_train"]).sum()
)

print(
    "Different disease labels:",
    (comparison["prognosis_test"] !=
     comparison["prognosis_train"]).sum()
)