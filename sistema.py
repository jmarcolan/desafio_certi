from parser_entrada import Entrada_dados
from conversor_dados import Conversor

class Transforma_numero_extensao:
    def __init__(self,string):

        self.parser_entrada = Entrada_dados(string)
        self.saida = self.parser_entrada.pega_vetor()

    def get_saida(self):
        if(self.parser_entrada.get_valida()):
            recebe = Conversor(self.saida)
            return recebe.get_nome_extenso()
        else:
            return self.saida
        

