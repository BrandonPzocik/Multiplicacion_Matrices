from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='public')

CORS(app)  # Habilitar CORS

# Ruta para servir el index.html desde la carpeta "public"
@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'public'), 'index.html')

# Ruta para multiplicar matrices
@app.route('/multiplicar', methods=['POST'])
def multiplicar_matrices():
    data = request.get_json()
    matriz1 = data['matriz1']
    matriz2 = data['matriz2']

    # Lógica para multiplicar las matrices
    resultado = multiplicar(matriz1, matriz2)
    return jsonify({'resultado': resultado})

# Lógica para multiplicar las matrices
def multiplicar(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])

    # Verificar si las matrices se pueden multiplicar
    if columnas1 != filas2:
        raise ValueError("Las matrices no se pueden multiplicar debido a sus dimensiones.")

    # Inicializamos la matriz de resultados
    resultado = [[0] * columnas2 for _ in range(filas1)]

    for i in range(filas1):
        for j in range(columnas2):
            for k in range(columnas1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

if __name__ == '__main__':
    app.run(debug=True)
