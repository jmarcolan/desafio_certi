import re


class Entrada_dados:
    def __init__(self, string_entrada):
        self.string_entrada = string_entrada
        # pega a entrada e valida,
        self.validador = Validando_entrada(self.string_entrada)

    def get_valida(self):
        return self.validador.get_test_valido()
        
    def pega_vetor(self):
        if self.validador.get_test_valido():
            string = self.validador.get_string_valida()
            return self._get_entrada(string)
        
        else:
            # se nao for valida vai voltar a e strign q nao é valida
            return self.validador.get_string_valida()
    
    # necessita refatorar tem 2 responsabilidade
    def _get_entrada(self,string):
        parser_entrada = Parser_entrada(string)
        self.test_sinal_negativo = parser_entrada.get_sinal()
        return parser_entrada.get_vetor_tratado()
        
    
            



class Validando_entrada:
    def __init__(self,string):
        self.string_entrada = string
        
       
    def get_test_valido(self):
        return self._testa_numero_valido()
      

    # tou setando que não é valido valor +++999
    def get_string_valida(self):
        # se for um sinal positivo na frente
        if self._testa_sinal_positivo() :
            if self._testa_numero_valido() :
                return self.string_entrada[1:len(self.string_entrada)]
            else:
                return "nao é uma entrada valida"
        else:
            if self._testa_numero_valido() :
                return self.string_entrada
            else:
                return "nao é uma entrada valida"
        


    def _testa_numero_valido(self):
        # referencias
        # https://stackoverflow.com/questions/8586346/python-regex-for-integer/8586432
        # https://docs.python.org/3/howto/regex.html
        # https://stackoverflow.com/questions/1649435/regular-expression-to-limit-number-of-characters-to-10
        # testa para ter os simbolos +-
        # os numeros podem variarar de 0 a 9
        # pode ter de 1 a 5 numeros
        testador_valida_entrada = re.compile("^[-+]?[0-9]{1,5}$")

        if None != testador_valida_entrada.match(self.string_entrada):
            return True
        else: 
            return False


    def _testa_sinal_positivo(self):
        # testa se tem exatamente 1 +
        test_sinal_positivo = re.compile("^[+][0-9]{1,5}$")

        if None != test_sinal_positivo.match(self.string_entrada):
            return True
        else: 
            return False
        
        # noa pode ter letra
        # nao pode estar fora do range
        # nao pode ser numero fracionado
        # nao pode ser um valor vazio
        # retorna um boleano


class Parser_entrada:
    def __init__(self, string):
        self.string_entrada = string
        self._sinal_negativo = self._detecta_sinal()
        self.test_zero = self._detecta_zero()
        self.vetor_nao_tratado = self._trata_sinal_entrada()
        self._vetor_dezena = self._gera_desena()

        self._vetor_tratado_saida = self._trata_vetor_desena()

    def get_vetor_tratado(self):
        return self._vetor_tratado_saida

    def get_sinal(self):
        return self._sinal_negativo

    def _detecta_zero(self):
        numero = int(self.string_entrada)
        return numero == 0

    def _detecta_sinal(self):
        # detecta sinal
        numero = int(self.string_entrada)
        test_positivo_zero = numero >= 0
        test_negativo = numero < 0

        if test_positivo_zero:
            return False
        if test_negativo:
            return True
    
    def _trata_sinal_entrada(self):
        
        vetor = list(self.string_entrada)
        if self._sinal_negativo:
            del vetor[0]

        result = list(map(lambda x: int(x), vetor))
        
        return result

    def _gera_desena(self):
        # vetor = list(reversed(self.vetor_nao_tratado))

        vetor = []
        for i,valor in enumerate(reversed(self.vetor_nao_tratado)):
            valor = valor * (10 ** i)
            vetor.append(valor)
        
        veto_1_s = list(reversed(vetor))

        return veto_1_s

    def _trata_vetor_desena(self):
        if self.test_zero :
            return [0]
        else:
            vetor_s=[]
            for i,valor in enumerate(self._vetor_dezena):
                tes_0 = valor == 0
                if not tes_0:
                    vetor_s.append(valor)



        return vetor_s


        

    # def conver_valor(self,valor):
    #     self._convertendo_entrada(valor)

    # def _convertendo_entrada(self,valor):
    #     vetor_unidade = self._arrumando_entrada(valor)

    # def _arrumando_entrada(self,valor):
    #     arra = []
    #     for a in valor:
    #         arra.append(a)
    #     return arra
        