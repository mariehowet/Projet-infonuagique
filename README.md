#  Déploiement Full Stack Vue/React + FastAPI + PostgreSQL avec Docker Swarm & Kubernetes

Ce projet regroupe un frontend mixte Vite.js + React servi par NGINX, un backend FastAPI, et une base de données PostgreSQL. Deux méthodes de déploiement sont disponibles :

- 🐳 **Docker Swarm**
- ☸️ **Kubernetes**


## Prérequis

- Docker (`docker start`)
- Kubernetes (Minikube, Kind, etc.)
- `kubectl` installé et configuré (command-line de K8s)
- Images Docker buildées et poussées dans un registre (Docker Hub, GHCR, etc.) ou accessible en local

### Construire et pousser les images

```bash
# Backend FastAPI
docker build -t dockermariexmas/projet-infonuagique-backend:latest ./backend
docker push dockermariexmas/projet-infonuagique-backend:latest

# Frontend NGINX avec Vue + React
docker build -t dockermariexmas/projet-infonuagique-frontend:latest ./frontend
docker push dockermariexmas/projet-infonuagique-frontend:latest
```

##  Déploiement Docker Swarm

### 1. Démarrer Docker Swarm

```bash
docker swarm init
```

### 2. Déployer la stack
```bash
docker stack deploy -c docker-compose.swarm.yml mon_projet_stack
```
### 3. Vérifier le déploiement
```bash
docker stack services mon_projet_stack
docker stack ps mon_projet_stack
```

##  Déploiement Kubernetes
### Prérequis
```bash
#Installer Prometheus + Grafana + CDRs
helm install prometheus prometheus-community/kube-prometheus-stack --namespace projet-infonuagique
```
### 1. Démarrer Minikube (si local)
```bash
minikube start
# To enable dashboard features addon
minikube addons enable metrics-server
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


### 6. Observer les métriques


#### Lancer Prometheus & Grafana
 ```bash
#kubectl expose service prometheus-operated --type=NodePort --target-port=9090 --port=9090 --name=prometheus-operated-ext -n projet-infonuagique
minikube service prometheus-grafana -n projet-infonuagique
```

#### Grafana
```bash
#kubectl expose service prometheus-grafana --type=NodePort --target-port=3000 --name=prometheus-grafana-ext -n projet-infonuagique

#Récupérer le mot de passe. Utilisateur par défaut:admin.
kubectl get secret prometheus-grafana --namespace projet-infonuagique -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

#### Lancer le dashboard Kubernetes
```bash
minikube dashboard
```