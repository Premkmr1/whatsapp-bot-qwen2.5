from flask import Flask, request, Response
import requests

app = Flask(__name__)

LLM_API_URL = "https://wool-functionality-camp-civic.trycloudflare.com/generate"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body", "").strip()
    sender = request.form.get("From", "")
    
    print(f"Incoming WhatsApp message from {sender}: {incoming_msg}")

    # Call your LLM model
    try:
        response = requests.post(LLM_API_URL, json={"prompt": incoming_msg})
        llm_reply = response.json().get("response", "Sorry, I didn't understand that.")
    except Exception as e:
        llm_reply = f"Error contacting LLM: {str(e)}"

    # Respond back to WhatsApp via TwiML
    reply_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{llm_reply}</Message>
</Response>"""
    
    return Response(reply_xml, mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
