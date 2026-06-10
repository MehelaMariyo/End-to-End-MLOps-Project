# End-to-End-MLOps-Project

    - Gonna use US Visa Approval classifation model building in this project.
    - Use CI/CD techniques
    - Impliment Docker for portibility
    - Use AWS for hosting

## How to run?

'''bash

    conda create -n visa python=3.8 -y

'''

'''bash

    conda activate visa

'''
'''bash

    conda install -r requirements.txt

'''

## workflow:

    1. constants
    2. entity
    3. components
    4. pipeline
    5. main file

### Export the environment variable

'''bash

    export MONGODB_URL=""

    export AWS_ACCESS_KEY_ID=""

    export AWS_SECRET_ACCESS_KEY=""
    
'''    

## AWS-CICD-Deployment-with-Github-Action

### with specific access

1. EC2 access : It is virtual machine
2. ECR: Elastic Container registry to save the docker image in aws

### Description: About the deployment

1. Build docker image of the source code
2. Push the docker image to ECR
3. Launch the EC2 
4. Pull the image from ECR in EC2
5. Lauch the docker image in EC2

### Policy:

1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess
3. AmazonS3FullAccess

## 3. Create ECR repo to store/save docker image

- Save the URI: 218852528806.dkr.ecr.us-east-1.amazonaws.com/visa

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

### optinal

sudo apt-get update -y
sudo apt-get upgrade

### required

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

## 6. Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one

## 7. Setup github secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO









    