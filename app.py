from flask import Flask, request, jsonify
import requests
import dotenv
import os
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from modules.gpt_call import get_summary_messages

app = Flask(__name__)


dotenv.load_dotenv()

TWILIO_ACCOUNT_SID= os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = "whatsapp:+14155238886"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message_sid = ''

@app.route('/bot', methods=['GET'])
def bot():
    try:
        to_number = request.args.get("toNumber", os.getenv("TO_NUMBER"))
        summary_messages = get_summary_messages()

        if not to_number:
            return jsonify({"error": "to_number and message fields are required"}), 400

        for message in summary_messages:
            message = client.messages.create(
                from_=TWILIO_PHONE_NUMBER,
                body=message,
                to=f'whatsapp:{to_number}'
            )
        return jsonify({"message_sid": message.body, "status": "Message sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# if __name__ == '__main__':
#     app.run(port=4000, debug=True)