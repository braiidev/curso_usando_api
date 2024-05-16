from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)  # Para permitir peticiones en contexto web

@app.get('/api')
def api():
    return jsonify({'message': 'Hola desde la API de Python!'})

if __name__ == "__main__":
    app.run(debug=True)
