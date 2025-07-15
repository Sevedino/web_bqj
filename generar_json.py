import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# === CONFIGURACIÓN ===
API_KEY = os.getenv("API_KEY")
PLAYLIST_ID = 'PLgSG7f4hM1f7J4JexzXxjmw223x5WBg8L'
MAX_RESULTS = 20

def obtener_videos():
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "part": "snippet",
        "playlistId": PLAYLIST_ID,
        "maxResults": MAX_RESULTS,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    datos = response.json()

    episodios = []

    for item in datos.get("items", []):
        snippet = item["snippet"]
        episodio = {
            "titulo": snippet["title"],
            "descripcion": snippet["description"],
            "videoId": snippet["resourceId"]["videoId"],
            "miniatura": snippet["thumbnails"]["medium"]["url"]
        }
        episodios.append(episodio)

    return episodios

def guardar_json(episodios):
    with open("episodios.json", "w", encoding="utf-8") as f:
        json.dump(episodios, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    episodios = obtener_videos()
    guardar_json(episodios)
    print(f"{len(episodios)} episodios guardados en episodios.json")
