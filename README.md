# whatsapp-bot-qwen2.5
A WhatsApp chatbot powered by Qwen2.5 LLM, integrated with Twilio and Flask.  This project demonstrates how to build a private, AI-driven assistant that responds  to WhatsApp messages in real-time using open-source models.

This repository contains the source code and documentation for building a **WhatsApp chatbot** using the **Qwen2.5 Large Language Model (LLM)**.  
It integrates **Twilio WhatsApp API** with a **Flask backend** that connects to the locally hosted Qwen2.5 model running on RunPod or Ollama.  

## Features
- Real-time responses to WhatsApp messages
- Powered by **Qwen2.5 LLM**
- Flask-based backend for easy deployment
- Compatible with Twilio Sandbox & production numbers

## Contents
- `qwen_api.py` → Flask app connecting Twilio WhatsApp to Qwen2.5  
- `whatsapp_bot.py` → API wrapper for Qwen2.5 model running locally  
- `process_document.pdf` → Reference documents  

## Setup
Follow the step-by-step instructions in the documentation to:
1. Configure Twilio Sandbox for WhatsApp
2. Deploy Flask server with Qwen2.5 backend
3. Connect everything to test your WhatsApp bot in real time

---

Created as part of my YouTube channel **[Neural Bytes with Prem](https://youtube.com/@NeuralBytes-PKR)**  
Check out the tutorial video here: [[WhatsApp_BOT_Tutortial](https://www.youtube.com/watch?v=PA65LSLfSKE&t=29s)]
