import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

# Paramètres du serveur
HOST_NAME = 'localhost'
PORT_NUMBER = 8445
KEY = "Aa1234512345"


# Fonctions de simulation pour chaque type de capteur
def simulate_temperature():
    return random.uniform(20.0, 30.0)


def simulate_humidity():
    return random.uniform(30.0, 50.0)


def simulate_luminosity():
    return random.uniform(300.0, 800.0)


# Classe pour gérer les requêtes HTTP
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sensor_types = ['temperature', 'humidity', 'luminosity']
            self.wfile.write(bytes(json.dumps(sensor_types), "utf-8"))
        elif self.path == '/sensors':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sensor_data = {
                'temperature': simulate_temperature(),
                'humidity': simulate_humidity(),
                'luminosity': simulate_luminosity()
            }
            self.wfile.write(bytes(json.dumps(sensor_data), "utf-8"))
        else:
            self.send_error(404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Obtient la taille du corps
        post_data = self.rfile.read(content_length)  # Lit les données du corps
        data = json.loads(post_data)

        if self.path == '/ping':
            received_key = data.get('key', '')
            if received_key == KEY:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("Pong from sensor", "utf-8"))
            else:
                self.send_response(403)  # Accès refusé si la clé ne correspond pas
                self.end_headers()
                sensor_types = ['temperature', 'humidity', 'luminosity']
                self.wfile.write(bytes(json.dumps(sensor_types), "utf-8"))
        else:
            self.send_error(404)  # Gérer les autres chemins


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


# Point d'entrée principal
if __name__ == '__main__':
    run_server()
    # threading.Thread(target=run_server, daemon=True).start()
