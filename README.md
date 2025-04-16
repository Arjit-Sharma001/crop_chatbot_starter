# 🌾 Crop Yield Chatbot

A chatbot that generates crop performance insights and visual charts using Gemini AI and Python.

---

## 🚀 Features

- 🤖 Gemini-powered agricultural insights *(can upgrade to Vertex AI)*
- 🧠 Flexible query interpretation via **spaCy NLP**
- 📈 Auto-generated charts using **Matplotlib**
- 💬 Web UI interface *(can integrate with Google Chat App using Google Cloud)*
- 🔮 Easily extendable to Telegram bots or cloud services

---

## 🧠 Logical Flow

1. **User Input**: A natural language crop-related question
2. `preprocessing.py`: Performs lemmatization and stop-word removal using `spaCy`
3. `chat_handler.py`: Detects intent (e.g., moisture, yield) and chart type
4. `vertex_ai_model.py`: Queries **Gemini** (or Vertex AI in future) for contextual insights
5. `chart_generator.py`: Generates the appropriate chart using `matplotlib`
6. `main.py`: Returns a structured response with insight + optional chart image

---

## 📊 Data Interpretation

- Reads from a **static CSV** containing crop-related indicators  
  *(can be upgraded to BigQuery, Firebase, or dynamic APIs)*
- Supports chart types: **line**, **bar**, **scatter**
- Charts are served dynamically through the `/static/` directory

---

## ☁️ Cloud Configuration (Future-Ready)

- **Google Cloud Functions**: For lightweight backend deployment
- **Apps Script**: For scripting and integration with **Google Chat App**
- **Firebase / BigQuery**: As a scalable data backend

---

## 🛠 Setup Instructions

```bash
git clone https://github.com/Arjit-sharma001/crop-chatbot-starter
cd crop-chatbot-starter

python -m venv .venv
. .venv/Scripts/activate  # or source .venv/bin/activate on macOS/Linux

pip install -r requirements.txt
python -m spacy download en_core_web_sm
python main.py
