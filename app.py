from flask import Flask, request, jsonify
from modules.messages_service import send_summary_messages


app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    try:
        to_number = request.json.get("to_number", "")
        if not to_number:
            return jsonify({"error": "to_number and message fields are required"}), 400
        return send_summary_messages(to_number=to_number)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=4000, debug=True)