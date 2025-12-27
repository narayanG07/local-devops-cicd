pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-app:latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image (Minikube)') {
            steps {
                sh '''
                  eval $(minikube docker-env)
                  DOCKER_BUILDKIT=0 docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                  kubectl apply -f k8s/
                  kubectl rollout status deployment/devops-app
                '''
            }
        }
    }
}
