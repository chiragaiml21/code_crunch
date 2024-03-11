# import google.generativeai as genai
from googlesearch import search
import webbrowser
import pywhatkit
import os
from langchain_google_genai import GoogleGenerativeAI
# from asr import asr
# from tts2 import tts
from dotenv import load_dotenv
load_dotenv()


GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")


# -------------------As the generative output contains multiple *. So this function removes them-------------------
def preprocess(text):
    text = text.replace('*', '')
    return text


# --------------------Conversation Handling----------------------
def response(text):
    llm = GoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GOOGLE_API_KEY,
    )

    response = llm.invoke(text)
    response = preprocess(response)
    print(response)
    # tts(response)


# ---------------------Open Google--------------------------------
def browse(url):
    webbrowser.open_new(url)


# -----------------------Play Youtube video------------------------
def play_on_youtube(query):
    query = query.split("play ")[1]
    query = query.split(" on youtube")[0]
    print(f"Playing {query} on youtube.....")
    # tts(f"Playing {query} on youtube.....")
    pywhatkit.playonyt(query)


# ------------------------Search in Google--------------------------
def search_on_google(text):
    search_term = text.split("search for ")[1] if "search for " in text else text
    print(f"Searching Google for : {search_term}")
    # tts(f"{search_term}")
    top_result = list(search(search_term, advanced=True))

    print(f"Title : {top_result[0].title}")
    print(f"Description : {top_result[0].description}")
    # tts(f"{top_result[0].description}")

    print("Would you like me to show you the results on web? (yes/no)")
    # tts("Would you like me to show you the results on web?")
    # show = asr()
    show = input()
    print("User : ", show)
    if "yes" in show.lower():
        browse(top_result[0].url)
    else:
        return