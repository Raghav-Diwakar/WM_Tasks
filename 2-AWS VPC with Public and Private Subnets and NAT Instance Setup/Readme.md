# VPC Setup with Public and Private Subnets and NAT Instance

Set up a Virtual Private Cloud (VPC) with both public and private subnets in AWS, and configure a NAT instance to provide internet access for instances in the private subnets. Additionally, EC2 instances will be launched in both public and private subnets to verify proper distribution and functionality.

---

## Steps to Set Up VPC with Public and Private Subnets, NAT Instance, and EC2 Instances

### 1. **Create the VPC**

1. Navigate to the **VPC Dashboard** in the AWS Management Console.
2. Click **Create VPC** and configure the following:
   - **VPC Name**: `MyVPC`
   - **IPv4 CIDR Block**: `10.0.0.0/16`
   - Leave other settings as default and click **Create VPC**.

### 2. **Create Subnets (Public and Private)**

#### **Public Subnets**:

1. Create three **Public Subnets** across different Availability Zones:
   - **Public Subnet 1**: `10.0.1.0/24` in `us-east-1a`
   - **Public Subnet 2**: `10.0.2.0/24` in `us-east-1b`
   - **Public Subnet 3**: `10.0.3.0/24` in `us-east-1c`

#### **Private Subnets**:

1. Create three **Private Subnets** across different Availability Zones:
   - **Private Subnet 1**: `10.0.11.0/24` in `us-east-1a`
   - **Private Subnet 2**: `10.0.12.0/24` in `us-east-1b`
   - **Private Subnet 3**: `10.0.13.0/24` in `us-east-1c`

### 3. **Set Up Route Tables**

#### **Public Route Table**:

1. In the VPC Dashboard, go to **Route Tables** and click **Create Route Table**.
   - Assign it to the `MyVPC` and name it `PublicRouteTable`.
   - Add a route:
     - **Destination**: `0.0.0.0/0`
     - **Target**: Your **Internet Gateway** (to be created next).
   - **Associate** this route table with the public subnets (`10.0.1.0/24`, `10.0.2.0/24`, `10.0.3.0/24`).

#### **Private Route Table**:

1. Create a **Private Route Table** and name it `PrivateRouteTable`.
2. Add a route to the **NAT Instance**:
   - **Destination**: `0.0.0.0/0`
   - **Target**: The **NAT Instance**.
3. Associate this route table with the private subnets (`10.0.11.0/24`, `10.0.12.0/24`, `10.0.13.0/24`).

### 4. **Create and Attach an Internet Gateway**

1. In the VPC Dashboard, go to **Internet Gateways** and click **Create Internet Gateway**.
2. Name it `MyInternetGateway` and click **Create**.
3. Attach the internet gateway to the `MyVPC`.

### 5. **Set Up NAT Instance**

#### **Launch a NAT Instance**:

1. Launch an EC2 instance using Amazon Linux 2 AMI (or Ubuntu).
   - Place it in **Public Subnet 1** (`10.0.1.0/24`).
   - Assign a public IP to the instance.
   - Allow SSH access from your IP address in the security group.
   - Disable **Source/Destination Check** for the instance.
   
2. **Disable Source/Destination Check**:
   - Run the following command to disable the source/destination check:
     ```bash
     aws ec2 modify-instance-attribute --instance-id i-xxxxxxxx --no-source-dest-check
     ```

3. **Enable IP Forwarding**:
   - Connect to the NAT instance and run:
     ```bash
     sudo sysctl -w net.ipv4.ip_forward=1
     ```

4. **Configure IP Masquerading**:
   - Run the following commands to enable IP masquerading:
     ```bash
     sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
     sudo service iptables save
     sudo service iptables restart
     ```

5. **Update Security Groups**:
   - Ensure the NAT instance security group allows inbound traffic from the private subnets.
   - Ensure the private subnets’ security group allows outbound traffic to the NAT instance.

### 6. **Launch EC2 Instances in Public and Private Subnets**

#### **Launch EC2 Instances in Public Subnets**:

1. Launch EC2 instances in each of the public subnets (`10.0.1.0/24`, `10.0.2.0/24`, `10.0.3.0/24`).
2. Choose an Amazon Machine Image (AMI) such as Amazon Linux 2 or Ubuntu.
3. Assign a public IP to the instances.
4. Configure security groups to allow SSH (port 22) from your IP address.

#### **Launch EC2 Instances in Private Subnets**:

1. Launch EC2 instances in each of the private subnets (`10.0.11.0/24`, `10.0.12.0/24`, `10.0.13.0/24`).
2. Choose an AMI (Amazon Linux 2, for example).
3. Do not assign public IPs to instances in private subnets.
4. Configure the security group to allow SSH access only from public subnets or your bastion host.

### 7. **Test the Setup**

1. **Verify Public Subnet Internet Access**:
   - SSH into an EC2 instance in the public subnet and run:
     ```bash
     ping google.com
     ```
   
2. **Verify Private Subnet Internet Access via NAT**:
   - SSH into an EC2 instance in the private subnet and run:
     ```bash
     ping google.com
     ```
   
3. **Verify Communication Between Subnets**:
   - Check if EC2 instances in public subnets can communicate with instances in private subnets and vice versa (via security groups).

---

## Summary of Key Components

- **VPC**: `10.0.0.0/16` CIDR block.
- **Public Subnets**: `10.0.1.0/24`, `10.0.2.0/24`, `10.0.3.0/24`.
- **Private Subnets**: `10.0.11.0/24`, `10.0.12.0/24`, `10.0.13.0/24`.
- **Internet Gateway**: Attached to the VPC.
- **NAT Instance**: Configured in the public subnet with source/destination check disabled.
- **Route Tables**: 
  - Public route table connected to the internet gateway.
  - Private route table connected to the NAT instance.
