pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Set the working directory to the root directory of the gpt_review package
                dir('path/to/gpt_review') {
                    // Install the Python package
                    bat 'pip install .'
                }
            }
        }
        stage('Run Script') {
            steps {
                script {
                    // Get the list of modified files in the pull request
                    def modifiedFiles = sh(returnStdout: true, script: 'git diff --name-only origin/master...HEAD').trim().split('\\r?\\n')

                    // Initialize an empty response variable
                    def aggregatedResponse = ""

                    // Iterate over each modified file
                    for (def file in modifiedFiles) {
                        // Run the custom Python script for each file
                        def response = bat(returnStdout: true, script: 'gpt_review -a "api_key.txt" -i "' + file + '"')
                        aggregatedResponse += "Response for ${file}:\n${response}\n\n"
                    }

                    // Print the aggregated response
                    println(aggregatedResponse)

                    // Save the aggregated response to a file or perform additional actions as needed
                    // For example, you can save the response to a text file and archive it as a build artifact
                    writeFile file: 'aggregated_response.txt', text: aggregatedResponse
                    archiveArtifacts 'aggregated_response.txt'
                }
            }
        }
    }

    post {
        success {
            // Additional actions to perform on successful build
        }
        failure {
            // Additional actions to perform on failed build
        }
    }
}
