### VPC Setup with Public and Private Subnets and Instance Deployment
Create a VPC with three public and three private subnets distributed across different availability zones. Launch three EC2 instances in each subnet to validate network segmentation and availability.

### VPC Setup with Public and Private Subnets and Instance Deployment (Using a NAT Instance Instead of a NAT Gateway)
Set up a VPC with public and private subnets across multiple availability zones. Deploy a NAT instance in the public subnet to provide internet access for private subnet instances. Launch three EC2 instances in each subnet for verification.

### Windows Server Setup: Port Change, SSM Installation, IIS Configuration, and Let's Encrypt SSL Integration
Configure a Windows Server by changing default ports, installing AWS Systems Manager agent, setting up IIS for hosting, and securing websites with Let’s Encrypt SSL certificates.

### Windows Server with MSSQL Setup: Launch from AMI, Configure SQL Authentication, User Setup, Drive Mapping, Port Change, Remote Access, and Backup
Launch a Windows Server with pre-installed MSSQL Standard. Enable SQL authentication, configure users, redirect data/log/backup to D: drive, change default SQL port, enable remote access, create databases, and perform backups.

### Docker Image Best Practices – Secure Nginx with Simple HTML Page
Build a secure Docker image serving a simple HTML page via Nginx. Follow best practices including minimal base images, non-root user, and minimal layers for efficiency and security.

### FastAPI Project: Full CRUDL Endpoints with AWS SDK Integration and API Features
Develop a FastAPI app offering full CRUDL operations and integrate AWS SDK to manage EC2 details like EBS volume sizes, protection settings, and security groups. Support JSON input/output and robust error handling.

### AWS EC2 Key Pair Management with Terraform Module
Terraform module to manage EC2 key pairs: creation, import, conditional resource handling, with flexible input/output for seamless key pair lifecycle management.

### AWS EC2 Instance Provisioning with Terraform Module
Terraform module to provision EC2 instances supporting on-demand and spot pricing, custom configurations, encryption, tagging, IAM roles, and conditional resource creation.

### API Load Testing Script for https://aws.eortv.com Using Python
Python script to perform load testing on https://aws.eortv.com API with concurrent users at different levels (100 to 1000). Analyze response time, stability, and scalability under varying loads.

### Terraform Script to Provision AWS EKS Managed Node Group
Terraform script to create an Amazon EKS managed node group, including cluster, IAM roles, networking, and subnets for scalable Kubernetes deployments on AWS.

### Terraform Module Development for AWS Budget Creation
Terraform module to create AWS Budgets with configurable parameters like budget name, amount, period, type, email notifications, and threshold alerts.

### Identifying and Resolving Corrupt Terraform State Files Using State Management Commands
Document steps to identify and fix corrupt Terraform state files caused by manual or concurrent changes using terraform state commands such as list, show, rm, and import.

### Learning Golang, Kubernetes CRDs, and Deploying Burrito.tf
Study Golang basics and Kubernetes CRDs, build a Kubernetes operator, and deploy Burrito.tf using Helm and manifests to understand Kubernetes operator patterns and automation.
