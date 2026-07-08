# 📊 Learnlytics – Student Performance Analysis Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/React-Vite-61DAFB?logo=react" />
  <img src="https://img.shields.io/badge/Flask-Python-black?logo=flask" />
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql" />
  <img src="https://img.shields.io/badge/Power%20BI-Analytics-F2C811?logo=powerbi" />
  <img src="https://img.shields.io/badge/License-Educational-blue" />
</p>

## 🚀 Overview

**Learnlytics** is a Full-Stack Student Performance Analysis Dashboard developed to help educational institutions monitor academic performance through interactive analytics and intelligent insights.

The application combines **React**, **Flask**, **MySQL**, **Machine Learning**, and **Power BI** to provide administrators and educators with a centralized platform for analyzing student performance, identifying low-performing students, monitoring attendance, and making data-driven academic decisions.

---

# ✨ Features

### 📈 Dashboard
- Total Students KPI
- Average Score KPI
- Pass Percentage KPI
- Subject-wise Performance
- Score Trend Analysis
- Pass / Fail Distribution
- Risk Band Analysis
- Student Search & Filtering
- Sorting Options
- CSV Export

---

### 📊 Analytics
- Low Performer Prediction
- Risk Analysis
- Attendance Analysis
- Intervention Queue
- Performance Trends
- Student Insights

---

### 👨‍💼 Admin Features
- Add Student
- Update Student
- Delete Student
- Import Student Dataset
- Export CSV
- Dashboard Management

---

### 👨‍🎓 Student Features
- View Academic Performance
- View Subject Marks
- Attendance Information
- Performance Analytics

---

# 🧠 Machine Learning Features

The system predicts academic risk based on multiple student attributes.

### Input Features

- Attendance Percentage
- Internal Marks
- Assignment Scores
- Subject Performance
- Previous Results

### Output

- Low Performer Prediction
- Student Risk Level
- Intervention Recommendation
- Performance Analysis

---

# 🏗️ System Architecture

```
React Frontend
        │
    REST APIs
        │
Flask Backend
        │
    MySQL Database
        │
 Machine Learning
        │
   Power BI Dashboard
```

---

# 💻 Tech Stack

## Frontend

- React (Vite)
- HTML5
- CSS3
- JavaScript
- Axios
- Framer Motion
- Chart.js

## Backend

- Python
- Flask
- Flask REST API
- Flask-CORS

## Database

- MySQL
- XAMPP

## Analytics

- Power BI
- Chart.js

## Machine Learning

- Pandas
- NumPy
- Scikit-learn

---

# 📂 Project Structure

```
Learnlytics/

├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── assets/
│   │   └── App.jsx
│   │
│   └── package.json
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── database/
│   ├── utils/
│   ├── config.py
│   └── app.py
│
├── powerbi/
│
├── database/
│
├── screenshots/
│
├── README.md
│
└── requirements.txt
```

---

# 📊 Dashboard Modules

## Dashboard

- KPI Cards
- Student Performance
- Subject Performance
- Score Trends
- Pass Percentage
- Student Filters

## Analytics Studio

- Risk Prediction
- Low Performer Analysis
- Attendance Analysis
- Intervention Queue
- Performance Insights

---

# 🔌 REST API

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/students` | Get all students |
| GET | `/api/students/:id` | Get student details |
| POST | `/api/students` | Add student |
| PUT | `/api/students/:id` | Update student |
| DELETE | `/api/students/:id` | Delete student |
| GET | `/api/summary` | Dashboard summary |
| GET | `/api/analytics/trends` | Trend analytics |
| GET | `/api/analytics/risk` | Risk prediction |
| GET | `/api/powerbi/dataset` | Power BI dataset |

---

# ⚡ Installation

## Clone Repository

```bash
git clone https://github.com/harshinikankati/Learnlytics.git
```

---

## Backend

```powershell
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

---

## Frontend

```powershell
cd frontend

npm install

npm run dev
```

---

# 📊 Power BI Integration

Learnlytics supports Power BI integration using:

- MySQL Database Connection
- Flask REST API
- Custom Analytics Dataset

Suggested Dashboards:

- Subject Performance
- Student Performance
- Attendance Analysis
- Pass / Fail Ratio
- Risk Prediction
- Monthly Trends

---

# 🎯 Future Enhancements

- AI-based Personalized Learning Recommendations
- Parent Portal
- Email Notifications
- Cloud Deployment
- Real-time Analytics
- Mobile Application
- Student Performance Forecasting

---

# 👩‍💻 Developer

**Sri Harshini K**
**Sindhuja P**
**Rachana N**

B.Tech – Computer Science Engineering (Data Science)

Sridevi Women's Engineering College

GitHub: https://github.com/harshinikankati

LinkedIn: https://www.linkedin.com/in/kankati-sri-harshini-4b39a4368

---

# 📜 License

This project is developed for educational and academic purposes.
