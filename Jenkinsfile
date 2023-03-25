#!groovy

pipeline {
    agent any
    stages {
        stage("Run images") {
            steps {
                sh 'docker-compose up -d --build --remove-orphans'
                sh 'docker-compose exec -d api init_models'
            }
        }
    }
}
