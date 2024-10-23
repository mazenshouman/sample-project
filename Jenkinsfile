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
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}