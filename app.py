from flask import Flask, request, jsonify
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from flask_cors import CORS

app = Flask(__name__)
CORS(app)





@app.route('/')
def hola_mundo():
    return jsonify(mensaje="¡Hola desde el backend en Python!")

@app.route('/modelo-black-scholes', methods=['POST'])
def calcular_black_scholes():
    try:
        data = request.get_json()
        edad = float(data.get['edad'])
        estado_hp = float(data.get['estadoHp'])
        ingresos = float(data.get['ingresos'])
        deuda = float(data.get['deuda'])
        cantidad_activos = float(data.get['cantidadActivos'])
        
        return jsonify(resultado='Resultado')
    except ValueError:
        return jsonify(error="Los datos proporcionados no son válidos"), 400

if __name__ == '__main__':
    app.run(debug=True)
