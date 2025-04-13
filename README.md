#  Déploiement Full Stack Vue/React + FastAPI + PostgreSQL avec Docker Swarm & Kubernetes

Ce projet regroupe un frontend mixte Vite.js + React servi par NGINX, un backend FastAPI, et une base de données PostgreSQL. Deux méthodes de déploiement sont disponibles :

- 🐳 **Docker Swarm**
- ☸️ **Kubernetes**


## Prérequis

- Docker (`docker start`)
- Kubernetes (Minikube, Kind, etc.)
- `kubectl` installé et configuré (command-line de K8s)
- Images Docker buildées et poussées dans un registre (Docker Hub, GHCR, etc.) ou accessible en local

##  Déploiement Docker Swarm

### 1. Démarrer Docker Swarm

```bash
docker swarm init
```

### 2. Construire et pousser les images

```bash
# Backend FastAPI
docker build -t mon_dockerhub_user/projet-infonuagique-backend:latest ./backend
docker push mon_dockerhub_user/projet-infonuagique-backend:latest

# Frontend NGINX avec Vue + React
docker build -t mon_dockerhub_user/projet-infonuagique-frontend:latest ./frontend
docker push mon_dockerhub_user/projet-infonuagique-frontend:latest
```

### 3. Déployer la stack
```bash
docker stack deploy -c docker-compose.swarm.yml mon_projet_stack
```
### 4. Vérifier le déploiement
```bash
docker stack services mon_projet_stack
docker stack ps mon_projet_stack
```

##  Déploiement Kubernetes

### 1. Démarrer Minikube (si local)
```bash
minikube start
```

### 2. Créer un namespace (optionnel mais conseillé)
 ```bash
 kubectl create namespace projet-infonuagique
```

### 3. Déployer les ressources Kubernetes
Se placer dans le dossier` k8s/`

```bash
kubectl apply -f . -n projet-infonuagique
```

### 4. Vérifier le déploiement
```bash
kubectl get all -n projet-infonuagique
```

### 5.  Accéder au frontend et au backend (en local avec Minikube)
```bash
minikube service frontend -n projet-infonuagique
minikube service backend -n projet-infonuagique
```

### 6. Pour tester en local avec des images non poussées
```bash
eval $(minikube docker-env)
docker build -t projet-infonuagique-backend ./backend
docker build -t projet-infonuagique-frontend ./frontend
```