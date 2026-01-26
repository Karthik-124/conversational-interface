
# Python Backend (Flask)

A Flask-based server logic for handling chat interactions.

## Installation

1. Create and activate a virtual environment:
  ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
  ```
2. Install dependencies 
  ```bash
    pip install -r requirements.txt
  ```

3. Run the server: python app.py (Default port: 5000).

## Deployment (Python Backend)

The Flask backend is deployed on AWS EC2 (Free Tier).

- Cloud Provider: AWS EC2 (Amazon Linux)
- Public IP: 16.171.224.237
- Port: 5000

### Live Test URL
GET:
http://16.171.224.237:5000/chat?message=hello

This endpoint is accessible from both desktop and mobile browsers.

### Notes
- Port 5000 is enabled via EC2 Security Group inbound rules.
- Flask is currently running using the built-in development server.


### AWS Setup Steps
1. Created an EC2 instance (Free Tier)
2. Enabled inbound rule for port 5000
3. Installed Python and Flask
4. Ran the Flask app using `python3 app.py


