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
        name ="name"
     
 
    elif msg == msg and  name == "name":
        resp.message("Hi {}".format(msg))
       
   
    else:
       resp.message("Enter Flats2rent to start ") 
    return str(resp)
        
if __name__ == "__main__":
    app.run(debug=True)
