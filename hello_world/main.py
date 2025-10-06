import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose the model
model = genai.GenerativeModel("gemini-2.5-flash")

# Send a message
response = model.generate_content("Hey there")

# Print response
print(response.text)
