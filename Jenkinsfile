pipeline {
 
    agent any
 
    environment {
        HEADLESS = 'true'
    }
 
    stages {
 
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
 
        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                '''
            }
        }
 
        stage('Install Dependencies') {
            steps {
                sh '''
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }
 
        stage('Install Playwright Browser') {
            steps {
                sh '''
                    .venv/bin/playwright install chromium
                '''
            }
        }
 
        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p reports
                    .venv/bin/pytest \
                        --junitxml=reports/junit.xml
                '''
            }
        }
    }
 
    post {
 
        always {
            junit 'reports/junit.xml'
 
            archiveArtifacts artifacts: 'reports/**/*',
                             allowEmptyArchive: true
        }
 
        success {
            echo 'Playwright tests completed successfully.'
        }
 
        failure {
            echo 'Playwright tests failed. Check the test results and artifacts.'
        }
    }
}