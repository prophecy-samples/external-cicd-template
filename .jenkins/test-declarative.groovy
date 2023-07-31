pipeline {
    agent any
    environment {
        DATABRICKS_HOST = credentials('DATABRICKS_HOST')
        DATABRICKS_TOKEN = credentials('DATABRICKS_TOKEN')
        PROJECT_PATH = "./hello_project"
        VENV_NAME = ".venv"
    }
    stages {
        stage('checkout') {
            steps {
                git branch: '${sha1}', credentialsId: 'github-hello-cicd-deploy-ssh', url: 'git@github.com:SimpleDataLabsInc/HelloCICD.git'
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
        stage('validate') {
            steps {
                sh """
                . ./$VENV_NAME/bin/activate
                python3 -m pbt validate --path $PROJECT_PATH
                """
            }
        }
        stage('test') {
            steps {
                sh """
                . ./$VENV_NAME/bin/activate
                python3 -m pbt test --path $PROJECT_PATH
                """
            }
        }
    }
}
