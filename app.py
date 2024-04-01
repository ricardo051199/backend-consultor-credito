from flask import Flask, request, jsonify
from flask_cors import CORS
from bayesian_model import modelo, inter, determinar_estados

app = Flask(__name__)
CORS(app)

@app.route('/')
def hola_mundo():
    return jsonify(mensaje="¡Hola desde el backend en Python!")

@app.route('/consultar-credito', methods=['POST'])
def consultar_credito():
    data = request.json
    edad = int(data['edad'])
    estado_hp = int(data['estadoHp'])
    ingresos = float(data['ingresos'])
    deuda = float(data['deuda'])
    cantidad_activos = int(data['cantidadActivos'])

    estado_edad, estado_hp, estado_pb, estado_ingresos, estado_activos = determinar_estados(edad, estado_hp, ingresos,
                                                                                            deuda, cantidad_activos)

    evidencias_c = {'Em': estado_edad, 'Hp': estado_hp}
    evidencias_bif = {'Bi': estado_ingresos, 'Mb': estado_activos}

    resultado_c = inter.query(variables=['C'], evidence=evidencias_c)
    phi_c_estado_1 = resultado_c.values[1]

    estado_c = 1 if phi_c_estado_1 > 0.5 else 0

    resultado_bif = inter.query(variables=['Bif'], evidence=evidencias_bif)
    phi_bif_estado_1 = resultado_bif.values[1]

    estado_bif = 1 if phi_bif_estado_1 > 0.5 else 0

    evidencias_dc = {'Pb': estado_pb, 'C': estado_c, 'Bif': estado_bif}
    resultado_dc = inter.query(['Dc'], evidence=evidencias_dc)
    phi_dc_estado_1 = resultado_dc.values[1]

    resultado = "Tiene derecho a crédito con un " + str(phi_dc_estado_1*100) + "%" if phi_dc_estado_1 > 0.5 else "NO tiene derecho a crédito"

    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
