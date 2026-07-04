# 🚀 DevOps Flask CI/CD Pipeline

A production-style DevOps project demonstrating the complete Software Development Life Cycle (SDLC) from application development to Continuous Integration (CI), containerization, orchestration, Infrastructure as Code (IaC), and cloud deployment.

This project is being built step by step to simulate a real-world DevOps workflow using modern tools and best practices.

## 📌 Project Objective

The goal of this project is to learn and implement a complete CI/CD pipeline while understanding each stage in depth.

The project covers:

* Python Flask Application
* Unit Testing with Pytest
* Docker
* Docker Compose
* Git & GitHub
* GitHub Actions (CI)
* Docker Hub
* Kubernetes
* Helm
* Terraform
* AWS
* Monitoring with Prometheus & Grafana

---

# 🏗️ Project Architecture


                    Developer
                        │
                        ▼
                 GitHub Repository
                        │
                        ▼
                GitHub Actions (CI)
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
    Run Tests      Build Docker     Security Scan
                        │
                        ▼
                 Docker Hub Registry
                        │
                        ▼
                Kubernetes Cluster
                        │
                        ▼
                     Helm Chart
                        │
                        ▼
                 Flask Application
                        │
                        ▼
            Prometheus + Grafana



# 🛠️ Tech Stack

| Category                | Technology                           |
| ----------------------- | ------------------------------------ |
| Language                | Python 3.10                          |
| Framework               | Flask                                |
| Testing                 | Pytest                               |
| Containerization        | Docker                               |
| Container Orchestration | Docker Compose                       |
| Version Control         | Git                                  |
| Source Repository       | GitHub                               |
| CI/CD                   | GitHub Actions *(Coming Soon)*       |
| Container Registry      | Docker Hub *(Coming Soon)*           |
| Kubernetes              | Kubernetes *(Coming Soon)*           |
| Package Manager         | Helm *(Coming Soon)*                 |
| Infrastructure as Code  | Terraform *(Coming Soon)*            |
| Cloud                   | AWS *(Coming Soon)*                  |
| Monitoring              | Prometheus & Grafana *(Coming Soon)* |


# 📁 Project Structure

devops-flask-cicd-pipeline/
│
├── app/
│   ├── __init__.py
│   └── app.py
│
├── tests/
│   └── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
├── README.md
│
├── docs/
├── helm/
├── kubernetes/
├── terraform/
└── .github/
    └── workflows/

# ✨ Features Implemented

* Flask REST API
* Health endpoint
* Readiness endpoint
* Version endpoint
* Custom 404 response
* Structured logging
* Environment variable support
* Unit testing with Pytest
* Docker image creation
* Docker Compose support


# 🌐 Available Endpoints

| Endpoint   | Description             |
| ---------- | ----------------------- |
| `/`        | Application information |
| `/health`  | Health check            |
| `/ready`   | Readiness check         |
| `/version` | Application version     |


# ⚙️ Local Setup

### 1. Clone the repository


git clone <repository-url>
cd devops-flask-cicd-pipeline

### 2. Create a virtual environment

python -m venv venv


### 3. Activate the virtual environment

**Windows**

venv\Scripts\activate

**Linux/macOS**

source venv/bin/activate


### 4. Install dependencies


pip install -r requirements.txt


### 5. Run the application

python app/app.py


Application URL:

http://localhost:5000


# 🧪 Run Unit Tests


pytest

Expected output:

5 passed

# 🐳 Docker

Build the image:


docker build -t flask-cicd-app:v1 .

Run the container:

docker run -d --name flask-app -p 5000:5000 flask-cicd-app:v1

View logs:

docker logs flask-app

# 🐳 Docker Compose

Start the application:

docker compose up -d

View logs:

docker compose logs -f

Stop the application:

docker compose down

# 📚 Key DevOps Concepts Demonstrated

* Version Control
* Unit Testing
* Containerization
* Container Orchestration
* Environment Variables
* Logging
* CI/CD Fundamentals
* Infrastructure as Code (Upcoming)
* Cloud Deployment (Upcoming)

---

# 👨‍💻 Author

**Kartik Agrawal**

This repository is part of my DevOps learning journey, where I am building a complete end-to-end CI/CD pipeline using industry-standard tools and best practices.

---

# ⭐ Future Enhancements

* GitHub Actions CI Pipeline
* Docker Hub Integration
* Kubernetes Deployment
* Helm Charts
* Terraform Automation
* AWS Deployment
* Prometheus Metrics
* Grafana Dashboards
* Trivy Security Scanning
* SonarQube Code Analysis
