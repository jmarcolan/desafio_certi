

class Validando_entrada:
    def __init__(self,string):
        self.string_entrada = string
        
        self._validando()


    def _validando(self):
        pass
        # noa pode ter letra
        # nao pode estar fora do range
        # nao pode ser numero fracionado
        # nao pode ser um valor vazio
        # retorna um boleano

class Envio_resposta_json():
    # classe quie sera usadao para configurar o texto de saida.
    pass



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
        