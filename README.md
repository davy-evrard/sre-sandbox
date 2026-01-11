# 🛠️ SRE & Platform Engineering Sandbox

**A comprehensive project demonstrating the full lifecycle of a modern application—from code and containerization to orchestration, observability, and automated CI/CD.**

## 📖 Overview
This project simulates a real-world microservice environment to practice. 

Instead of a perfect "Hello World" app, this repository contains **"The Unstable API"**—a Python service designed to fail randomly. The goal of the project is not just to run the app, but to **monitor it, break it, and fix it** using industry-standard SRE tools.

### Key Concepts Demonstrated:
* **SLIs & SLOs:** Measuring Service Level Indicators and visualizing Objectives.
* **Telemetry:** Instrumenting a Python API to expose Prometheus metrics.
* **Infrastructure as Code:** Using Docker Compose/k8s/terraform to spin up a full monitoring stack.
* **Chaos Engineering:** Using load testing scripts to intentionally trigger SLO breaches.

## 🛠 Tech Stack
* **Application:** Python (FastAPI)
* **Containerization:** Docker & Docker Compose
* **Metric Storage:** Prometheus
* **Visualization:** Grafana
* **Scripting:** Python (`requests` for load testing)


## 🏗️ Project Architecture
This repository is organized into distinct modules, each representing a core SRE pillar:

* **`/app`**: FastAPI application instrumented with Prometheus metrics and unit tests.
* **`/monitoring`**: Observability stack using **Prometheus** (metrics collection) and **Grafana** (dashboards).
* **`/k8s`**: Kubernetes manifests for high-availability deployments and self-healing.
* **`/terraform`**: Infrastructure as Code (IaC) for automated configuration management.
* **`.github/workflows`**: Automated CI/CD pipeline for testing and quality gates.

---

## 🚀 Getting Started (Docker Compose)
The easiest way to see the entire stack in action is using Docker Compose:

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sre-sandbox.git](https://github.com/YOUR_USERNAME/sre-sandbox.git)
   cd sre-sandbox

2. **Launch the stack:**
    docker-compose up --build

3. **Access the endpoints:**
    - API: http://localhost:8000
    - Prometheus: http://localhost:9090
    - Grafana: http://localhost:3000


## 📊 Observability & Reliability
One of the primary goals of this project was to visualize SLOs (Service Level Objectives). Below is a real-world trace of a reliability breach and subsequent recovery:
    - Green Line: Successful Request Rate.
    - The Incident: A simulated 20% failure rate was introduced via a load test.
    - The Recovery: Automated self-healing and manual patching restored the service to 100% reliability.
![alt text](image.png)

## 🧪 The Experiment (Chaos Mode)
The repository includes a load testing script to simulate a traffic spike and trigger latent bugs.

1. **Start the Load Test:**
    ```bash
    python load_test.py

This script hits the /risky endpoint, which has a 20% chance of throwing a 500 error.

2. **Observe the SLO Breach:**
Go to Grafana and watch the "Success Rate" drop below the 90% threshold.

![alt text](image.png)

3. **Fix the Issue:**
Update main.py to patch the random failure, rebuild the container, and watch the graph recover to 100%.

## 🤖 CI/CD Pipeline
Every change pushed to this repository is automatically validated via GitHub Actions. The pipeline performs the following:
    - Sets up a clean Python environment.
    - Installs production and testing dependencies.
    - Runs a suite of pytest unit tests to ensure no regressions.

## ☸️ Kubernetes & Self-Healing
For production-grade orchestration, this project includes Kubernetes manifests.
    - Deployments: Manages 3 replicas of the app for high availability.
    - Services: Provides a stable entry point and load balancing.
    - Self-Healing: Demonstrated by deleting a pod and watching Kubernetes immediately spin up a replacement to maintain the desired state.

    # Apply to your cluster (e.g., Minikube)
    ```bash
    kubectl apply -f k8s/