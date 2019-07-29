""" Módulo responsável por unir as classes criadas. Isso foi feito para que fique fácil o úso da funcionalidade de conversão dos numeros para sua forma por extenso.

Example:
    Um exemplo de como usar a classe é:
    literal blocks::
        >>> teste = "-29319" # palavra de entrada
        >>> recebe = Transforma_numero_extensao(teste)

        >>> vetor_palavras = recebe.get_saida()

Todo:
    * Ver notas dentro das classes.

"""


from parser_entrada import Entrada_dados
from conversor_dados import Conversor



class Transforma_numero_extensao:
    """Converte um numero inteiro, que esteja dentro do intervalo de -99999 até 99999, para sua verão por extenso. 
    """
    def __init__(self,string):
        """Método inicializador
        Args:
            string (str): Um numero, no formato de stringm que pode estar entre o intervalo de -99999 até 99999.
        """
    
        self.parser_entrada = Entrada_dados(string)
        self.saida = self.parser_entrada.pega_vetor()
        self.tes_sinal_negativo = self.parser_entrada.get_sinal()

    def get_saida(self):
        """Pega valor por extenso.
        Returns:
            str: Retorna o valor por extenso do numero informado.
        
        """
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


    
        

