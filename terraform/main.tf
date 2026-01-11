terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
      version = "2.4.0"
    }
  }
}

provider "local" {}

# 1. Define the content of the file using a Terraform variable logic
resource "local_file" "app_config" {
  filename = "${path.module}/sre-config.json"
  content  = jsonencode({
    "app_name": "SRE Sandbox",
    "version": "1.0.0",
    "maintenance_mode": false,
    "max_retries": 5,
    "database": {
      "host": "localhost",
      "port": 5432
    }
  })
}