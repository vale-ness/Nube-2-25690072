import requests, os, time
from dotenv import load_dotenv
load_dotenv()

t0 = time.perf_counter()
API_KEY = os.getenv("apikey")
url = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "q": "Ciudad Valles,MX",
    "appid": API_KEY,
    "units": "metric",
    "lang": "es"
}
r = requests.get(url, params=params)
r.raise_for_status()
datos = r.json()
ms = (time.perf_counter()- t0) * 1000
print(r.status_code, f"{ms:.0f} ms", len(r.content), "bytes")
for pronostico in datos["list"]:
    temperatura = pronostico["main"]["temp"]
    descripcion = pronostico["weather"][0]["description"]
    hora = pronostico["dt_txt"]
    print(hora, "-", temperatura, "°C -", descripcion)