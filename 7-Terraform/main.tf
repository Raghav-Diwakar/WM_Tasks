provider "aws" {
  region = "eu-west-1"
}

locals {
  name = "Key"

  tags = {
    Example    = local.name
  }
}

################################################################################
# Variables
################################################################################

variable "create" {
  type        = bool
  default     = true
}

variable "create_private_key" {
  type        = bool
  default     = true
}

variable "key_name" {
  type        = string
  default     = null
}

variable "key_name_prefix" {
  type        = string
  default     = null
}

variable "public_key" {
  type        = string
  default     = ""
}

variable "private_key_algorithm" {
  type        = string
  default     = "RSA"
}

variable "private_key_rsa_bits" {
  type        = number
  default     = 4096
}

variable "tags" {
  type        = map(string)
  default     = {}
}

################################################################################
# Generate Private Key (optional)
################################################################################

resource "tls_private_key" "this" {
  count     = var.create && var.create_private_key ? 1 : 0
  algorithm = var.private_key_algorithm
  rsa_bits  = var.private_key_rsa_bits
}

################################################################################
# Create AWS Key Pair
################################################################################

resource "aws_key_pair" "this"  {
  count = var.create ? 1 : 0

  key_name        = var.key_name != null ? var.key_name : local.name
  key_name_prefix = var.key_name == null ? var.key_name_prefix : null
  public_key      = var.create_private_key ? trimspace(tls_private_key.this[0].public_key_openssh) : var.public_key
  tags            = local.tags
}

resource "aws_instance" "Ubuntu" {
  ami                    = "ami-0df368112825f8d8f"  # Replace with a valid AMI ID
  instance_type          = "t2.micro"                # Default instance type (Eligible for the AWS Free Tier)
  key_name               = aws_key_pair.this[0].key_name  # Use the key pair created
  tags                   = local.tags

  # Default security group and default VPC (no need to define explicitly)
  associate_public_ip_address = true  # Automatically associate a public IP address with the instance

  # Optional: Enabling User Data to initialize the instance on first boot
#   user_data = <<-EOF
#               #!/bin/bash
#               echo "Hello, World!" > /var/www/html/index.html
#               EOF
}

################################################################################
# Outputs
################################################################################

output "key_pair_id" {
  value       = try(aws_key_pair.this[0].key_pair_id, "")
  description = "AWS Key Pair ID"
}

output "key_pair_name" {
  value       = try(aws_key_pair.this[0].key_name, "")
  description = "AWS Key Pair Name"
}

output "key_pair_arn" {
  value       = try(aws_key_pair.this[0].arn, "")
  description = "AWS Key Pair ARN"
}

output "key_pair_fingerprint" {
  value       = try(aws_key_pair.this[0].fingerprint, "")
  description = "Public key MD5 fingerprint"
}

output "private_key_pem" {
  value       = try(trimspace(tls_private_key.this[0].private_key_pem), "")
  description = "Private key (PEM format)"
  sensitive   = true
}

output "private_key_openssh" {
  value       = try(trimspace(tls_private_key.this[0].private_key_openssh), "")
  description = "Private key (OpenSSH format)"
  sensitive   = true
}

output "public_key_openssh" {
  value       = try(trimspace(tls_private_key.this[0].public_key_openssh), "")
  description = "Public key (OpenSSH format)"
}

output "public_key_pem" {
  value       = try(trimspace(tls_private_key.this[0].public_key_pem), "")
  description = "Public key (PEM format)"
}

output "public_key_fingerprint_md5" {
  value       = try(tls_private_key.this[0].public_key_fingerprint_md5, "")
  description = "Public key fingerprint (MD5)"
}

output "public_key_fingerprint_sha256" {
  value       = try(tls_private_key.this[0].public_key_fingerprint_sha256, "")
  description = "Public key fingerprint (SHA256)"
}
