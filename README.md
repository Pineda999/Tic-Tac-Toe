## 🎮 Tic Tac Toe (Tres en Raya)

Un juego clásico de **Tic Tac Toe (Tres en Raya)** desarrollado con **Django** y **JavaScript**.  
El jugador se enfrenta a la máquina, que realiza movimientos aleatorios controlados desde el backend.  

---

## 🧠 Descripción del proyecto

El juego muestra un tablero interactivo donde el jugador selecciona su casilla y la máquina responde automáticamente.  
Incluye detección de ganador, control de empate y mensajes visuales usando **SweetAlert2**.

Este proyecto fue creado con fines de práctica para fortalecer conocimientos en:

- Comunicación entre **frontend (JavaScript)** y **backend (Django)**
- Uso de **fetch** para enviar datos al servidor
- Control de flujo del juego entre cliente y servidor
- Uso de **POO** y separación lógica en controladores Python

---

## ⚙️ Tecnologías utilizadas 

| Tipo | Herramientas |
|------|---------------|
| Backend | Django (Python) |
| Frontend | HTML, CSS, JavaScript |
| Estilos visuales | SweetAlert2 |
| Control del juego | Python (controladores personalizados) |

---

## 🚀 Funcionalidades principales

- ✅ Detección automática de ganador o empate  
- ✅ Bloqueo de casillas tras terminar el juego  
- ✅ Reinicio rápido de la partida  
- ✅ IA básica con movimientos aleatorios  
- ✅ Mensajes visuales con animaciones  
- ✅ Interfaz adaptable y moderna  

---

## 🗂️ Estructura del proyecto
tictactoe/
│
├── controller/
│ ├── custom_tags.py # Filtros personalizados para plantillas Django
│ ├── tablaJuego.py # Lógica principal del tablero
│ └── numeroAleatorio.py # Generación de jugadas aleatorias
│
├── static/
│ ├── js/
│ │ ├── tabla.js # Control de botones y turnos
│ │ └── estiloAlert.js # Estilo de alertas con SweetAlert2
│ └── imagenes/
│ └── cat2.gif # Imagen decorativa para SweetAlert
│
├── templates/
│ └── juego.html # Interfaz principal del juego
│
├── tictactoe/
│ ├── views.py # Control de peticiones y respuestas JSON
│ └── urls.py # Rutas de acceso
│
└── manage.py

---

## 🕹️ Cómo ejecutar el proyecto

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/tuusuario/tictactoe.git
   
2. **Entra al directorio del proyecto:**
   ```bash
   cd tictactoe

3.**Instala las dependencias:**
   ```bash
   pip install django
  
4.**Ejecuta el servidor de desarrollo:**
   bash
   python manage.py runserver
  
5.**Abre tu navegador y visita:**
   cpp
   http://127.0.0.1:8000/

👨‍💻 Autor
**Desarrollado por:** Pineda999
💬 Proyecto educativo y de práctica con Django + JavaScript.

🏷️ Licencia
Este proyecto se distribuye bajo la licencia MIT.
Puedes usarlo y modificarlo libremente con fines educativos o personales.

