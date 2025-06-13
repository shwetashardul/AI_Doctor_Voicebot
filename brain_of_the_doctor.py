# Step 1: Setup GROQ API key
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()  # Load from .env
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Step 2: Convert image to required format
import base64

image_path = "acne.jpeg"
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Setup multimodal LLM
from groq import Groq

query = "Is there something wrong with my face?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

client = Groq(api_key=GROQ_API_KEY)  # Use the API key

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}",
                },
            },
        ],
    }
]

chat_completion = client.chat.completions.create(
    messages=messages,
    model=model
)

print(chat_completion.choices[0].message.content)
