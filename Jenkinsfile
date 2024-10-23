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
        // stage('Run Test') {
        //     steps {
        //         script {
        //             sh """
        //             docker run --name math_flask --rm mazenshouman/sample-app:latest pytest ./app/test_app.py
        //             """
        //         }
        //     }
        // }
    }
}