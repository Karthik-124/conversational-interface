# conversational-interface -Task1
This contains the initial express backend setup for task 1.

# Directory Structure
```text
conversational-interface/
├── server.js # Express server entry point
├── package.json
├── package-lock.json 
├── .gitignore # Ignored files (node_modules)
└── README.md # Project documentation

Make sure you have the following installed:
- Node.js (v16 or later)
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

## Frontend (Task 1)

A minimal web-based UI is included to interact with the `/chat` API.

- Users can enter a message and send it to the backend
- The conversation history is displayed on the screen
- The UI communicates with the backend using HTTP POST requests

To use the UI:
1. Start the backend server (`node server.js`)
2. Open `index.html` in a browser

