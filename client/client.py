import requests
import time

url = "http://server:8000"

for i in range(5):
    response = requests.get(url)
    print(f"Respuesta {i+1}: {response.text}")
    time.sleep(1)  # Pequeña pausa entre peticiones
