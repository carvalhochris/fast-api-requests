from dotenv import load_dotenv
from fastapi import FastAPI
import requests
from fastapi import Response
import os

load_dotenv()

key = os.environ["DRF_API_KEY"]

app = FastAPI()

@app.get("/{email}")
async def root(email):
    print("hiya")
    # print("Email is ", email)
    # print("Key is ", key)
    r = requests.get(f'https://api.songcards.io/retrieve_artist_user/{email}', headers={'Authorization': f'Api-Key {key}'})
    text = r.text
    print(text)
    return Response(content=text, media_type="application/json")

