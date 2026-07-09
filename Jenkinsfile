pipeline {

agent any


stages {


stage('Unit Test') {

steps {

sh '''
python3 -m pytest test_app.py -v/
'''

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


