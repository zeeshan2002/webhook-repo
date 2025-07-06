# Webhook Receiver Backend (Flask)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set MongoDB URI (optional):
   - Create a `.env` file:
     ```
     MONGO_URI=mongodb://localhost:27017/webhookdb
     ```
3. Run the server:
   ```bash
   python app.py
   ```

## Endpoints
- `POST /webhook` — Receives GitHub webhook events
- `GET /events` — Returns latest events for frontend polling 