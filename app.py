from flask import Flask, request, jsonify
from modules.utils.twilio_messages import send_message, client
from modules.gpt_call import get_summary_messages
import time

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    try:
        to_number = request.json.get("to_number", "")
        if not to_number:
            return jsonify({"error": "to_number and message fields are required"}), 400
        message_response = send_message("These are the summaries for today", to_number)
        time.sleep(2)
        message_status = client.messages(message_response.sid).fetch().status
        if message_status != "queued":
            summary_messages = get_summary_messages()
            for message in summary_messages:
                send_message(message, to_number)
            return jsonify({"status": "Message sent successfully!"}), 200
        return jsonify({"status": "The user might not be in the sandbox"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=4000, debug=True)