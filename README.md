# Simple Python Flask app

## Setup

```bash
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
cd backend
python app.py
```

## Docker

```bash
docker build --tag d2s-learn .
docker run -d -p 5000:5000 d2s-learn
```

## Deploy on Minikube

```bash
minikube start
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service d2s-learn-svc
```

## Clean up

```bash
kubectl delete service d2s-learn-svc
kubectl delete deployment d2s-learn
minikube stop
minikube delete
```

## Common Errors

```bash
# Run PowerShell as admin
docker context use default
```