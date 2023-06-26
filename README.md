This repository contains a Python script that can be used as an init container in Kubernetes to fetch secrets from AWS Secrets Manager. The script utilizes the AWS SDK (boto3) and the AWS CLI configuration to authenticate with AWS Secrets Manager and retrieve the secret value. 

To use the script, ensure that you have the AWS CLI installed and configured with the appropriate AWS credentials. Additionally, Python 3 and the required dependencies (boto3) should be installed on your system. 

Clone this repository to your local machine or server and install the necessary dependencies using pip. Configure your AWS credentials using the AWS CLI and update the secret name and output file variables in the fetch_secrets.py script. Then, run the script to fetch the secret value from AWS Secrets Manager and store it in the specified output file.
