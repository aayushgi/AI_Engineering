import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key not found")


client = Groq(api_key=my_api_key)
model=""