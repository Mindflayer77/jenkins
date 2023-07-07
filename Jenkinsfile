/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr: '5')
        disableConcurrentBuilds()
    }
    stages {
        stage('Hello') { 
    
            steps {
                echo "hello"
            }
        stage ('cat README'){
            when {
                branch "work*"
            }
            steps{
                sh '''
                    cat README.md
                    '''
            }
        }
        }
    }
}

