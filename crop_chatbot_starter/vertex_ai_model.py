# def query_vertexai(prompt):
#     # Simulate AI insight logic based on keyword
#     if "yield" in prompt:
#         return "Crop yield has steadily increased over the past years due to improved techniques."
#     elif "soil" in prompt or "moisture" in prompt:
#         return "Soil moisture has shown seasonal variations impacting crop performance."
#     elif "temperature" in prompt:
#         return "Rising temperatures have slightly decreased crop yields."
#     else:
#         return "I couldn’t extract useful insight from this prompt."

# VERTEX AI
# import vertexai
# from vertexai.language_models import TextGenerationModel

# def query_vertexai(prompt):
#     vertexai.init(project="your-project-id", location="us-central1")

#     model = TextGenerationModel.from_pretrained("text-bison")
#     response = model.predict(
#         prompt,
#         max_output_tokens=256,
#         temperature=0.7,
#         top_p=0.8,
#         top_k=40
#     )
#     return response.text.strip()



# HUGGING
# from transformers import pipeline

# generator = pipeline("text-generation", model="tiiuae/falcon-rw-1b",device=0)  # Better than distilgpt2

# def query_vertexai(prompt):
#     result = generator(f"Agriculture question: {prompt}", max_length=100, do_sample=True, temperature=0.7)
#     return result[0]["generated_text"].strip()

# CHAT GPT
# import openai

# client = openai.OpenAI(api_key="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")

# def query_vertexai(prompt):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  # or "gpt-4"
#         messages=[
#             {"role": "system", "content": "You are an expert in agriculture."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.7,
#         max_tokens=200
#     )
#     return response.choices[0].message.content.strip()


import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="AIzaSyAGiKb7tWb4sonLfXRL9Q3fqOdU5qFEKjU")  # Replace with your actual Gemini API key

model = genai.GenerativeModel("gemini-1.5-pro")  # Replace with the actual model name after confirming

def query_vertexai(prompt):
    # Generate content using the selected model
    response = model.generate_content(prompt)
    return response.text.strip()


