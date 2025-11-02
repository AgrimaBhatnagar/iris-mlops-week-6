# IRIS MLOps - Week 6 (CD to GKE)

## Objective
Continuous Deployment of an IRIS FastAPI service to Google Kubernetes Engine using GitHub Actions and Google Artifact Registry.

## Flow
- GitHub Actions builds Docker image from `api/Dockerfile`
- Pushes image to Artifact Registry
- Applies `k8s/` manifests to GKE (namespace `iris`)
- Service exposed via LoadBalancer; `/health` returns `{"status": "ok"}`

## Pod vs Container (screencast)
- **Container**: single runnable unit (image + one process).
- **Pod**: smallest deployable K8s unit; can hold 1+ containers sharing IP/volumes. K8s schedules pods, not containers.
