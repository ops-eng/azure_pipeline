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
~/myagent$ tar zxvf ~/Downloads/vsts-agent-osx-x64-4.248.0.tar.gz
```

## Configure the agentDetailed instructions
```bash
~/myagent$ ./config.sh
```

Enter Server URL:
Azure Pipelines: https://dev.azure.com/timtampouris

## Run the agent interactively
```bash
~/myagent$ ./run.sh
```


# Steps to Set Up the Pipeline

## Create a new repository in Azure DevOps.

Push the azure-pipeline/ folder to your repository.

```bash
git init
git remote add origin https://timtampouris@dev.azure.com/timtampouris/cicdassessment/_git/cicdassessment
git push -u origin --all
git add .
git commit -m "Initial commit"
git push -u origin main
```

Go to Azure DevOps → Pipelines → Create Pipeline.

Select the repository and the azure-pipelines.yml file.

Run the pipeline.
