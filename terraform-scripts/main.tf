terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.14.0"
    }
    azuredevops = {
      source  = "microsoft/azuredevops"
      version = "~> 0.10.0"
    }
  }
  required_version = ">= 1.0.0"
}

provider "azurerm" {
  features {}
}

provider "azuredevops" {
  org_service_url = "https://dev.azure.com/timtampouris"
  personal_access_token = var.pat
}

resource "azuredevops_project" "sample-project" {
  name               = "Sample-Project"
  visibility         = "private"
  version_control    = "Git"
  work_item_template = "Agile"
}
