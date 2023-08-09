def DEFAULT_FABRIC = "1174"
def fabricPerBranch = [
        prod: "4004",
        qa: "4005",
        develop: DEFAULT_FABRIC
]

pipeline {
    agent any
    environment {
        //note: credentials call must be made with a non-templated string which is why we have to get prod/nonprod
        // here before assigning to our actual env var
        DATABRICKS_HOST_PROD = credentials("DEMO_PROD_DATABRICKS_HOST")
        DATABRICKS_TOKEN_PROD = credentials("DEMO_PROD_DATABRICKS_TOKEN")
        DATABRICKS_HOST_NONPROD  = credentials("DEMO_DATABRICKS_HOST")
        DATABRICKS_TOKEN_NONPROD = credentials("DEMO_DATABRICKS_TOKEN")
        DATABRICKS_HOST = ("${env.GIT_BRANCH}" == "prod") ? DATABRICKS_HOST_PROD : DATABRICKS_HOST_NONPROD
        DATABRICKS_TOKEN = ("${env.GIT_BRANCH}" == "prod") ? DATABRICKS_TOKEN_PROD : DATABRICKS_TOKEN_NONPROD

        PROJECT_PATH = "./hello_project"
        VENV_NAME = ".venv"
        FABRIC_ID = fabricPerBranch.getOrDefault("${env.GIT_BRANCH}", DEFAULT_FABRIC)
    }
    stages {
        stage('prepare system') {
            steps {
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
            environment {
                //note: credentials call must be made with a non-templated string
                DATABRICKS_HOST = credentials("${DATABRICKS_HOST_CRED_STRING}")
                DATABRICKS_TOKEN = credentials("${DATABRICKS_TOKEN_CRED_STRING}")
            }
            steps {
                sh """
                . ./$VENV_NAME/bin/activate
                python3 -m pbt deploy --fabric-ids $FABRIC_ID --path $PROJECT_PATH
                """
            }
        }
    }
}
