/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr: '5')
        disableConcurrentBuilds()
    }
    stages {
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

