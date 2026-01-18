# conversational-interface 
This contains the initial express backend setup.

# Directory Structure
```text
conversational-interface/
├── client/
│   └── index.html       # Frontend UI
└── server/
    ├── server.js        # Express logic
    ├── package.json     
    ├── package-lock.json
    └── README.md        # Documentation

Make sure you have the following installed:
- Node.js (v16 or later):Download and install from [nodejs.org](https://nodejs.org/) and run the setup.
- npm (comes with Node.js)
``` 
# Installation 
1.Clone the repository
  - git clone https://github.com/prasenjitb-cloud/conversational-interface
  cd conversational-interface
2.Install dependencies
 -npm install

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
2. Open `index.html` in a browser

