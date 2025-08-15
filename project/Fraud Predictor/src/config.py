
import os
from dotenv import load_dotenv

def load_env():
  return load_dotenv()

def get_key():
  return os.getenv("API_KEY")
