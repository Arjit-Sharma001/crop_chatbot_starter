# Crop Insights Chatbot

A chatbot that generates crop performance insights and charts using Gemini AI and Python.

---

## 🚀 Features
- Gemini-powered agricultural insights (can upgrade to Vertex Ai)
- Flexible query interpretation via spaCy NLP
- Auto-generated charts using matplotlib
- Web UI support (can Integrate with Google chat app with Google Cloud)

---

## 🧠 Logical Flow

1. User types a crop-related question
2. `preprocessing.py`: Extracts keywords (lemmatization, filtering)
3. `chat_handler.py`: Matches intent and chart type
4. `vertex_ai_model.py`: Queries Gemini(vertex ai in future) for smart insights
5. `chart_generator.py`: Creates appropriate plot
6. `main.py`: Returns response + chart to frontend or Telegram

---

## 📊 Data Interpretation

- Charts generated using a static CSV (can upgrade to BigQuery/Firebase)
- Matplotlib used to draw `line`, `bar`, `scatter` plots
- Plots served via `static/` endpoint

---

## ☁️ Cloud Configuration

- **CLOUD FUNCTION** in future
- GOOGLE SCRIPT FOR SCRIPTING AND INTEGRATION WITH GOOGLE CHAT APP

---

## 🛠 Setup

```bash
git clone https://github.com/Arjit-sharma001/crop-chatbot-starter
cd crop-chatbot-starter

python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python main.py
