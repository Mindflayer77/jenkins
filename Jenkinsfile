/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr: '5')
        disableConcurretBuilds()
    }
    stages {
        stage('Hello') { 
    
            steps {
                echo "hello"
            }
        }
    }
}

