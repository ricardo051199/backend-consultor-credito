from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hola_mundo():
    return jsonify(mensaje="¡Hola desde el backend en Python!")

if __name__ == '__main__':
    app.run(debug=True)
