import os
import json
from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Load mock data
with open('data/customers.json', 'r') as f:
    customers = json.load(f)

with open('data/knowledge_base.json', 'r') as f:
    knowledge_base = json.load(f)

with open('data/appointments.json', 'r') as f:
    appointments = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/current_customer')
def current_customer():
    # Simulate current customer on call
    return jsonify(customers[0])

@app.route('/api/current_appointment')
def current_appointment():
    return jsonify(appointments[0])

@app.route('/api/analyze_screen', methods=['POST'])
def analyze_screen():
    # Simulate AI screen analysis
    analysis = {
        "detected_issue": "iPhone Email Setup - Exchange Configuration Error",
        "confidence": 0.92,
        "screen_elements": [
            "Settings app open",
            "Mail, Contacts, Calendars section",
            "Exchange account showing 'Cannot Connect' error"
        ],
        "suggested_guidance": [
            "I can see your email settings are open. Let's check your Exchange server settings.",
            "Tap on your work email account that shows 'Cannot Connect'",
            "Now tap 'Account Info' at the top",
            "Look for the server field - it should say 'outlook.office365.com'",
            "If it shows something different, let's update it together"
        ],
        "escalation_needed": False,
        "knowledge_base_match": "kb_001"
    }
    return jsonify(analysis)

@app.route('/api/analyze_conversation', methods=['POST'])
def analyze_conversation():
    # Simulate conversation analysis
    conversation_data = request.json
    
    analysis = {
        "customer_sentiment": "frustrated",
        "issue_category": "email_setup",
        "confidence": 0.89,
        "suggested_empathy": "I understand how frustrating email issues can be, especially for work. Let's get this fixed for you right away.",
        "next_steps": [
            "Acknowledge frustration with empathy",
            "Confirm you can see their screen",
            "Guide through Exchange server settings check"
        ],
        "estimated_resolution_time": "3-5 minutes"
    }
    return jsonify(analysis)

@app.route('/api/knowledge_base/<kb_id>')
def get_knowledge_base(kb_id):
    kb_item = next((item for item in knowledge_base if item['id'] == kb_id), None)
    return jsonify(kb_item) if kb_item else jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)