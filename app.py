from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    # Create reply
    resp = MessagingResponse()
    if msg == "Flats2rent":
        resp.message("Hi, whats your name?")
    elif msg == "Heinrich":
        resp.message("Hi {}".format(msg) + ", what is your monthly budget? \n1. <R500 \n2. R600 – R1000 \n3. R1100 – R3000 \n4. R3000 or more")
    elif msg == "1":
        resp.message("Good, and where do you want to live? \n1. Johannesburg \n2. Pretoria ")

    else:
        resp.message("Enter Flats2rent to start ")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
