from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Configuration des règles CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines (à restreindre en prod)
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les headers
)

# Instrumentation Prometheus
Instrumentator().instrument(app).expose(app)

# Connexion PostgreSQL
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@postgres:5432/mydb")

def check_db_connection():
    try:
        conn = psycopg2.connect(DB_URL)
        conn.close()
        return True
    except:
        return False

@app.get("/ping")
def ping():
    db_status = check_db_connection()
    return {"message": "Pong!", "db_status": db_status}

# Pour lancer : uvicorn main:app --reload --host 0.0.0.0 --port 8000
