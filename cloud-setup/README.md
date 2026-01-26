# Cloud Setup (AWS EC2)

This document describes how the conversational-interface backends are deployed on AWS EC2 using the Free Tier.

A single EC2 instance is used to host:
- Python (Flask) backend
- Node.js (Express) backend

Each backend runs on a different port.

---

## Overview

- Cloud Provider: AWS EC2
- OS: Amazon Linux
- Instance Type: Free Tier eligible
- Public IP: 16.171.224.237

---

## Network Configuration (Security Groups)

The following inbound rules are enabled on the EC2 Security Group:

| Port | Service              | Purpose       |
|-----:|----------------------|-------------  |
| 5000 | Python Flask Backend | `/chat` API   |
| 8000 | Node.js Backend      | `/chat` API   |
| 22   |  SSH                 |Remote Terminal|

Source for both ports: 0.0.0.0/0

## AWS Account & EC2 Instance Creation

Go to https://aws.amazon.com

Click Sign In to the Console,enter all the required details and keep proceeding.

Login using your AWS account credentials

In the AWS Console, search for EC2

Click Launch Instance

Choose Amazon Linux

Select a Free Tier eligible instance type

Create or select a key pair (.pem file) and download it. (key.pem)

Allow SSH (port 22) in network settings

Click Launch Instance

After launch, note down the Public IPv4 address.

## Security Groups

To allow external access to the backend services:

Go to EC2 → Instances

Click on the created instance

Open the Security tab

Click the Security Group link(highlighted in blue)

Select Edit inbound rules.
Click on the add rule.
Select TCP.

Add the rules mentioned above.

Click Save rules

### Project Setup
In EC2->Instance, click on Connect and select public link.
In the opened EC2 terminal :-
```
git clone https://github.com/prasenjitb-cloud/conversational-interface.git

cd conversational-interface
```


## Deployment (Python Backend)

Run these commands :-
```
sudo yum update -y
sudo yum install python3 -y
sudo yum install python3-pip -y
pip3 install flask
pip3 install -r requirements.txt

```

## Run the Flask app

```
cd backend
cd python-server
python3 app.py
```

The Flask backend is deployed on AWS EC2 (Free Tier).

- Cloud Provider: AWS EC2 (Amazon Linux)
- Public IP: 16.171.224.237
- Port: 5000

## Live Test URL
GET:
http://16.171.224.237:5000/chat?message=hello

This endpoint is accessible from both desktop and mobile browsers.

### Notes
- Port 5000 is enabled via EC2 Security Group inbound rules.
- Flask is currently running using the built-in development server.


## AWS Setup Steps
1. Created an EC2 instance (Free Tier)
2. Enabled inbound rule for port 5000
3. Installed Python and Flask
4. Ran the Flask app using `python3 app.py`

## Deployment (Node)

To Install Node Run:-
```
curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo yum install nodejs -y
```

Install Dependencies:-
```
cd frontend
cd node
npm install
```

To Run:-
``` 
npm run start
``` 
or 
``` 
node server.js
```

The Node.js Server is deployed on AWS EC2 (Free Tier).

- Cloud Provider: AWS EC2 (Amazon Linux)
- Public IP: 16.171.224.237
- Port: 8000

### Live Test URL
GET:
http://16.171.224.237:8000/chat?message=hello

This endpoint is accessible from both desktop and mobile browsers.


### Notes 
Port 8000 is enabled via EC2 Security Group inbound rules.

Express is currently running as the primary server for the frontend UI and Node API.

## AWS Setup Steps for Node
1. Installed Node.js and npm on the existing EC2 instance (16.171.224.237).
2. Enabled inbound rule for port 8000 in the AWS Security Group.
3. Installed required packages using npm install.
4. Started the Node server using node server.js.

## Note 
 If the instance is stopped and started, the Public IP will change.
 Ensure the Frontend code is updated with the new IPv4 address.