import dotenv
import os
from twilio.rest import Client

dotenv.load_dotenv()

TWILIO_ACCOUNT_SID= os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = "whatsapp:+14155238886"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_message(message, to_number):
    message_response = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        body=message,
        to=f'whatsapp:{to_number}'
    )
    return message_response
