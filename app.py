from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__)

# URL de l'API pour les incubateurs et accélérateurs de start-up en Île-de-France
API_URL = "https://data.iledefrance.fr/api/records/1.0/search/?dataset=incubateurs-accelerateurs&q=&rows=20"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/startup')
def api_startup():
    try:
        response = requests.get(API_URL)
        data = response.json()
        records = data.get('records', [])

        if records:
            # Sélectionner un enregistrement aléatoire
            random_record = random.choice(records)['fields']
            result = {
                "nom": random_record.get("nom", "N/A"),
                "description": random_record.get("description", "N/A"),
                "financement": random_record.get("financement", "N/A"),
                "partenaires": random_record.get("partenaires", "N/A")
            }
        else:
            result = {
                "nom": "N/A",
                "description": "N/A",
                "financement": "N/A",
                "partenaires": "N/A"
            }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/advice')
def api_advice():
    # Liste des conseils d'investissement
    advices = [
        "L'investissement peut-être prometteur.",
        "Probabilité de retour sur investissement faible."
    ]
    # Sélectionner un conseil aléatoire
    advice = random.choice(advices)
    return jsonify({"advice": advice})

if __name__ == '__main__':
    app.run(debug=True)
