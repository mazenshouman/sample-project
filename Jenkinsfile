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
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    // Install pytest and other dependencies
                    sh 'venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "pwd"
                    sh "ls"
                    dockerImage = docker.build("mazenshouman/sample-app:latest")
                }
            }
        }
        stage('Run Test') {
            steps {
                script {
                    // Activate the virtual environment and run pytest
                    sh 'source venv/bin/activate && venv/bin/pytest app.py'
                }
            }
        }
    }
}