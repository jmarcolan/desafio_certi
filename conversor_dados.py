class Converte_numero:
    def __init__(self):
        self.dicionario={
            1:"um",
            2:"dois",
            3:"tres",
            4:"quatro",
            5:"cinco",
            6:"seis",
            7:"sete",
            8:"ointo",
            9:"nove",
            10:"dez",
            11:"onze",
            12:"doze",
            13:"treze",
            14:"quatorze",
            15:"quinze",
            16:"dezeseis",
            17:"dezesete",
            18:"dezoito",
            19:"dezenove",
            20:"vinte",
            30:"trinta",
            40:"quarenta",
            50:"cinquenta",
            60:"sessenta",
            70:"setenta",
            80:"oitenta",
            90:"noventa",
            100:"cem",
            200:"duzento",
            300:"trezentos",
            400:"quatrocentos",
            500:"quatrocentos",
            600:"quatrocentos",
            700:"quatrocentos",
            800:"quatrocentos",
            900:"quatrocentos",
            1000:"mil"
            }
        
 
    def ret_valor(self,valor):
        self._convertendo_entrada(valor)
        

    def _convertendo_entrada(self,valor):
        vetor_unidade = self._arrumando_entrada(valor)

        # print(self.unidade[valor])

    def _arrumando_entrada(self,valor):
        arra = []
        for a in valor:
            arra.append(a)
        return arra



class Arrumando_entrada():
    def __init__(self,vetor_dados):
        self.vetor_dados = vetor_dados

        self.pos_critica = self._encontrando_posicao_critica()

        self.vetor_dados_saida = []

    
    def _inverte_a_lista(self):
        list_invertida = list(reversed(self.vetor_dados))
        return list_invertida


    
    def _encontrando_posicao_critica(self):
        self.list_invertida = self._inverte_a_lista()

        self.list_invertida = list(reversed(self.vetor_dados))
        pos_critica = []
        regra_tamanho_3 = len(self.list_invertida) >= 2
        regra_tamanho_5 = len(self.list_invertida) >= 5

        if regra_tamanho_3:
            pos_critica.append(1)
        
        if regra_tamanho_5:
            pos_critica.append(4)

        return pos_critica

    def _testando_regra_excecao(self):

        resul_regra = []
        for pos_critica in self.pos_critica:
            regra_milhar = self.list_invertida[pos_critica] >= 10000

            if regra_milhar:
                valor_teste = int(self.list_invertida[pos_critica] /1000) #forcando ser inteiro
            else:
                valor_teste = self.list_invertida[pos_critica]


                
            regra = valor_teste < 20
            resul_regra.append(regra)
        
        return resul_regra






