import http.server
import socketserver
import urllib.parse as urlparse
import requests
import json
import time

# Configuración del servidor
PORT = 8000

# Cache para almacenar datos de clima
weather_cache = {}
cache_expiration_time = 300  # 5 minutos

# Servidor HTTP que maneja solicitudes GET
class WeatherRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(parsed_path.query)

        if parsed_path.path == '/weather':
            city = query.get('city', [''])[0]
            if city:
                current_time = time.time()

                # Verifica si hay datos en caché y si no han expirado
                if city in weather_cache and (current_time - weather_cache[city]['timestamp']) < cache_expiration_time:
                    print(f"Datos en caché para {city}.")
                    response_data = weather_cache[city]['data']
                else:
                    api_key = 'f33412b3d42fc6ddac7aeb0e703b960e'  # Reemplaza con tu clave real
                    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es'
                    
                    response = requests.get(url)

                    if response.status_code == 200:
                        weather_data = response.json()
                        temperature = weather_data['main']['temp']
                        weather_description = weather_data['weather'][0]['description']
                        print(f"Datos del clima para {city}: Temperatura = {temperature}, Descripción = {weather_description}")
                        
                        response_data = {
                            "temperature": temperature,
                            "weather": weather_description
                        }

                        # Guardar en caché
                        weather_cache[city] = {
                            'data': response_data,
                            'timestamp': current_time
                        }
                    else:
                        print(f"Error al obtener el clima para {city}: {response.status_code}")
                        self.send_response(404)
                        self.end_headers()
                        self.wfile.write(b'{"error": "Ciudad no encontrada"}')
                        return

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode())
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Falta la ciudad en la consulta"}')
        else:
            super().do_GET()

# Ejecutar el servidor
with socketserver.TCPServer(("", PORT), WeatherRequestHandler) as httpd:
    print(f"Servidor corriendo en el puerto {PORT}")
    httpd.serve_forever()
