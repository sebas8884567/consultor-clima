Descripción
Consultor de Clima es una aplicación web simple que permite a los usuarios obtener la temperatura y el estado del clima actual de cualquier ciudad del mundo.
Los usuarios pueden ingresar el nombre de una ciudad, y la aplicación mostrará la temperatura y la descripción del clima utilizando datos de una API externa de clima.

Funcionalidades
Autocompletado de nombres de ciudades.
Consulta de la temperatura y estado del clima en tiempo real.
Visualización de los datos del clima en una interfaz sencilla y amigable.
Capturas de pantalla
Aquí puedes incluir capturas de pantalla de la interfaz de la aplicación para mostrar cómo se ve.

Tecnologías utilizadas
HTML5: Estructura de la página web.
CSS3: Estilizado de la interfaz.
JavaScript: Lógica del autocompletado y manejo de la API de clima.
Python (Flask): Lado del servidor para la comunicación con la API de clima.
Git: Control de versiones del proyecto.

Estructura del Proyecto

├── cliente.html          # Archivo HTML principal
├── servidor.py           # Script de servidor en Python
├── styles.css            # Archivo de estilos CSS
├── cities.json           # Lista de ciudades para el autocompletado
└── README.md             # Documentación del proyecto


Instalación
Clona el repositorio en tu máquina local:
*git clone https://github.com/sebas8884567/consultor-clima.git
Navega al directorio del proyecto:
*cd consultor-clima
Asegúrate de tener Python , requests y Flask instalados. Si no, puedes instalarlos con:
pip install Flask
pip install requests

Ejecuta el servidor:
python servidor.py
Abre el archivo cliente.html en tu navegador web para usar la aplicación.
*http://localhost:8000/cliente.html

Uso
Ingresa el nombre de una ciudad en el campo de búsqueda.
Selecciona una ciudad de las sugerencias que aparecen.
Haz clic en el botón de "Consultar" para ver la temperatura y el clima actual.
