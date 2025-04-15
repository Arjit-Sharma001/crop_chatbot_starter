import spacy
import subprocess

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Auto-download the model if it's missing
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"], check=True)
    nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    return [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
