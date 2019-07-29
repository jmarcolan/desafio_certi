""" Módulo responsável por criar o servidor HTTTP.
Example:
    Para rodar o módulo, tenha instalado o Python 3.5, abra um termina direciona a essa parte e digite:
    literal blocks::
        $ python -m pip install -r requirements.txt
    
    Após realizar a instalação das dependencias do projeto digite:
    literal blocks::
        $ python servidor.py

Todo:
    * Ver notas dentro das classes.

"""


from sistema import Transforma_numero_extensao

from flask import Flask
# from flask import jsonify
import json

import os
app = Flask(__name__)

class Saida_Desafio_Certi:
    """Adequa o sistema para a saída experada pelo pessoal da CERTI.
    """
    def __init__(self,string):
        """ Método inicializador
        Args:
            string (str): Uma string que contenha um numero para ser convertido para sua forma por extensa. 
        """
        self.transformador = Transforma_numero_extensao(string)
        self.texto_extenso = self.transformador .get_saida()  

    def saida(self):
        """Pega a saida adequa e experada pelo pessoal da CERTI.
        """
        return json.dumps({"extenso" :self.texto_extenso})
        
        # return jsonify(extenso=self.texto_extenso)

# Como é uma API seria interessante na URN ter o versionamento (e.g., /v1/<string_entrada>)
@app.route("/<string_entrada>")
def hello1(string_entrada):
    saida_extenso  = Saida_Desafio_Certi(string_entrada)
    return saida_extenso.saida()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host= '0.0.0.0', port=port)



