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
                sh 'docker compose stop db vault backend frontend nginx || true'
		sh 'docker compose rm -f db vault backend frontend nginx || true'
                sh 'sudo fuser -k 80/tcp || true'
                // Explicitly list your app services to avoid restarting Jenkins
                sh 'docker compose up -d db vault backend frontend nginx'
            }
        }
    }
}
