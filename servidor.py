from sistema import Transforma_numero_extensao

from flask import Flask
# from flask import jsonify
import json

import os
app = Flask(__name__)

class Saida_Desafio_Certi:
    def __init__(self,string):
        self.transformador = Transforma_numero_extensao(string)
        self.texto_extenso = self.transformador .get_saida()  

    def saida(self):
        return json.dumps({"extenso" :self.texto_extenso})
        
        # return jsonify(extenso=self.texto_extenso)

@app.route("/<string_entrada>")
def hello1(string_entrada):
    saida_extenso  = Saida_Desafio_Certi(string_entrada)
    return saida_extenso.saida()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host= '0.0.0.0', port=port)



