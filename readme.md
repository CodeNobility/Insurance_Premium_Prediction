# Insurance Premium Prediction System 🚀

A full-stack Machine Learning application for predicting insurance premium categories using a trained ML model, served via **FastAPI** and consumed by a **Streamlit** frontend.  
Both backend and frontend are fully **Dockerized** and ready for cloud deployment (Render).

---

## 🔥 Project Highlights

- 🔹 Machine Learning model trained using Scikit-learn
- 🔹 Backend API built with FastAPI
- 🔹 Interactive frontend built with Streamlit
- 🔹 Fully Dockerized (backend + frontend)
- 🔹 Cloud-ready (Render compatible)
- 🔹 Clean, scalable, production-style architecture

---

## 🧱 Project Architecture

Insurance_Premium_Prediction/
│
├── backend/
│ ├── app.py # FastAPI entry point
│ ├── config/
│ │ └── city_tier.py # City tier logic
│ ├── Model/
│ │ ├── model.pk1 # Trained ML model
│ │ └── predict.py # Model loading & prediction logic
│ ├── schema/
│ │ └── pydantic_model.py # Request validation schemas
│ ├── Dockerfile # Backend Dockerfile
│ └── requirements.txt # Backend dependencies
│
├── frontend/
│ ├── frontend.py # Streamlit UI
│ ├── Dockerfile # Frontend Dockerfile
│ └── requirements.txt # Frontend dependencies
│
├── myenv/ # Local virtual environment (NOT pushed)
└── README.md

---

## ⚙️ Tech Stack

- **Backend:** FastAPI, Pydantic, Scikit-learn
- **Frontend:** Streamlit
- **ML:** RandomForestClassifier
- **Containerization:** Docker
- **Deployment:** Render
- **Language:** Python 3.10

---

## 🚀 Running Locally (Without Docker)

### Backend 
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
Backend will be available at:
http://localhost:8000


Frontend
cd frontend
pip install -r requirements.txt
streamlit run frontend.py
Frontend will be available at:
http://localhost:8501


🐳 Running with Docker
Build Backend Image
cd backend
docker build -t insurance-backend .
docker run -p 8000:8000 insurance-backend


Build Frontend Image
cd frontend
docker build -t insurance-frontend .
docker run -p 8501:8501 insurance-frontend
☁️ Deployment Strategy (Render)


Backend (FastAPI):
Deployed as a Docker Web Service
Always running (24×7)
Exposes /predict API endpoint

Frontend (Streamlit):
Deployed separately (Docker or Streamlit Cloud)
Communicates with backend using public API URL

Example:
API_URL = "https://your-backend.onrender.com/predict"
📡 API Endpoint
POST /predict


Input:
json
{
  "age": 30,
  "weight": 65,
  "height": 1.7,
  "income_lpa": 6,
  "smoker": false,
  "city": "Delhi",
  "occupation": "private_job"
}
Output:

json
{
  "predicted_category": "Medium",
  "confidence": 87.45
}
🔐 Notes
myenv/ is a local virtual environment and must not be pushed to GitHub.
Docker ensures consistent behavior across machines.
Backend and frontend are intentionally decoupled for scalability.

👨‍💻 Author
Prince Kumar Gupta
B.Tech Data Science
Machine Learning | FastAPI | Docker | Streamlit

⭐ If you like this project, give it a star!