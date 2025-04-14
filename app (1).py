from flask import Flask, render_template, request, jsonify
from jarvis_main import speak
from jarvis_tasks import handle_task
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    """Handle user commands."""
    command_text = request.json.get("command")
    if command_text:
        response = handle_task(command_text)
        return jsonify({"response": response})
    return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)