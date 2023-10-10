from flask import Flask, render_template, request, jsonify
import vonage

app = Flask(__name__)

# Replace with your Vonage API key and secret
client = vonage.Client(key="b78ec810", secret="SkV66w8nnV1Wsi0v")
sms = vonage.Sms(client)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        recipient_number = request.form["recipient_number"]
        message_text = request.form["message_text"]

        responseData = sms.send_message(
            {
                "from": "Vonage APIs",
                "to": recipient_number,
                "text": message_text,
            }
        )

        if responseData["messages"][0]["status"] == "0":
            message_status = "Message sent successfully."
        else:
            message_status = f"Message failed with error: {responseData['messages'][0]['error-text']}"

        return render_template("index.html", message_status=message_status)

    return render_template("index.html", message_status=None)

def account():
    data = request.json
    address = data.get('address')
    # Process the address (e.g., store it, log it, etc.)
    print(f'Connected MetaMask address: {address}')
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)
