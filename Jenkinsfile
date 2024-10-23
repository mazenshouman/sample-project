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
                    sh "pwd"
                    sh "ls"
                    dockerImage = docker.build("mazenshouman/sample-app:latest")
                }
            }
        }
        stage('Run Test') {
            steps {
                script {
                    sh "pytest app.py"
                }
            }
        }
    }
}