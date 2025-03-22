from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return jsonify({"message": "API está rodando!"})

@app.route('/teste')
def caralho():
    return jsonify({"message": "Caralho mano que sonho!"})

@app.route('/ccc')
def ccc():
    return jsonify({"message": "ccca"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
