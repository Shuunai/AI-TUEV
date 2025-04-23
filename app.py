from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

# Dummy AI-Analyse (nur zur Demo – kann später durch echtes Modell ersetzt werden)
def analyze_image(image):
    avg_brightness = image.convert("L").resize((50, 50)).getdata()
    brightness = sum(avg_brightness) / len(avg_brightness)
    if brightness < 50:
        return "Möglicherweise Rost oder starke Verschmutzung – check das mal!"
    return "Sieht gut aus – kein offensichtliches Problem."

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'Kein Bild gefunden.'}), 400
    file = request.files['file']
    image = Image.open(file.stream)
    result = analyze_image(image)
    return jsonify({'diagnose': result})

@app.route('/', methods=['GET'])
def index():
    return "AI TÜV-Check Backend läuft!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
