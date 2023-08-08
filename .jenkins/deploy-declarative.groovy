def DEFAULT_FABRIC = "1174"
def fabricPerBranch = [
        prod: "2807",
        qa: "1400",
        develop: DEFAULT_FABRIC
]

pipeline {
    agent any
    environment {
        DATABRICKS_HOST = credentials('DEMO_DATABRICKS_HOST')
        DATABRICKS_TOKEN = credentials('DEMO_DATABRICKS_TOKEN')
        PROJECT_PATH = "./hello_project"
        VENV_NAME = ".venv"
        FABRIC_ID = fabricPerBranch.getOrDefault('${env.BRANCH_NAME}', DEFAULT_FABRIC)
    }
    stages {
        stage('checkout') {
            steps {
                git branch: '${env.BRANCH_NAME}', credentialsId: 'jenkins-cicd-runner-demo', url: 'git@github.com:SimpleDataLabsInc/HelloCICD.git'
                sh "apt-get install -y python3-venv"
            }
        }
        stage('install pbt') {
            steps {
                sh """#!/bin/bash -xe
                python3 --version
                if [[ ! -d "$VENV_NAME" ]]; then
                    python3 -m venv $VENV_NAME
                fi
                source ./$VENV_NAME/bin/activate
                python3 -m pip install -U pip 
                python3 -m pip install -U build pytest wheel pytest-html pyspark prophecy-build-tool
                """
            }
        }
        stage('deploy') {
            steps {
                sh """
                . ./$VENV_NAME/bin/activate
                python3 -m pbt deploy --fabric-ids $FABRIC_ID --path $PROJECT_PATH
                """
            }
        }
    }
}
