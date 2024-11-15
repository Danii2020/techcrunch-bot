import time
from flask import jsonify
from modules.gpt_call import get_summary_messages
from modules.utils.twilio_messages import send_message, client

def send_summary_messages(to_number):
    message_response = send_message("These are the summaries for today", to_number)
    time.sleep(2)
    message_status = client.messages(message_response.sid).fetch().status
    if message_status != "queued":
        summary_messages = get_summary_messages()
        for message in summary_messages:
            send_message(message, to_number)
        return jsonify({"status": "Message sent successfully!"}), 200
    return jsonify({"status": "The user might not be in the sandbox"}), 400