pipeline {
 
    agent any
 
    stages {
 
        stage('Verify Environment') {

            steps {

                sh '''

                    echo "Python:"

                    python3.11 --version
 
                    echo "Git:"

                    git --version
 
                    echo "Jenkins user:"

                    whoami

                '''

            }

        }
 
        stage('Setup Python') {

            steps {

                sh '''

                    rm -rf .venv
 
                    python3.11 -m venv .venv
 
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

                        -v \

                        --junitxml=reports/junit.xml

                '''

            }

        }

    }
 
    post {
 
        always {

            junit(

                testResults: 'reports/junit.xml',

                allowEmptyResults: true

            )

        }
 
        success {

            echo 'Playwright tests completed successfully.'

        }
 
        failure {

            echo 'Playwright tests failed.'

        }

    }

}
 