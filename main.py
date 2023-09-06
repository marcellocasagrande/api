from flask import Flask, request, jsonify

app = Flask(__name__)

carros = [
    {
        'id': 1,
        'marca':'Volkswagen',
        'modelo':'Gol GII',
        'cor':'Prata'
    },
    {
        'id': 2,
        'marca': 'Volkswagen',
        'modelo': 'Gol GIV',
        'cor': 'Prata'
    },
    {
        'id': 3,
        'marca': 'Hyundai',
        'modelo': 'HB20S',
        'cor': 'Prata'
    },
    {
        'id': 4,
        'marca': 'Volkswagen',
        'modelo': 'Virtus',
        'cor': 'Prata'
    },
    {
        'id': 5,
        'marca': 'Volkswagen',
        'modelo': 'Virtus',
        'cor': 'Cinza'
    },
]

# criar a 1ª pagina do site
# rout -> hashtagtreinamentos

@app.route('/')
def homepage():
    return "Esse é meu 1º site. TESTANDO... muito loko"

@app.route('/listacarros',methods=['GET'])
def listacarros():
    return jsonify(carros)

if __name__ == "__main__":
    app.run()