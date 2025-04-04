# 🚀 Déploiement Full Stack Vue/React + FastAPI + PostgreSQL avec Docker Swarm & Kubernetes

Ce projet regroupe un frontend mixte Vite.js + React servi par NGINX, un backend FastAPI, et une base de données PostgreSQL. Deux méthodes de déploiement sont disponibles :

- 🐳 **Docker Swarm**
- ☸️ **Kubernetes**

---

## 📁 Structure du projet
 ├── backend/ 
 │ ├── Dockerfile 
 │ └── main.py 
 ├── frontend/ 
 │ ├── vue-app/ 
 │ ├── react-app/ 
 │ ├── nginx.conf 
 │ └── Dockerfile 
 ├── docker-compose.swarm.yml 
 ├── k8s/ 
 │ ├── backend-deployment.yaml 
 │ ├── backend-service.yaml 
 │ ├── frontend-deployment.yaml 
 │ ├── frontend-service.yaml 
 │ ├── db-deployment.yaml 
 │ └── db-service.yaml

---

## 🧰 Prérequis

- Docker + Docker Swarm (`docker swarm init`)
- Kubernetes (Minikube, kind, etc.)
- Docker Hub ou registre privé pour Docker Swarm

---

##  Déploiement Docker Swarm

### 1. Construire et pousser les images

```bash
# Backend FastAPI
docker build -t mon_dockerhub_user/backend:latest ./backend
docker push mon_dockerhub_user/backend:latest

# Frontend NGINX avec Vue + React
docker build -t mon_dockerhub_user/frontend:latest ./frontend
docker push mon_dockerhub_user/frontend:latest
```

### 2. Déployer la stack
docker stack deploy -c docker-compose.swarm.yml my_app_stack

### 3. Vérifier  le déploiement
docker stack services my_app_stack
docker stack ps my_app_stack
