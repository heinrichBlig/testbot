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
    name ="name"
    # Create reply
    resp = MessagingResponse()
    if msg == "Flats2rent":
        resp.message("Hi, whats your name?")
       
    elif msg != "" and  name == "name":
        resp.message("Hi {}".format(msg) + "what is your monthly budget? 1. <R500 2. R600 – R1000 3. R1100 – R3000 4. R3000 or more")
       
   
    else:
       resp.message("Enter Flats2rent to start ") 
    return str(resp)
        
if __name__ == "__main__":
    app.run(debug=True)
