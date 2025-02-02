from flask import Flask, request, jsonify
from flask_cors import CORS  # Si tienes problemas de CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Factores de conversión (unidades base: metros para longitud, gramos para peso)
converter = {
    "length": {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    },
    "weight": {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592
    }
}

@app.route('/convert', methods=['POST'])
def handle_convert():
    data = request.get_json()
    print("Datos recibidos:", data) # Para depuración
    type_ = data['type']
    value = data['value']
    from_unit = data['from']
    to_unit = data['to']

    try:
        # Conversión de temperatura (fórmulas específicas)
        if type_ == "temperature":
            if from_unit == "C":
                if to_unit == "F":
                    result = (value * 9/5) + 32
                elif to_unit == "K":
                    result = value + 273.15
                else:
                    result = value  # Misma unidad
            elif from_unit == "F":
                if to_unit == "C":
                    result = (value - 32) * 5/9
                elif to_unit == "K":
                    result = (value - 32) * 5/9 + 273.15
                else:
                    result = value
            elif from_unit == "K":
                if to_unit == "C":
                    result = value - 273.15
                elif to_unit == "F":
                    result = (value - 273.15) * 9/5 + 32
                else:
                    result = value
        else:
            # Conversión para longitud y peso
            factor_from = converter[type_][from_unit]
            factor_to = converter[type_][to_unit]
            result = value * factor_from / factor_to

        return jsonify({ "result": result })

    except KeyError:
        return jsonify({ "error": "Unidades no válidas" }), 400
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

if __name__ == '__main__':
    app.run(debug=True)