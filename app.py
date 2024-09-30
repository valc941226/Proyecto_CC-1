from flask import Flask, render_template, request, jsonify
import requests
import json

from flask import Flask, render_template, request
from helpers.utils import cambiar_a_mayusculas, call_predict_function  # Importamos la función que cambiará a mayúsculas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    user_input = data.get('text_input', '')

    # Convertimos el input a mayúsculas usando la función cambiar_a_mayusculas
    # respuesta_cf = cambiar_a_mayusculas(user_input)
    respuesta_cf = call_predict_function(user_input)


    # Return the processed result as JSON
    return jsonify({'result': respuesta_cf})

if __name__ == '__main__':
    app.run(debug=True)
