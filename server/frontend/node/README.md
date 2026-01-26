# Node.js  (Express)
Make sure you have the following installed:
- Node.js (v16 or later):Download and install from [nodejs.org](https://nodejs.org/) and run the setup.
- npm (comes with Node.js) (-npm install)



# Running 
 Start the server using - node server.js
 The server runs on port 8000.

 ### GET  `/chat`(for browser testing)
 
 example:http://localhost:8000/chat?message=hi

 Response:
```json
{
  "reply": "hi"
}
```
 ### POST `/chat`

**Request Body:**
```json
{
  "message": "Hello"
}
```
Response:
```json
{
  "reply": "Hello"
}
```
You can test this endpoint using:
Postman,curl

Example using curl:
curl -X POST http://localhost:8000/chat

-H "Content-Type: application/json"
-d '{"message":"Hello"}'

---
## Deployment (Node)

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

### AWS Setup Steps for Node
1. Installed Node.js and npm on the existing EC2 instance (16.171.224.237).
2. Enabled inbound rule for port 8000 in the AWS Security Group.
3. Installed required packages using npm install.
4. Started the Node server using node server.js.