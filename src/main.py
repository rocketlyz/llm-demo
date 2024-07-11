import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ['OPENAI_API_KEY']

print("YOUR KEY IS: %s" %(openai.api_key))
