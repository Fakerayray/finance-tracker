pipeline {
    agent any
    
    stages {
        
        stage('Build Image') {
            steps {
                // Building the image first so Trivy has something to scan
                sh 'sudo docker compose build backend'
            }
        }
        
        stage('Security Scan') {
            steps {
                // Running the Trivy scan on the image we just built
                sh 'trivy image --severity HIGH,CRITICAL finance-tracker-backend'
            }
        }
        
        stage('Deploy') {
            steps {
                // Launching the full stack
                sh 'sudo docker compose up -d'
            }
        }
    }
}
