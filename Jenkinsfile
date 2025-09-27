pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello DevOps Engineer 🚀" > report.txt'
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
        stage('Deploy') {
            steps {
                sh 'mkdir -p deploy'
                sh 'cp report.txt deploy/'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                sh 'cat deploy/report.txt'
            }
        }
    }
    post {
        success {
            echo 'Pipeline ran successfully ✅'
            // Slack notification (plugin & credentials required)
            // slackSend channel: '#devops', message: "Build Success ✅"
            // Email notification (plugin & credentials required)
            // mail to: 'ajay@example.com', subject: 'Build Success', body: 'Pipeline ran successfully ✅'
        }
        failure {
            echo 'Pipeline failed ❌'
            // Slack notification example
            // slackSend channel: '#devops', message: "Build Failed ❌"
            // Email notification example
            // mail to: 'ajay@example.com', subject: 'Build Failed', body: 'Pipeline failed ❌'
        }
    }
}

