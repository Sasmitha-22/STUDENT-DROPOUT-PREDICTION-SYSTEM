# 🎓 Student Dropout Prediction System

## 📌 Problem Statement

Student dropout is a critical issue in educational institutions, affecting both academic performance and institutional reputation. Early identification of students at risk enables timely intervention and support.
This project aims to develop a Machine Learning-based prediction system that classifies students into:
- Dropout  
- Enrolled  
- Graduate  
based on academic performance and socio-economic factors.

## ⚙️ Project Pipeline
<img width="309" height="343" alt="image" src="https://github.com/user-attachments/assets/0cff4ee2-7420-46c5-bab7-c02af2ecfd2f" />


## 📊 Dataset Details

- Source: Kaggle  
- Dataset Type: Structured tabular data  
- Number of Attributes: 36 features + 1 target variable  

### 📖 Description:
The dataset contains student-related information including:
- Academic performance
- Demographic details
- Financial status
- Enrollment information

### 🔑 Selected Features (for model deployment):
- Age at Enrollment  
- Gender  
- 1st Semester Grade  
- 2nd Semester Grade  
- Tuition Fees Status  
- Previous Qualification Grade  

### 🎯 Target Variable:
- 0 → Dropout  
- 1 → Enrolled  
- 2 → Graduate  

## 🤖 Model Details

### 🔹 Supervised Learning Algorithms:
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Tree  
- Random Forest ⭐ (Best Performing Model)

### 🔹 Unsupervised Learning Algorithms:
- K-Means Clustering  
- Hierarchical Clustering  
- DBSCAN  
- Apriori Algorithm  

## 🏆 Best Model Selection

- Selected Model: Random Forest Classifier  
- Reason:  
  - High accuracy  
  - Better generalization  
  - Handles feature importance effectively  

## 🚀 Model Deployment

The final model is deployed using:
- **Backend**: Flask  
- **Frontend**: HTML (Beige-themed UI)  
- **Functionality**:
  - User inputs student details  
  - Model predicts outcome  
  - Displays recommendation  

## 📦 Required Libraries

•	Python 3.x 

•	Flask 

•	Pandas 

•	NumPy 

•	Scikit-learn 

•	Pickle


## 🧠 Key Features

•	Predicts student academic outcome

•	Uses Machine Learning models

•	Web-based interface using Flask 

•	Provides recommendations


## SAMPLE OUTPUT
<img width="475" height="327" alt="image" src="https://github.com/user-attachments/assets/639ba178-1d93-4a7f-93d9-4ed1978ff76e" />
<img width="436" height="329" alt="image" src="https://github.com/user-attachments/assets/5a65f81f-9d09-4144-b0df-1ace4fa5789c" />


## 👥 Team Members

•	Pooja Akshaya A – 24BIT082 

•	Sasmitha V – 24BIT108 

•	Yashwanth R – 24BIT133

## 🚀 Steps to run

### ✅ Prerequisites
Make sure you have the following installed on your computer:
- Python (version 3.x)
- Git

---

### 📥 Step 1: Clone the Repository
Open Command Prompt and run:
git clone https://github.com/Sasmitha-22/STUDENT-DROPOUT-PREDICTION-SYSTEM.git

### 📂 Step 2: Go Into the Project Folder
cd STUDENT-DROPOUT-PREDICTION-SYSTEM

### 📦 Step 3: Install Required Libraries
pip install -r requirements.txt

### ▶️ Step 4: Run the Application
python app.py

### 🌐 Step 5: Open in Browser
http://127.0.0.1:5000

## 🌐 Live Demo
https://student-dropout-prediction-system-u4mt.onrender.com

---

## 📊 Prediction Output
- 🔴 **Dropout** - High risk of dropping out
- 🟡 **Enrolled** - Currently enrolled, monitor performance
- 🟢 **Graduate** - Likely to graduate successfully

