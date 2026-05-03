# Python CI/CD DevOps Project

## Overview

This project demonstrates a complete CI/CD pipeline for a Python Flask application using GitHub Actions and Docker.

---

## Tech Stack

* Python (Flask)
* GitHub Actions (CI/CD)
* Docker
* Docker Hub
* Render (Deployment)

---

## CI/CD Pipeline

```text
Code Push →
Lint (flake8) →
Test (pytest) →
Build Docker Image →
Push to Docker Hub →
Deploy on Render
```

---

## Testing

* Unit tests using pytest
* Endpoint validation
* Negative test cases

---

## Docker

Application is containerized using Docker for consistent deployment.

---

## Live Demo

https://python-cicd-project.onrender.com/

---

## Project Structure

```
app.py → Main Flask app  
test_app.py → Test cases  
Dockerfile → Container config  
ci.yml → CI/CD pipeline  
```

---

## Key Features

* Automated CI/CD pipeline
* Docker-based deployment
* Cloud hosting
* Production-style workflow

---

## Author

Kotala Bhanuchander