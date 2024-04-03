import openai
import time
import sys
import os
import traceback
import google.generativeai as palm
from google.api_core import exceptions
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize

# Set the API keys from prompted user inputs
print("Please enter your OpenAI API key")
openai_key = input()
print("Please enter your Google API key")
google_key = input()

#################### Set ChatGPT model configs
max_tokens = 1600
os.environ["OPENAI_API_KEY"] = openai_key
openai.api_key = os.getenv("OPENAI_API_KEY")

model_API_gpt35 = "gpt-3.5-turbo-0613"
model_API_gpt4 = "gpt-4-0613"

systemMsg = 'Hello I am doing a basic test of your functionality.'
userMsg = 'If you successfully receive my message please reply with your model name and greetings.'  
messages = [{"role": "system", "content": systemMsg},
            {"role": "user", "content": userMsg}]

prompt = systemMsg + userMsg

# Check GPT-3.5
try:
    response = openai.ChatCompletion.create(
        model=model_API_gpt35,
        messages=messages,
        max_tokens=max_tokens,
        top_p=0.95)
    
    print(response["choices"][0]["message"]['content'])      

except:
    error = sys.exc_info()[0]
    if error == openai.error.InvalidRequestError: # something is wrong: e.g. prompt too long
        print(f"InvalidRequestError\nPrompt passed in:\n\n{prompt}\n\n")
        assert False
    print("API error:", error)
    print("Basic test not passed. Error occurred when testing GPT-3.5 model.")
    exit()
    
# Check GPT-4
try:
    response = openai.ChatCompletion.create(
        model=model_API_gpt4,
        messages=messages,
        max_tokens=max_tokens,
        top_p=0.95)
    
    print(response["choices"][0]["message"]['content'])      

except:
    error = sys.exc_info()[0]
    if error == openai.error.InvalidRequestError: # something is wrong: e.g. prompt too long
        print(f"InvalidRequestError\nPrompt passed in:\n\n{prompt}\n\n")
        assert False
    print("API error:", error)
    print("Basic test not passed. Error occurred when testing GPT-4 model.")
    exit()
    

#################### Set PaLM2 model configs
max_tokens = 2048
palm.configure(api_key=google_key)
models = [m for m in palm.list_models() if "generateText" in m.supported_generation_methods]
model = models[0].name

try:          
    response = palm.generate_text(
        model=model,
        prompt=prompt,
        top_p=0.95,
        max_output_tokens=max_tokens)
    print(response)
    print("Basic test passed!")

except exceptions as e:
    print("An unexpected error occurred:", str(e))
    print("Basic test not passed. Error occurred when testing PaLM2 model.")
    
except Exception as e:
    print("An unexpected error occurred:", str(e))
