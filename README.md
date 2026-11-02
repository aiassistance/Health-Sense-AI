HealthSense AI

Machine Learning-Based Disease Prediction System

Live Demo: https://health-sense-ai-seven.vercel.app/

Backend API: https://health-sense-ai-1.onrender.com/

API Documentation: https://health-sense-ai-1.onrender.com/docs

---

Project Overview

HealthSense AI is an educational machine-learning application that analyzes user-selected symptoms and generates the top three possible disease-category predictions using a trained classification model.

The application combines a React frontend, FastAPI backend, and Random Forest classification model to provide an interactive symptom-based prediction experience.

Features

- Symptom Selection: Select from 132 available symptoms.
- Symptom Search: Search and filter symptoms easily.
- Selected Symptoms: View, remove, and manage selected symptoms.
- Machine Learning Predictions: Generate the top three predicted disease categories.
- Interactive Interface: User-friendly React dashboard.
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
Model Persistence| Joblib
Development Tools| VS Code, Git, GitHub
Deployment| Vercel, Render
AI Development Assistant| ChatGPT

AI and Machine Learning Implementation

The project uses supervised machine learning to classify disease categories based on selected symptoms.

- Processed 132 symptom features.
- Worked with 41 disease categories.
- Trained a Random Forest classification model.
- Also explored Logistic Regression for model comparison.
- Evaluated model performance using stratified five-fold cross-validation.
- Integrated the trained model with FastAPI for prediction requests.
- Generated the top three model predictions with corresponding model scores.

Model Evaluation

- Random Forest achieved 100% average accuracy in five-fold stratified cross-validation on the processed dataset.

Important: This result is specific to the supplied dataset. The dataset contains only 304 unique symptom patterns after duplicate removal, and the supplied testing dataset has substantial overlap with training patterns. This result does not establish real-world or clinical accuracy.

AI-Assisted Development

ChatGPT was used as an AI development assistant throughout the project to support:

- Coding Assistance: Exploring implementation approaches and understanding code structure.
- Debugging: Identifying errors and understanding possible solutions.
- Concept Learning: Understanding Python, Machine Learning algorithms, APIs, and deployment concepts.
- Problem Solving: Exploring alternative approaches and improving implementation.
- Documentation: Organizing technical explanations and project documentation.

AI-generated suggestions were reviewed and tested as learning support during development to build a better understanding of the implementation.

Machine Learning Workflow

1. Dataset collection and exploration.
2. Removal of missing and duplicate records.
3. Separation of symptom features and disease labels.
4. Model training using Random Forest and Logistic Regression.
5. Model evaluation using stratified five-fold cross-validation.
6. Saving the trained model using Joblib.
7. Integrating the model with FastAPI.
8. Connecting the React frontend to the backend API.
9. Deploying the frontend and backend.

Dataset

The project uses the Disease Prediction Using Machine Learning dataset from Kaggle.

Dataset Source:
https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning

The dataset contains symptom-based records covering 41 disease categories.

Project Structure

Health-Sense-AI/
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

git clone https://github.com/aiassistance/Health-Sense-AI.git
cd Health-Sense-AI

2. Create a virtual environment

python -m venv .venv

Activate it on Windows PowerShell:

.venv\Scripts\Activate.ps1

3. Install Python dependencies

pip install -r requirements.txt

4. Start the FastAPI backend

Run from the project root:

python -m uvicorn backend.main:app --reload

Backend URL: http://127.0.0.1:8000

API Documentation: http://127.0.0.1:8000/docs

5. Start the React frontend

Open a second terminal:

cd frontend
npm install
npm run dev

Frontend URL: http://localhost:5173/

API Endpoints

Method| Endpoint| Description
GET| "/"| Check backend status
GET| "/symptoms"| Retrieve available symptoms
POST| "/predict"| Generate disease-category predictions

Interactive API documentation:

https://health-sense-ai-1.onrender.com/docs

Deployment

The application is deployed using:

- Frontend: Vercel
- Backend: Render
- Version Control: GitHub

Live Application:
https://health-sense-ai-seven.vercel.app/

Limitations

- The processed dataset contains only 304 unique symptom patterns.
- The supplied testing dataset has substantial overlap with training patterns.
- Cross-validation results do not establish real-world medical accuracy.
- Model scores are not clinically calibrated probabilities.
- The application does not consider patient history, physical examination, age, or other clinical factors.

Disclaimer

This project is developed strictly for educational purposes. It is not a medically validated diagnostic tool and must not be used for self-diagnosis or treatment decisions. Always consult a qualified healthcare professional for medical advice.

Author

Kotireddy Vanteddu

B.Tech – Computer Science and Machine Learning

GitHub: https://github.com/aiassistance

---
