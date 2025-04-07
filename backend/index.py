from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.CreateFile import CreateFile
from controller.MangaApiClient import MangaApiClient

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "API está rodandokkk!"})

@app.route('/get-mangas')
def getManga():
    manga = request.args.get('manga')
    offset = request.args.get('offset')
    
    if not manga:
        return {"error": "Mangá não especificado"}, 404
    
    result = MangaApiClient.getManga(manga, offset)
    return jsonify(result)

@app.route('/get-manga-chapters')
def getMangaChapters():
    idManga = request.args.get('idManga')
    offset = request.args.get('offset')
    
    if not idManga:
        return {"error": "Mangá não especificado"}, 404
    
    result = MangaApiClient.getMangaList(idManga, offset)
    return jsonify(result)

@app.route('/pdf-manga-chapter')
def pdfDownloadMangaChapters():
    idManga = request.args.get('idManga')
        
    if not idManga:
        return {"error": "Mangá não especificado"}, 404
    
    result = CreateFile.pdfGenerator(idManga)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    