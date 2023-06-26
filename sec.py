import boto3
import os

def fetch_secret_from_vault(secret_name, output_file):
    # Fetch AWS credentials from environment variables
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

    # Create a Secrets Manager client using AWS credentials
    session = boto3.session.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    secretsmanager_client = session.client('secretsmanager')

    try:
        # Retrieve the secret value from AWS Secrets Manager
        response = secretsmanager_client.get_secret_value(SecretId=secret_name)

        # Extract the secret value from the response
        secret_value = response['SecretString']

        # Write the secret value to the output file
        with open(output_file, 'w') as f:
            f.write(secret_value)

        # Return success
        return True
    except Exception as e:
        # Handle any errors that occur during secret retrieval
        print(f"Error fetching secret: {e}")
        return False

# Usage example
if __name__ == '__main__':
    secret_name = 'my-secret'  # Name of the secret stored in AWS Secrets Manager
    output_file = '/tmp/my-secret.txt'  # Path to the output file

    if fetch_secret_from_vault(secret_name, output_file):
        print(f"The secret value is fetched and stored in {output_file}")
    else:
        print("Failed to fetch secret")
