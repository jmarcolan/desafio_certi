# Classe usada para o conversor.
class Conversor:
    def __init__(self,vetor_dados):
        self.compatibilizador =  Arrumando_entrada(vetor_dados)
        self.vetor_dados_compatibilizados = self.compatibilizador.get_lista_valores()
        self.vetor_dados = Vetor_dados(self.vetor_dados_compatibilizados)                           
        self.nome = self.vetor_dados.get_nome()

    def get_nome_extenso(self):
        return self.nome


class Arrumando_entrada():
    def __init__(self,vetor_dados):
        self.vetor_dados = vetor_dados
        self.vetor_dados_saida = self._arrumando_entrada()

    
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




class Vetor_dados():
    # lista de entrada tem que ser ja a lista tratada para o 19
    def __init__(self,list_entrada):
        self.vetor_dados_traduzidos = list_entrada
        self.nova_strutura_dados = self._estrutura_numeros()
        self._get_cases()
        self.conversor = Converte_vetor_string(self)
        self._set_nome()

    def _set_nome(self):
        self.nome = self.conversor.get_nome_extenso()

    def get_nome(self):
        return self.nome
 
    def _get_cases(self):
        
        self.tamanho = len(self.vetor_dados_traduzidos)
        self.tes_tamanho_igual_1= len(self.vetor_dados_traduzidos) == 1
        self.tes_tamanho_igual_2= len(self.vetor_dados_traduzidos) == 2
        self.tes_tamanho_igual_3= len(self.vetor_dados_traduzidos) == 3
        self.tes_tamanho_igual_4 = len(self.vetor_dados_traduzidos) == 4
        # teste case para quando for 5 valores
        self.tes_case_especial_5 = len(self.vetor_dados_traduzidos) == 5


        self.tes_case_mil_mil = self._get_mil_mil()

    # verificar para que o vetor de dados os numeros ja tenham nome
    def _get_mil_mil(self):
        cont = 0
        for valor in self.nova_strutura_dados:
            if valor.teste_e_milhar or valor.teste_milhar or valor.teste_milhar_dezena:
                cont = cont + 1
        if(cont == 2):
            return True
        else:
            return False
        

    def _estrutura_numeros(self):
        nova_strutura_dados =[]
        for dado in self.vetor_dados_traduzidos:
            nova_strutura_dados.append(Numero(dado))
        return nova_strutura_dados


class Converte_vetor_string:
    def __init__(self, vetor_dados):
        self.vetor_dados_objeto = vetor_dados


    def get_nome_extenso(self):
        # funcao a ser usada 
        vetor = self._convert_vetor()
        if(self.vetor_dados_objeto.tes_case_especial_5):
            return "{0} e {1} e {2} e {3} e {4}".format(self._tratar_primeiro_mil(vetor[0]),vetor[1], vetor[2],vetor[3], vetor[4])
                  
        if(self.vetor_dados_objeto.tes_tamanho_igual_4):
            vetor[3] = self._teste_cento(vetor[3])
            return "{0} e {1} e {2} e {3}".format(self._tratar_primeiro_mil(vetor[0]),vetor[1], vetor[2],vetor[3])
            
        if(self.vetor_dados_objeto.tes_tamanho_igual_3):
            vetor[2] = self._teste_cento(vetor[2])
            return "{0} e {1} e {2}".format(self._tratar_primeiro_mil(vetor[0]),vetor[1], vetor[2])
            
        if(self.vetor_dados_objeto.tes_tamanho_igual_2):
            vetor[1] = self._teste_cento(vetor[1])
            return "{0} e {1}".format(self._tratar_primeiro_mil(vetor[0]),vetor[1])
            
        if(self.vetor_dados_objeto.tes_tamanho_igual_1):
            vetor[0] = self._teste_cento(vetor[0])
            return "{}".format(vetor[0])
            

    def _teste_cento(self, string):
        
        test_cento = string == "cento"
        if(test_cento):
            return "cem"
        else:
            return string


    def _tratar_primeiro_mil(self,string):
        if(self.vetor_dados_objeto.tes_case_mil_mil):
            return string.replace(" mil","")
        else:
            return string


    def _convert_vetor(self):
        vetor = self.vetor_dados_objeto.nova_strutura_dados
        vetor_string = []
        for valor in vetor:
            palavra_saida = ""
            if valor.teste_unidade:
                palavra_saida = "{}".format(valor.nome)

            if valor.teste_dezena or valor.teste_centena :
                palavra_saida = "{}".format(valor.nome)

            if valor.teste_milhar or valor.teste_milhar_dezena :
                palavra_saida = "{} mil".format(valor.nome)

            if valor.teste_e_milhar:
                palavra_saida = "mil"


            vetor_string.append(palavra_saida)

        return vetor_string


   
# Classe numero
class Numero():
    
    def __init__(self, numero):
        self.numero = numero
        self._get_qualificador()
        self.conversor = Converte_numero(self)
        self._set_nome()



    def _get_qualificador(self):
        # é o zero
        self.teste_0 = self.numero == 0
        # é a unidade
        self.teste_unidade = self.numero  < 10  # 1
        self.teste_dezena = self.numero  < 100 and not self.teste_unidade  #10
        self.teste_centena = self.numero  < 1000 and not self.teste_dezena and not self.teste_unidade #900
        self.teste_e_milhar = self.numero == 1000
        self.teste_milhar = self.numero  < 10000 and not self.teste_e_milhar and not self.teste_centena and not self.teste_dezena and not self.teste_unidade # 9000
        self.teste_milhar_dezena = self.numero <= 100000 and not self.teste_e_milhar and not self.teste_milhar and not self.teste_centena and not self.teste_dezena and not self.teste_unidade #99000


    #setar o nome do numero 
    def _set_nome(self):
        self.nome = self.conversor.get_nome_extenso()
    
    def get_nome(self):
        return self.nome


class Converte_numero:
    # o numero tem que ser um objeto da classe Numero
    def __init__(self,numero):
        self.dicionario ={
            0:"zero",
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
            100:"cento",
            200:"duzentos",
            300:"trezentos",
            400:"quatrocentos",
            500:"quinhentos",
            600:"seiscentos",
            700:"setecentos",
            800:"oitocentos",
            900:"novecentos",
            1000:""
            }
        self.numero_objeto = numero

    
    # usada para receber valores 
    def get_nome_extenso(self):
        return self._encontra_numero_nome(self.numero_objeto.numero)

    
    def _encontra_numero_nome(self,numero_e):
        # Aqui é numero_e é um valor inteiro
        numero = self._testa_milhar(numero_e)

        # resolvendo o bug do milhar
        return self.dicionario[numero]

    def _testa_milhar(self,valor):
        if self.numero_objeto.teste_milhar_dezena or self.numero_objeto.teste_milhar or self.numero_objeto.teste_e_milhar:
            return int(valor/1000)
        else:
            return valor


