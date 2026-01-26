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