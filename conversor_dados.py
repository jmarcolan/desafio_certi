class Converte_numero:
    def __init__(self,vetor_dados):
        self.dicionario ={
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
            200:"duzentos",
            300:"trezentos",
            400:"quatrocentos",
            500:"quatrocentos",
            600:"quatrocentos",
            700:"quatrocentos",
            800:"quatrocentos",
            900:"quatrocentos",
            1000:"mil"
            }

        self.parser_entrada = Arrumando_entrada(vetor_dados)
        
        self.list_entrada = self.parser_entrada.get_lista_valores()

    def get_valor_por_extenso(self):
        pass


    # fazer algumas proteções para casa o valor nao tenha no dicionario
    # tem que assegurar que o numero seja um inteiro
    def _converte_numero(self,numero):
        return self.dicionario[numero]
    

  
    def _cria_lista_nomes(self):
        list_nomes = []
        for numero_entrada in self.list_entrada:
            teste_milhar = numero_entrada > 1000 and numero_entrada < 10000
            teste_milhar_dezena = numero_entrada >= 10000

            if teste_milhar:
                numero = int(numero_entrada/100)
            
            if teste_milhar_dezena:
                numero = int(numero_entrada/1000)
            
            if not teste_milhar and not teste_milhar_dezena:
                numero = numero_entrada
        

            list_nomes.append(
                {"num_s":numero_entrada,
                 "num_ext":self._converte_numero(numero)})
                
        return list_nomes
        




class Arrumando_entrada():
    def __init__(self,vetor_dados):
        self.vetor_dados = vetor_dados
        self.vetor_dados_saida = self._arrumando_entrada()

    
    #  unica funcao que é necessaria saber para usar a classe.
    def get_lista_valores(self):
        return self.vetor_dados_saida


    
    def _inverte_a_lista(self):
        list_invertida = list(reversed(self.vetor_dados))
        return list_invertida


    
    def _encontrando_posicao_critica(self):
        self.list_invertida = self._inverte_a_lista()

        # self.list_invertida = list(reversed(self.vetor_dados))
        pos_critica = []
        regra_tamanho_3 = len(self.list_invertida) >= 2
        regra_tamanho_5 = len(self.list_invertida) >= 5

        if regra_tamanho_3:
            pos_critica.append(1)
        
        if regra_tamanho_5:
            pos_critica.append(4)

        return pos_critica



    def _teste_posicao_critic(self,i):
        for cont,critica in enumerate(self.pos_critica):
                if i == critica:
                    return self._testando_se_aconteceu_exececao(cont)
        return False

    def _testando_se_aconteceu_exececao(self,cont):
        return self.excecoes[cont]



    def concerta_vetor(self,saida,valor,i):
        saida.pop(len(saida)-1) #tirando o ultimo valor da lista
        valor_1 = self.list_invertida[i] + self.list_invertida[i-1]
        saida.append(valor_1)


    def _arrumando_entrada(self):
        self.pos_critica = self._encontrando_posicao_critica()
        self.excecoes = self._testando_regra_excecao()
        

        saida = []
        for i,valor in enumerate(self.list_invertida):
            if self._teste_posicao_critic(i):
                self.concerta_vetor(saida,valor,i)
            else:
                saida.append(valor)

        return list(reversed(saida))

    def _testando_regra_excecao(self):
        self.pos_critica = self._encontrando_posicao_critica()

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


