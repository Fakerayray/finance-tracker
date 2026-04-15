pipeline {
    agent any
    
    stages {
        stage('Build Image') {
            steps {
                // Removed 'sudo'
                sh 'docker compose build backend'
            }
        }
        
        stage('Security Scan') {
            steps {
                // Removed 'sudo'
                sh 'trivy image --severity HIGH,CRITICAL finance-tracker-backend'
            }
        }
        
        stage('Deploy') {
            steps {
                // Removed 'sudo'
                sh 'docker compose up -d'
            }
        }
    }
}
