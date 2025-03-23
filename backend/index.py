from flask import Flask, jsonify, request
from controller.CreateFile import CreateFile
from controller.MangaApiClient import MangaApiClient

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return jsonify({"message": "API está rodandokkk!"})

@app.route('/get-mangas')
def getManga():
    manga = request.args.get('manga')
    if not manga:
        return {"error": "Mangá não especificado"}, 400
    return MangaApiClient.getManga(manga)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)