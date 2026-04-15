pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YourUsername/finance-tracker.git'
            }
        }
        stage('Security Scan') {
            steps {
                // This runs the Trivy we installed earlier
                sh 'trivy image --severity HIGH,CRITICAL finance-tracker-backend'
            }
        }
        stage('Build & Deploy') {
            steps {
                sh 'sudo docker compose up --build -d'
            }
        }
    }
}
