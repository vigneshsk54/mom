import google.generativeai as genai;
import os;

from utils.constants import model_config;

def generate_model():
    os.environ["API_KEY"] = "AIzaSyAj25zHHsH-UaMVoq_Y1QaVTCGPaPRvF0E";
    genai.configure(api_key=os.environ["API_KEY"])
    return genai.GenerativeModel("gemini-1.5-flash-latest", generation_config=model_config);