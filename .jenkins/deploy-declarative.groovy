def DEFAULT_FABRIC = "1174"
def fabricPerBranch = [
        prod: "4004",
        qa: "4005",
        develop: DEFAULT_FABRIC
]
def get_databricks_host() {
    if ("${env.GIT_BRANCH}" == "prod") {
        return credentials("DEMO_PROD_DATABRICKS_HOST")
    } else {
        return credentials("DEMO_DATABRICKS_HOST")
    }
}
def get_databricks_token() {
    if ("${env.GIT_BRANCH}" == "prod") {
        return credentials("DEMO_PROD_DATABRICKS_TOKEN")
    } else {
        return credentials("DEMO_DATABRICKS_TOKEN")
    }
}

pipeline {
    agent any
    environment {
        //note: credentials call must be made with a non-templated string
        DATABRICKS_HOST = get_databricks_host()
        DATABRICKS_TOKEN = get_databricks_token()
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
            steps {
                sh """
                . ./$VENV_NAME/bin/activate
                python3 -m pbt deploy --fabric-ids $FABRIC_ID --path $PROJECT_PATH
                """
            }
        }
    }
}
