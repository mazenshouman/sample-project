Step 1: Create a Sample Flask Project
Project Structure
First, we’ll create a simple Flask web application. Here’s the structure of our project:

sample-project/
├── app/
│   ├── app.py
├── Jenkinsfile
├── requirements.txt
├── Dockerfile
└── README.md

app/app.py
This is the main application file for our Flask app.

requirements.txt
List of dependencies for our Flask app.

makefile
Flask==2.0.3

app/Dockerfile
Dockerfile to containerize our Flask application.

Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

Jenkinsfile
Jenkins pipeline configuration.

pipeline {
    agent any
stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/mazenshouman/sample-project.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("mazenshouman/sample-app:latest")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    sh """
                    docker run --name math_flask --rm mazenshouman/sample-app:latest
                    """
                }
            }
        }
    }
}


Step 2: Configure Jenkins
Install Plugins
Ensure you have the following Jenkins plugins installed:

Docker Pipeline
Create a New Pipeline Job


Step 3: Run the Pipeline
