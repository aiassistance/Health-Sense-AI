import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold

# Load training dataset
df = pd.read_csv("data/raw/Training.csv")

# Clean dataset
df = df.dropna(axis=1, how="all")
df = df.drop_duplicates()

# Separate features and target
X = df.drop(columns=["prognosis"])
y = df["prognosis"]

print("Features:", X.shape)
print("Target:", y.shape)
# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X, y)

print("\nModel training completed successfully!")
# Create 5-fold cross-validation
skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# Evaluate model
scores = cross_val_score(
    model,
    X,
    y,
    cv=skf,
    scoring="accuracy"
)

print("\nCross-validation scores:", scores)
print("Average accuracy:", scores.mean())
print("Standard deviation:", scores.std())
# Get predictions using cross-validation
y_pred = cross_val_predict(model, X, y, cv=skf)

# Classification report
print("\nClassification Report:")
print(classification_report(y, y_pred))

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y, y_pred))
# Save trained model
joblib.dump(model, "models/disease_prediction_model.pkl")

print("\nModel saved successfully!")
# Create Logistic Regression model
lr_model = LogisticRegression(max_iter=2000)

# Evaluate Logistic Regression
lr_scores = cross_val_score(
    lr_model, X, y, cv=skf, scoring="accuracy"
)

# Compare models
print("\nMODEL COMPARISON")
print("Random Forest:", scores.mean())
print("Logistic Regression:", lr_scores.mean())