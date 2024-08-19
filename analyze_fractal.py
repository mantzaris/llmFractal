# filename: analyze_fractal.py
import openai
import os
from dotenv import load_dotenv
import sys

load_dotenv()
openai.api_key = os.getenv("OPENAIAPIKEY")

def analyze_fractal(image_path, api_key):
    return f"Test successful for image: {image_path} with API key: {api_key}"



def test1():
    return "from python"

def test2():
    return "from python 2nd yay!"


def check_python_env():
    return sys.executable


def ask_how_are_you():
    prompt = "How are you?"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )

    return response['choices'][0]['text'].strip()
