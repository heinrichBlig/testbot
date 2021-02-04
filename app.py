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
      resp.message(
         "Hi, whats your name? ")
    
    if msg != "":
        resp.message(
            "Hi {}".format(msg))

    if msg == "1":
        resp.message(
            "Good, and where do you want to live? 1. Johannesburg 2. Pretoria ")
    elif msg == "2":
        resp.message(
            "This is Home bot 2: R200 ")
           
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
