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

        stage('Build Image Inside Minikube') {
            steps {
                sh '''
                  minikube image build -t devops-app:latest .
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

    post {
        success {
            echo "✅ Jenkins CI/CD pipeline completed successfully"
        }
        failure {
            echo "❌ Jenkins CI/CD pipeline failed"
        }
    }
}

