from  flask import  Flask, jsonify, request

app = Flask(__name__)

animes = [{
    'id': 1,
    'titulo': 'One Piece',
    'autor': ''
},
    { 'id': 2,
'titulo': 'Naruto',
'autor': ''
},
    {'id': 3,
'titulo': 'Kimetsu no Uaiba',
'autor': ''
}
]

#Consultar (todos)

@app.route('/animes',methods=['GET'])
def obter_animes():
    return jsonify(animes)

#Consultar(id)

@app.route('/animes/<int:id>',methods=['GET'])
def obter_animes_por_id(id):
    for anime in animes:
       if anime.get('id') == id:
           return jsonify(anime)

#Editar

@app.route('/animes/<int:id>',methods=['PUT'])
def editar_anime_por_id(id):
    anime_alterado = request.get_json()
    for indice,anime in enumerate(animes):
        if anime.get('id')== id:
            animes[indice].update(anime_alterado)

#Criar
@app.route('/animes/',methods=['POST'])
def incluir_novo_anime():
    novo_anime = request.get_json()
    animes.append(novo_anime)
    return  jsonify(animes)

#Excluir

@app.route('/animes/<int:id>',methods=['DELETE'])
def excluir_anime(id):
    for indice, anime in enumerate(animes):
        if anime.get('id')== id:
          del animes[indice]

        return jsonify(animes)

app.run(port=5000, host='localhost', debug=True)