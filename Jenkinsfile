pipeline {
    agent any
stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/mazenshouman/sample-project.git'
            }
        }
         stage('Set Up Python Environment') {
            steps {
                script {
                    // Create and activate virtual environment
                    bash 'python3 -m venv venv'
                    bash 'source venv/bin/activate'
                    // Install pytest and other dependencies
                    bash 'venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    bash "pwd"
                    bash "ls"
                    dockerImage = docker.build("mazenshouman/sample-app:latest")
                }
            }
        }
        stage('Run Test') {
            steps {
                script {
                    // Activate the virtual environment and run pytest
                    bash 'source venv/bin/activate && venv/bin/pytest app.py'
                }
            }
        }
    }
}