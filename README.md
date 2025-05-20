# Secrets for UC4

## Overview
This repository stores sensitive data for GLACIATION Use Case 4 by IPTO. 
Sensitive data is securely encrypted with the use of [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets). 

The core idea is to manually manage human-readable secret templates and secret values in `.env`. 
This repo provides a tool to convert these manually managed artifacts to Sealed Secrets files that you can commit to Git
and reuse in GitOps processes.    

## How to Set Up

Follow these steps to set up the project:

1. **Clone the Repository**  
   Clone the repository to your local environment:
    ```shell script
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Install Dependencies**  
   Make sure you have the required tools installed:
   - [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) for managing Kubernetes resources.
   - [kubeseal](https://github.com/bitnami-labs/sealed-secrets#kubeseal) CLI for encrypting secrets.

3. **Access Kubernetes Cluster**  
   Ensure you have access to the target cluster:
   - Set up your kubeconfig file to point to the Integration environment.
   - You can verify access by running:
    ```shell script
    kubectl get nodes
    ```

4. **Verify the Sealed Secrets Controller**  
   Confirm that the Sealed Secrets controller is installed and running in the Kubernetes cluster:
    ```shell script
    kubectl get pods -A | grep sealed-secrets
    ```


## How to Use

### Encrypt a Secret

1. Create your `.env` file from `example.env`. Do not commit your secrets to Git!

2. Create a template file for your secret. 
Use [uc4-minio-configuration.yaml](secrets/templates/uc4-minio-configuration.yaml) as example.

3. Generate sealed secret
    ```
   ./scripts/seal.sh secrets/templates/example-secret.yaml
   ```
   Now the new sealed secret file is created in `secrets/sealed`.

4. Now you can deliver the secret to the cluster
   ```aiignore
   kubectl apply -f secrets/templates/example-secret.yaml
   ```