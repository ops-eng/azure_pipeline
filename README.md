# Commands to Run

## Initialize Terraform:

```bash
terraform init
```

## Validate configuration:

```bash
terraform validate
```

## Generate a plan:

```bash
terraform plan
```

## Apply the changes:

```bash
terraform apply
```

# Install a local agent for private repos

## Create the agent
```bash
~/$ mkdir myagent && cd myagent
~/myagent$ tar zxvf ~/downloads/vsts-agent-osx-x64-V.vvv.v.tar.gz
```

## Configure the agentDetailed instructions
```bash
~/myagent$ ./config.sh
```

## Run the agent interactively
```bash
~/myagent$ ./run.sh
```

# Steps to Set Up the Pipeline

## Create a new repository in Azure DevOps.

Push the azure-pipeline/ folder to your repository.

```bash
git init
git remote add origin https://\<your-organization\>@dev.azure.com/\<your-organization\>/cicdassessment/_git/cicdassessment
git push -u origin --all
git add .
git commit -m "Initial commit"
git push -u origin main
```

Go to Azure DevOps → Pipelines → Create Pipeline.

Select the repository and the azure-pipelines.yml file.

Run the pipeline.

# Function for Approval process

You need to create a Function app and a http-trigger.

The function_app.py script will simulate a random deployment approval check. Returns a decision ("Approved" or "Not Approved") as the response.
