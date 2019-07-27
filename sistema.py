from parser_entrada import Entrada_dados
from conversor_dados import Conversor



class Transforma_numero_extensao:
    def __init__(self,string):

        self.parser_entrada = Entrada_dados(string)
        self.saida = self.parser_entrada.pega_vetor()
        self.tes_sinal_negativo = self.parser_entrada.get_sinal()

    def get_saida(self):
            if(self.parser_entrada.get_valida()):
                return self._get_texto()
            else:
                return self.saida

    def _get_texto(self):
        recebe = Conversor(self.saida)
        texto = recebe.get_nome_extenso()
        if(self.tes_sinal_negativo):
            texto = "menos {}".format(texto)
        return texto


    
        

