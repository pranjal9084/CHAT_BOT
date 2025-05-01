# 🤖 Streamlit + Groq Socratic Chatbot

A conversational **AI chatbot** built with **Streamlit** and **Groq API**, featuring an optional **Socratic mode** to promote learning through guided questions instead of direct answers. Ideal for educational platforms and learning assistants.

---

## ✨ Features

- 🧠 Powered by Groq API (OpenAI-compatible)
- 💬 Real-time chat interface with **Streamlit**
- 🎓 **Socratic Mode**: Helps users learn through thought-provoking questions
- 📚 Maintains conversation history
- 🎨 Minimal, clean UI

---

## 🔧 Requirements

- Python 3.8+
- Groq API Key
- Streamlit

Install dependencies:

```bash
pip install -r requirements.txt
```
# 🔑 Setup

## Clone the repo:
```bash
git clone https://github.com/yourusername/streamlit-socratic-chatbot.git
cd streamlit-socratic-chatbot
```
## Add your Groq API Key:

Create a .env file in the root directory:
```python
GROQ_API_KEY=your_groq_api_key
```
---

## Run the chatbot:
```python
streamlit run chat_bot.py
```
📁 File Structure

.
             # Streamlit UI & logic
├── chat_bot.py           # Handles Groq interactions, Streamlit UI & logic
├── requirements.txt     # Dependencies
├── .env                 # API Key file (not committed)
└── README.md            # You're reading it!

## 🔗 Live Demo

👉 [Click here to try the chatbot](https://genai-edu-chatbot.streamlit.app/)

> Enable **Socratic mode** from the checkbox and start learning interactively!

![image](https://github.com/user-attachments/assets/9d4a3502-a553-4363-9158-886d3dba517d)



## Built with 💡 by Pranjal Gupta
