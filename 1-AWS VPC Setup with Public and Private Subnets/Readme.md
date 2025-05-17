# VPC Setup with Public and Private Subnets and EC2 Instance Deployment

Setting up a Virtual Private Cloud (VPC) in AWS with both public and private subnets, and deploying EC2 instances across both subnets.

## Steps

### 1. **Create the VPC**
1. **Log in to AWS Management Console** and navigate to the **VPC** service.
2. Click **Create VPC**.
   - **IPv4 CIDR block**: `10.0.0.0/16`
3. Click **Create VPC**.

### 2. **Create Subnets**
Create both **Public** and **Private** subnets across different availability zones.

#### Public Subnets
1. **Public Subnet 1**:
   - **CIDR block**: `10.0.1.0/24`
   - **Availability Zone**: `us-east-1a`
2. **Public Subnet 2**:
   - **CIDR block**: `10.0.2.0/24`
   - **Availability Zone**: `us-east-1b`
3. **Public Subnet 3**:
   - **CIDR block**: `10.0.3.0/24`
   - **Availability Zone**: `us-east-1c`

#### Private Subnets
1. **Private Subnet 1**:
   - **CIDR block**: `10.0.11.0/24`
   - **Availability Zone**: `us-east-1a`
2. **Private Subnet 2**:
   - **CIDR block**: `10.0.12.0/24`
   - **Availability Zone**: `us-east-1b`
3. **Private Subnet 3**:
   - **CIDR block**: `10.0.13.0/24`
   - **Availability Zone**: `us-east-1c`

### 3. **Create an Internet Gateway (IGW)**
1. Go to the **VPC Dashboard**, then **Internet Gateways** > **Create Internet Gateway**.
2. Name it and click **Create**.
3. Attach the Internet Gateway to the VPC by selecting the IGW and clicking **Attach to VPC**.

### 4. **Create Route Tables**
#### Public Route Table
1. Go to **Route Tables** > **Create Route Table**.
   - **Name**: `Public-Route-Table`
   - Associate with the VPC.
2. Select the route table and click **Edit Routes** > **Add Route**.
   - **Destination**: `0.0.0.0/0` (default route to the internet).
   - **Target**: Select the Internet Gateway.
3. Associate the **Public-Route-Table** with the **Public Subnets**.
   - Go to **Subnet Associations** > **Edit subnet associations**, and select public subnets.

#### Private Route Table
1. Go to **Route Tables** > **Create Route Table**.
   - **Name**: `Private-Route-Table`
   - Associate with the VPC.
2. Select the route table and click **Edit Routes** > **Add Route**.
   - **Destination**: `0.0.0.0/0` (default route to the internet).
   - **Target**: Select the **NAT Gateway**.
3. Associate the **Private-Route-Table** with the **Private Subnets**.
   - Go to **Subnet Associations** > **Edit subnet associations**, and select private subnets.

### 5. **Create a NAT Gateway**
1. Go to **Elastic IPs** and create a new Elastic IP.
2. Go to **NAT Gateways** > **Create NAT Gateway**.
   - Choose one of the public subnets and assign the Elastic IP.
3. Update the **Private Route Table** to route internet traffic through the NAT Gateway.

### 6. **Create Security Groups**
1. Go to **EC2 Dashboard** > **Security Groups** > **Create Security Group**.
2. Create **Public Security Group**:
   - Allow inbound HTTP (port 80) and SSH (port 22) traffic from `0.0.0.0/0`.
   - Allow all outbound traffic.
3. Create **Private Security Group**:
   - Allow inbound traffic only from the **Public Security Group**.
   - Allow all outbound traffic.

### 7. **Launch EC2 Instances**
Launch EC2 instances in both **Public** and **Private** subnets:

#### Public Subnet EC2 Instances:
1. Launch three EC2 instances in **Public Subnets 1, 2, and 3**.
2. Assign **Public IP addresses** and select **Public Security Group**.
3. These instances will be accessible from the internet.

#### Private Subnet EC2 Instances:
1. Launch three EC2 instances in **Private Subnets 1, 2, and 3**.
2. Do not assign **Public IP addresses** and select **Private Security Group**.
3. These instances will rely on the NAT gateway for internet access.

### 8. **Verify the Setup**
1. **Public EC2 Instances**:
   - Access the public EC2 instances using their **Public IPs** via SSH.
   - Test HTTP/HTTPS access if a web server is running.

2. **Private EC2 Instances**:
   - SSH into a **Public EC2 instance**, then access **Private EC2 instances** by using private IPs.
   - Test internet access through the **NAT Gateway** (e.g., by running `sudo yum update` on Amazon Linux instances).

### Architecture Diagram
- **VPC CIDR**: `10.0.0.0/16`
- **Public Subnets**:
  - `10.0.1.0/24` (AZ 1)
  - `10.0.2.0/24` (AZ 2)
  - `10.0.3.0/24` (AZ 3)
- **Private Subnets**:
  - `10.0.11.0/24` (AZ 1)
  - `10.0.12.0/24` (AZ 2)
  - `10.0.13.0/24` (AZ 3)
- **Internet Gateway**: Attached to VPC.
- **NAT Gateway**: Used by private subnets for internet access.
- **EC2 Instances**:
  - 3 instances in **Public Subnets**.
  - 3 instances in **Private Subnets**.

---