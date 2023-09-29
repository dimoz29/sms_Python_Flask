from flask import Flask, request, jsonify
import vonage
from web3 import Web3

app = Flask(__name__)

# Initialize Vonage
client = vonage.Client(key="b78ec810", secret="SkV66w8nnV1Wsi0v")
sms = vonage.Sms(client)

# Initialize Web3
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/a99fc8833eb8497e84637ab7db564a9c'))

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    recipient_number = data['recipient_number']
    message_text = data['message_text']

    # Send SMS via Vonage
    responseData = sms.send_message({
        "from": "Vonage APIs",
        "to": recipient_number,
        "text": message_text
    })

    if responseData["messages"][0]["status"] == "0":
        return jsonify({"status": "Message sent successfully"})
    else:
        return jsonify({"status": "Message failed"})

if __name__ == '__main__':
    app.run(debug=True)
