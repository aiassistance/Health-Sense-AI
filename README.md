HealthSense AI

Machine Learning-Based Disease Prediction System

HealthSense AI is an educational machine-learning application that analyzes user-selected symptoms and generates possible disease-category predictions using a trained classification model.

Features

- Symptom Selection: Select from 132 available symptoms.
- Symptom Search: Search and filter symptoms easily.
- Selected Symptoms: View and remove selected symptoms.
- Machine Learning Predictions: Generate the top three model predictions.
- Interactive Dashboard: User-friendly React interface.
- REST API: FastAPI backend for model predictions.
- Input Validation: Handles empty and invalid symptom selections.

Technologies Used

Category| Technologies
Programming Language| Python
Frontend| React.js, HTML, CSS, JavaScript
Backend| FastAPI
Machine Learning| Scikit-learn
Data Processing| Pandas, NumPy
Model| Random Forest Classifier
Development Tools| VS Code, Git, GitHub

Project Structure

healthcare-diagnosis-assistant/
│
├── backend/
│   └── main.py
│
├── data/
│   └── raw/
│       ├── Training.csv
│       └── Testing.csv
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   └── package.json
│
├── models/
│   └── disease_prediction_model.pkl
│
├── notebooks/
│   ├── 01_dataset_exploration.py
│   ├── 02_data_preparation.py
│   ├── 03_model_training.py
│   └── 04_model_testing.py
│
├── requirements.txt
└── README.md

Installation and Setup

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd healthcare-diagnosis-assistant

2. Create and activate virtual environment

python -m venv .venv

Windows PowerShell:

.venv\Scripts\Activate.ps1

3. Install Python dependencies

pip install -r requirements.txt

4. Start the FastAPI backend

From the project root:

python -m uvicorn backend.main:app --reload

Backend URL: "http://127.0.0.1:8000"

API documentation: "http://127.0.0.1:8000/docs"

5. Start the React frontend

Open a second terminal:

cd frontend
npm install
npm run dev

Frontend URL: "http://localhost:5173/"

Machine Learning Workflow

1. Dataset collection and exploration.
2. Removal of missing and duplicate records.
3. Separation of symptom features and disease labels.
4. Training using Random Forest and Logistic Regression.
5. Model evaluation using stratified five-fold cross-validation.
6. Saving the trained model using Joblib.
7. Integrating the model with FastAPI.
8. Connecting the React frontend to the backend.

Dataset

The project uses the Disease Prediction Using Machine Learning dataset from Kaggle.

Dataset source:
https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning

The dataset contains symptom-based records covering 41 disease categories.

Limitations

- The dataset contains only 304 unique symptom patterns after duplicate removal.
- The supplied testing dataset has substantial overlap with training patterns.
- Cross-validation results do not establish real-world medical accuracy.
- Model scores are not clinically validated probabilities.
- The system does not consider patient history, examination findings, age, or other clinical factors.

Disclaimer

This project is developed for educational purposes only. It is not a medically validated diagnostic tool and must not be used for treatment decisions. Consult a qualified healthcare professional for medical advice.

Author

Kotireddy Vanteddu

B.Tech – Computer Science and Machine Learning

Project: HealthSense AI