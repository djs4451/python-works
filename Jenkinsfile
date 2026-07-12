pipeline {

    agent any

    stages {

        stage('Unit Test') {

            steps {

                sh '''
                pytest test_app.py -v
                '''
            }
        }

        stage('Build Artifact') {

            steps {

                sh '''
                tar -czf python-app.tar.gz app.py
                '''
            }
        }

        stage('Archive Artifact') {

            steps {

                archiveArtifacts artifacts: 'python-app.tar.gz'
            }
        }

        stage('Deploy') {

            steps {

                sh '''
                ssh root@192.168.74.147 \
                "ansible-playbook /python-works/ansible/deploy.yml"
                '''
            }
        }
    }
}
