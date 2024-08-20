# filename: analyze_fractal.py
import openai
import os
import time
from dotenv import load_dotenv
import sys
from openai import OpenAIError, RateLimitError  # Import directly from openai




load_dotenv()
api_key = os.getenv("OPENAIAPIKEY")
client = openai.OpenAI(api_key=api_key)

def analyze_fractal(image_path, api_key):
    return f"Test successful for image: {image_path} with API key: {api_key}"



def test1():
    return "from python"

def test2():
    return "from python 2nd yay"


def check_python_env():
    return sys.executable




def ask_how_are_you():
    prompt = "How are you?"

    for _ in range(3):  # Retry 3 times
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=50
            )
            return response.choices[0].message.content.strip()
        except RateLimitError:
            print("Rate limit exceeded. Retrying in 5 seconds...")
            time.sleep(5)  # Introduce a delay before retrying
        except OpenAIError as e:
            print(f"OpenAI API error: {str(e)}")
            break
    return "Failed to get a response due to rate limit or API error."

