from flask import Flask, request, jsonify
from flask_cors import CORS
from models import insert_event, get_latest_events
from datetime import datetime

app = Flask(__name__)
CORS(app)

def parse_github_event(payload):
    # Determine action type and extract fields
    if 'pull_request' in payload:
        action = 'PULL_REQUEST'
        author = payload['pull_request']['user']['login']
        from_branch = payload['pull_request']['head']['ref']
        to_branch = payload['pull_request']['base']['ref']
        request_id = str(payload['pull_request']['id'])
        timestamp = payload['pull_request']['created_at']
    elif 'commits' in payload:
        action = 'PUSH'
        author = payload['pusher']['name']
        from_branch = None
        to_branch = payload['ref'].split('/')[-1]
        request_id = payload['after']
        timestamp = datetime.utcnow().isoformat()
    elif payload.get('action') == 'closed' and payload.get('pull_request', {}).get('merged'):
        action = 'MERGE'
        author = payload['pull_request']['user']['login']
        from_branch = payload['pull_request']['head']['ref']
        to_branch = payload['pull_request']['base']['ref']
        request_id = str(payload['pull_request']['id'])
        timestamp = payload['pull_request']['merged_at']
    else:
        return None
    return {
        'request_id': request_id,
        'author': author,
        'action': action,
        'from_branch': from_branch,
        'to_branch': to_branch,
        'timestamp': timestamp
    }

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    print("payload: ", payload)
    event = parse_github_event(payload)
    if not event:
        return jsonify({'error': 'Unsupported event'}), 400
    insert_event(event)
    return jsonify({'status': 'success'}), 201

@app.route('/events', methods=['GET'])
def events():
    data = get_latest_events()
    for d in data:
        d['_id'] = str(d['_id'])
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True) 