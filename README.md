# conversational-interface 
This contains the client and server for conversational-interface.

# Directory Structure
```text
conversational-interface/
├── client/                 
│   └── index.html
├── python-server/          # New Python Backend
│   ├── .venv/              
│   └── app.py              # Flask Server Logic
├── server/                 # Node.js Backend
│   ├── node_modules/       
│   ├── package.json
│   └── server.js
├── .gitignore              # Git Ignore 
└── README.md               # Main Project Documentation
   ``` 
```
Make sure you have the following installed:
- Node.js (v16 or later):Download and install from [nodejs.org](https://nodejs.org/) and run the setup.
- npm (comes with Node.js)
- Python and pip
``` 
# Installation 
1.Clone the repository
  - git clone https://github.com/prasenjitb-cloud/conversational-interface
  cd conversational-interface
2.Install dependencies
 -npm install

3.Python Backend Setup
Create and activate a virtual environment (venv) to isolate dependencies.

Install Flask and Flask-CORS: pip install flask flask-cors.

Run the server: python app.py (Default port: 5000).

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

## Frontend 

A minimal web-based UI is included to interact with the `/chat` API.

- Users can enter a message and send it to the backend
- The conversation history is displayed on the screen
- The UI communicates with the backend using HTTP POST requests

To use the UI:
1. Start the backend server (`node server.js`)
or Start the backend server(Python) (`flask run`)
2. Open `index.html` in a browser

## Deployment (Python Backend)

The Flask backend is deployed on AWS EC2 (Free Tier).

- Cloud Provider: AWS EC2 (Amazon Linux)
- Public IP: 13.53.36.22
- Port: 5000

### Live Test URL
GET:
http://13.53.36.22:5000/chat?message=hello

This endpoint is accessible from both desktop and mobile browsers.

### Notes
- Port 5000 is enabled via EC2 Security Group inbound rules.
- Flask is currently running using the built-in development server.


### AWS Setup Steps
1. Created an EC2 instance (Free Tier)
2. Enabled inbound rule for port 5000
3. Installed Python and Flask
4. Ran the Flask app using `python3 app.py`
