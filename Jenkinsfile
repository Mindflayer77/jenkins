/* Requires the Docker Pipeline plugin */
pipeline {
    agent  { docker { image 'python:3.10.7-alpine' } }
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr: '5')
        disableConcurrentBuilds()
    }
    stages {
        stage ('Verify tools'){
            steps{
                sh "python --version"
            }
        }
        stage('Build') { 
    
            steps {
                sh "python main.py car.py"
            }
        }
        stage ('Test'){
            // when {
            //     branch "work*"
            // }
            steps{
                sh "python -m unittest tests.py"
            }
        } 
    }
}

