from flask import Flask, request, jsonify
from flask_cors import CORS
from bayesian_model import inter, determinar_estados

app = Flask(__name__)
CORS(app)

@app.route('/')
def hola_mundo():
    return jsonify(mensaje="¡Hola desde el backend en Python!")

@app.route('/consultar-credito', methods=['POST'])
def consultar_credito():
    data = request.json
    edad, estado_hp, ingresos, deuda, cantidad_activos = map(int, (data['edad'], data['estadoHp'], data['ingresos'], data['deuda'], data['cantidadActivos']))
    estado_edad = 1 if edad > 30 else 0
    estado_pb = 1 if deuda / ingresos < 1 else 0
    estado_ingresos = 1 if ingresos > 5000 else 0
    estado_activos = 1 if cantidad_activos > 40 else 0
    evidencias_c = {'Em': estado_edad, 'Hp': estado_hp}
    evidencias_bif = {'Bi': estado_ingresos, 'Mb': estado_activos}
    resultado_c = inter.query(variables=['C'], evidence=evidencias_c)
    estado_c = 1 if resultado_c.values[1] > 0.5 else 0
    resultado_bif = inter.query(variables=['Bif'], evidence=evidencias_bif)
    estado_bif = 1 if resultado_bif.values[1] > 0.5 else 0
    evidencias_dc = {'Pb': estado_pb, 'C': estado_c, 'Bif': estado_bif}
    resultado_dc = inter.query(['Dc'], evidence=evidencias_dc)
    phi_dc_estado_1 = resultado_dc.values[1]
    resultado = "Tiene derecho a crédito con un {}%".format(phi_dc_estado_1*100) if phi_dc_estado_1 > 0.5 else "NO tiene derecho a crédito"
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
