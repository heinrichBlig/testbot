from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, This is Brandhue Chat app check out our website: http://brandhue.studio/"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    if msg == "1":
        resp.message(
            "This is Home bot: we help find you next home ")
    elif msg == "2":
        resp.message(
            "This is Home bot 2: R200 ")

    else:
        resp.message(
            "This is Home bot how can we help you \n 1) about us \n 2) cost ")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
