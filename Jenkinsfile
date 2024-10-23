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
                    docker run --name math_flask -p 5000:5000 --rm mazenshouman/sample-app:latest
                    """
                }
            }
        }
    }
}