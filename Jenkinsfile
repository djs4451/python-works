pipeline {

agent any


stages {



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


