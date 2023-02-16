import numpy as np
import pickle, json
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)
@app.route('/api/getScore', methods=['Get'])
def score():
    try: # намагаємося зчитати дані з json
        features = request.get_json()
    except:
        return jsonify(message="Reading json error"), 422

    try:  
        pred_proba = 0.99
        pred_class = 1
        return jsonify({"proba": round(pred_proba, 4),
                        "class": int(pred_class)
                        }), 200
    except:
        return jsonify(message="Predict error"), 500


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=80)
    serve(app, host="0.0.0.0", port=443)
