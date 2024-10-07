from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir peticiones desde el frontend

@app.route('/procesar_texto', methods=['POST'])
def procesar_texto():
    data = request.json
    texto = data.get('texto')
    
    # Aquí puedes realizar el procesamiento que necesites con el texto
    respuesta = f"Procesaste: {texto}"
    
    return jsonify({'respuesta': respuesta})

if __name__ == "__main__":
    app.run(debug=True)
