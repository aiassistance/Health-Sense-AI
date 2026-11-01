import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/disease_prediction_model.pkl")

# Load training dataset to get symptom names
df = pd.read_csv("data/raw/Training.csv")

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

# Separate symptom columns
symptoms = df.drop(columns=["prognosis"]).columns

print("Model loaded successfully!")
print("Total symptoms:", len(symptoms))
# Create empty input for all symptoms
input_data = [0] * len(symptoms)

# Select symptoms
selected_symptoms = [
    "itching",
    "skin_rash",
    "nodal_skin_eruptions"
]

# Mark selected symptoms as 1
for symptom in selected_symptoms:
    if symptom in symptoms:
        index = list(symptoms).index(symptom)
        input_data[index] = 1

# Convert input into DataFrame
input_df = pd.DataFrame([input_data], columns=symptoms)

print("\nSelected symptoms:", selected_symptoms)
# Generate prediction
prediction = model.predict(input_df)

print("\nPredicted condition:", prediction[0])
# Get prediction probabilities
probabilities = model.predict_proba(input_df)

# Get top 3 predictions
top_3 = probabilities[0].argsort()[-3:][::-1]

print("\nTop 3 model predictions:")

for index in top_3:
    disease = model.classes_[index]
    probability = probabilities[0][index] * 100

    print(f"{disease}: {probability:.2f}%")