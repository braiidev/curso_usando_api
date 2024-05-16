<picture><img src="https://raw.githubusercontent.com/braiidev/usando_api/main/files/banner-short.png" /></picture>

# Aprende sobre APIs

En este tutorial, aprenderás sobre las APIs, cómo crear una con Flask y consumirla con JavaScript en pocas lineas de código.

## ¿Qué son las APIs?

Las APIs _(Interfaz de Programación de Aplicaciones)_ son como puentes que permiten que diferentes aplicaciones se comuniquen entre sí y compartan información.

### ¿Para qué pueden servir las APIs?

Las APIs son herramientas poderosas que permiten a las aplicaciones:

- Integrar funcionalidades de servicios externos en su propia aplicación.
Automatizar procesos y tareas mediante la comunicación entre diferentes sistemas.
Acceder y manipular datos de servicios web, como redes sociales, bases de datos, y más.

- Construir aplicaciones modulares y escalables al separar la lógica de negocio de la interfaz de usuario.
Fomentar la colaboración y la interoperabilidad entre aplicaciones y plataformas.
### Ejemplos de uso de APIs

Algunos ejemplos comunes de uso de APIs incluyen:

- Integrar el inicio de sesión de una aplicación con Google o Facebook.
Mostrar datos meteorológicos en una aplicación utilizando la API de un servicio meteorológico.
- Obtener información sobre películas o libros utilizando APIs como OMDB o Google Books.
Acceder a datos de redes sociales, como tweets o publicaciones de Facebook, a través de las APIs de Twitter o Facebook.

## Creación de una API con Flask

Instalación de Flask
Antes de comenzar, asegúrate de tener Flask instalado en tu sistema. Puedes instalarlo utilizando pip:

`bash
pip install flask flask_cors
`

## Creación del Servidor API con Flask

Utilizaremos Flask para crear el servidor para nuestra API.

```python
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/api')
def hello_world():
    return jsonify({"message":"Hola desde la API de Python"})

if __name__ == '__main__':
    app.run(debug=True)
```

#### Luego, corremos el servidor en la terminal:

`bash
python3 server.py
`

## Consumiendo la API con JavaScript
#### Con Fetch, podemos enviar una petición a la URL de la API.

```javascript
const $api = document.getElementById("api"); //Recuperamos el elemento html
      const url = "http://localhost:5000/api"; //URL de API
      const options = { //Necesario para una correcta conexión
        method: "GET", // Tipo de petición
        headers: { // Encabezados
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      };
      fetch(url, options) // Realizando Petición
        .then((response) => response.json())
        .then((json) => ($api.textContent = JSON.stringify(json)))
        .catch((err) => console.error("Error:", err));
```
Si la **API** responde la solicitud, nos devolverá un _json_ que vamos a mostrarlo como texto en el elemento con ID **api**, solo con fines prácticos, pero podríamos hacer un sin fin de cosas con ellos.

## Consideraciones sobre CORS
Es importante tener en cuenta el problema de CORS (Cross-Origin Resource Sharing) al consumir APIs desde un origen diferente al de la API. **Pero...**

### ¿Qué es CORS?
CORS (Cross-Origin Resource Sharing) es una regla de seguridad en los navegadores web que decide si permitir o bloquear solicitudes entre diferentes sitios web. Ayuda a prevenir que páginas web maliciosas accedan a tus datos personales cuando navegas por internet.


## Capturas de pantalla

#### Vista de código Python
<picture><img src="https://raw.githubusercontent.com/braiidev/usando_api/main/files/python-api.jpg" /></picture>

#### Vista de código Javascript dentro de un HTML
<picture><img src="https://raw.githubusercontent.com/braiidev/usando_api/main/files/javascript-api.jpg" /></picture>

#### Vista previa sin realizar petición
<picture><img src="https://raw.githubusercontent.com/braiidev/usando_api/main/files/before.jpg" /></picture>

#### Vista previa luego de la petición
<picture><img src="https://raw.githubusercontent.com/braiidev/usando_api/main/files/after.jpg" /></picture>


---

### TODO:

- [x] Subir imagenes
- [x] Crear API
- [ ] Uso real de API
- [ ] Screenshots de uso real de API

---

<picture><img src="https://raw.githubusercontent.com/braiidev/braiidev/main/files/banner-short.jpg" /></picture>

