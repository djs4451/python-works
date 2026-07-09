pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/djs4451/python-works.git'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'python3 -m pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                ssh ansible@ansible-controller \
                "ansible-playbook \
                /python-works/ansible/deploy.yml"
                '''
            }
        }
    }
}
