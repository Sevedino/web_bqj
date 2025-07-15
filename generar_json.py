import requests
import json

# === CONFIGURACIÓN ===
API_KEY = 'AIzaSyCw_1sPnWIHqNn7Qpu2Ht2vEdegoB2ABsk'  # ← reemplaza con tu API Key de YouTube Data API v3
PLAYLIST_ID = 'PLgSG7f4hM1f7J4JexzXxjmw223x5WBg8L'
MAX_RESULTS = 20  # puedes ajustarlo

# === FUNCIÓN PARA OBTENER EPISODIOS ===
def obtener_videos():
    url = f"https://www.googleapis.com/youtube/v3/playlistItems"
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

# === GUARDAR COMO JSON ===
def guardar_json(episodios):
    with open("episodios.json", "w", encoding="utf-8") as f:
        json.dump(episodios, f, ensure_ascii=False, indent=2)

# === EJECUCIÓN ===
if __name__ == "__main__":
    episodios = obtener_videos()
    guardar_json(episodios)
    print(f"{len(episodios)} episodios guardados en episodios.json")
