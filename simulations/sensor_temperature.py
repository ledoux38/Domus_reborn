import random
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests

# Paramètres du capteur et du serveur
SERVER_URL = 'http://localhost:8000/sensor_data/ping'
SENSOR_ID = 'sensor123'
REGISTRATION_KEY = 'your_registration_key'
HOST_NAME = 'localhost'  # Adresse IP du capteur
PORT_NUMBER = 9000  # Port pour le serveur HTTP du capteur


# Simuler les données d'un capteur
def simulate_sensor_data():
    temperature = random.uniform(20.0, 30.0)
    return temperature


# Envoyer les données au serveur
# def send_data_to_server(sensor_data):
#     data = {
#         'sensor_type': 'TEMP',
#         'value': sensor_data,
#         'timestamp': time.time(),
#         'sensor_id': SENSOR_ID,
#         'registration_key': REGISTRATION_KEY
#     }
#     response = requests.post(SERVER_URL, json=data)
#     print("Status Code:", response.status_code)
#     print("Response:", response.json())


# Classe pour gérer les requêtes HTTP (Ping)
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Pong from " + SENSOR_ID, "utf-8"))
        else:
            self.send_error(404)


# Lancer le serveur HTTP dans un thread séparé
def run_server():
    webServer = HTTPServer((HOST_NAME, PORT_NUMBER), MyServer)
    print("Sensor HTTP Server started http://%s:%s/" % (HOST_NAME, PORT_NUMBER))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Sensor HTTP Server stopped.")


# Boucle principale pour envoyer les données du capteur
def main():
    last_data_sent = None

    # Démarrer le serveur HTTP dans un thread séparé
    threading.Thread(target=run_server, daemon=True).start()

    while True:
        current_data = simulate_sensor_data()
        if last_data_sent is None or abs(current_data - last_data_sent) > 0.5:
            # send_data_to_server(current_data)
            last_data_sent = current_data
        time.sleep(60)


if __name__ == '__main__':
    main()
