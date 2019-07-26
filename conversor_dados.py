class Vetor_dados():
    def __init__(self, vetor_dados,list_entrada):
        self.vetor_dados_originais = vetor_dados
        self.vetor_dados_traduzidos = list_entrada

        self.nova_strutura_dados = self._estrutura_numeros()
        self._get_cases()

        
    def _get_cases(self):
        
        self.tamanho = len(self.vetor_dados_traduzidos)

        self.tes_tamanho_igual_1= len(self.vetor_dados_traduzidos) == 1
        self.tes_tamanho_igual_2= len(self.vetor_dados_traduzidos) == 2
        self.tes_tamanho_igual_3= len(self.vetor_dados_traduzidos) == 3
        self.tes_tamanho_igual_4 = len(self.vetor_dados_traduzidos) == 4
        # teste case para quando for 5 valores
        self.tes_case_especial_5 = len(self.vetor_dados_traduzidos) == 5

        # teste case para quando aconteceu alguma execao no vetor, 19,18
        self.tes_case_especial_19 = len(self.vetor_dados_originais) > len(self.vetor_dados_traduzidos)

        # teste case para quando so vem um numero
        self.test_case_especial_1 = len(self.vetor_dados_originais)  == 1 


        self.tes_case_mil_mil = self._get_mil_mil()
        
        # preciso escrever a conversao para ter certeza disso.
        # teste case se tem algum vetor zerado
        self.tes_case_especial_0 = self._vetor_tem_zero()

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

    # olhar pq nao usa as propiedades da classe Numero
    def _vetor_tem_zero(self):
        for elemento in self.vetor_dados_originais:
            if elemento == 0:
                return True
            
        return False
    
    def set_nome(self,nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

   

class Numero():
    def __init__(self, numero):
        self.numero = numero
        self._get_qualificador()

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
    def set_nome(self, nome_string):
        self.nome = nome_string


class Recebendo_dados:
    def __init__(self,vetor_dados):
        self.parser_entrada = Arrumando_entrada(vetor_dados)     
        self.list_entrada = self.parser_entrada.get_lista_valores()
        self.vetor_dados = Vetor_dados(self.parser_entrada.vetor_dados,self.list_entrada)

        self.valores_convertidos = Converte_numero(self.vetor_dados)
        vetor_dados = self.valores_convertidos._get_vetor()
        self.valores_convertidos_vetor = Converte_vetor_string(self.vetor_dados)

 

class Converte_numero:
    def __init__(self,vetor_dados):
        self.dicionario ={
            0:"",
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
            1000:"mil"
            }
        self.vetor_dados = vetor_dados

    
    # usada para receber valores 
    def _get_vetor(self):
        vetor = self.vetor_dados.nova_strutura_dados
        vetor_nome = []
        for valor in vetor:
            valor.set_nome(self._get_numero_nome(valor))
            vetor_nome.append(valor)
        
        # self.vetor_dados.nova_strutura_dados = vetor_nome
        return vetor_nome

    
    def _get_numero_nome(self,valor):
        numero = self._testa_milhar(valor)
        return self.dicionario[numero]

    def _testa_milhar(self,valor):
        numero_entrada = valor.numero
        if valor.teste_milhar_dezena or valor.teste_milhar or valor.teste_e_milhar:
            return int(numero_entrada/1000)
        else:
            return numero_entrada

    def _caminho_minimo(self):
        pass



class Converte_vetor_string:
    def __init__(self, vetor_dados):
        self.vetor_dados = vetor_dados


    def _tratar_primeiro_mil(self,string):
        if(self.vetor_dados.tes_case_mil_mil):
            return string.replace(" mil","")
        else:
            return string
    
    def _deci_de_vetor(self,vetor):
        if(self.vetor_dados.tes_case_especial_5):
            nome = "{0} e {1} e {2} e {3} e {4}".format(self._tratar_primeiro_mil(vetor[0]),vetor[1], vetor[2],vetor[3], vetor[4])
            self.vetor_dados.set_nome(nome)
           
            
        if(self.vetor_dados.tes_tamanho_igual_4):
            # alguma vezes aparece o mil mil seguido
            nome = "{0} e {1} e {2} e {3}".format(self._tratar_primeiro_mil(vetor[0]),vetor[1], vetor[2],vetor[3])
            self.vetor_dados.set_nome(nome)
            
        
        if(self.vetor_dados.tes_tamanho_igual_3):
            # encontrar se ocorre o problema
            nome = "{} e {} e {}".format(self._tratar_primeiro_mil(vetor[0]),vetor[1], vetor[2])
            self.vetor_dados.set_nome(nome)
           
        if(self.vetor_dados.tes_tamanho_igual_2):
            # encontrar se occore o problema do mil mil
            nome = "{} e {}".format(self._tratar_primeiro_mil(vetor[0]),vetor[1])
            self.vetor_dados.set_nome(nome)
           
        if(self.vetor_dados.tes_tamanho_igual_1):
            # tratar o caso do 100
            # refatorar
            if("cento" == vetor[0]):
                self.vetor_dados.set_nome("cem")
                
            else:
                nome = "{}".format(vetor[0])
                self.vetor_dados.set_nome(nome)

        return self.vetor_dados.get_nome()
        
        
        
    
    def _retira_string(self):
        vetor = self.vetor_dados.nova_strutura_dados
        vetor_string = []
        for valor in vetor:
            palavra_saida = ""
            if valor.teste_unidade:
                palavra_saida = "{}".format(valor.nome)

            if valor.teste_dezena or valor.teste_centena :
                palavra_saida = "{}".format(valor.nome)

            if valor.teste_milhar or valor.teste_milhar_dezena or valor.teste_e_milhar :
                palavra_saida = "{} mil".format(valor.nome)

            vetor_string.append(palavra_saida)

        # so para testar.
        nome = self._deci_de_vetor(vetor_string)
        return nome





        
    


        # self.teste_0 = self.numero == 0
        # # é a unidade
        # self.teste_unidade = self.numero  < 10  # 1
        # self.teste_dezena = self.numero  < 100 and not self.teste_unidade  #10
        # self.teste_centena = self.numero  < 1000 and not self.teste_dezena and not self.teste_unidade #900
        # self.teste_e_milhar = self.numero == 1000
        # self.teste_milhar = self.numero  < 10000 and not self.teste_e_milhar and not self.teste_centena and not self.teste_dezena and not self.teste_unidade # 9000
        # self.teste_milhar_dezena = self.numero <= 100000 and not self.teste_e_milhar and not self.teste_milhar and not self.teste_centena and not self.teste_dezena and not self.teste_unidade #99000




    



        # teste case para quando aconteceu alguma execao no vetor, 19,18

    # teste case para quando so vem um numero
    

    # preciso escrever a conversao para ter certeza disso.
    # teste case se tem algum vetor zerado
    # esse ainda nao tenho certeza se vou usar
    # provavelmente nao
    # self.tes_case_especial_0 

    
    
    
    # def _decidir_saida_string(self):
    #     pass
        

    # # Precissa urgentemente ser refatorado
    # def _cria_vetor_frase(self):
    #     self.lista_nomes = self._cria_lista_nomes()
    #     test_case_especial_1 = self.tes_case_especial_5  == 1 
    #     test_case_especial_5 = self.tes_case_especial_5  == 5

    #     list_string =[]
    #     # caso o valor seja inteiro so tenha 1 no array [300] [4000]
    #     if test_case_especial_1:
    #         for dici_convertido in self.lista_nomes:
    #         #codigo repetido.
    #             palavra_saida = ""
    #             numero_entrada = dici_convertido["num_s"]
    #             palavra = dici_convertido["num_ext"]

      

    #             self._decidir_saida_string()
    #             if teste_unidade:
    #                 palavra_saida = "{}".format(palavra)

    #             if teste_dezena or teste_centena :
    #                 palavra_saida = "{}".format(palavra)
                
    #             if teste_milhar_dezena or teste_milhar:
    #                 palavra_saida = "{} mil".format(palavra)


    #             list_string.append(palavra_saida)
    #     else:

    #         for i,dici_convertido in enumerate(self.lista_nomes):
    #             test_case_especial_primeiro_1 = i == 0  
    #             #codigo repetido.
    #             palavra_saida = ""
    #             numero_entrada = dici_convertido["num_s"]
    #             palavra = dici_convertido["num_ext"]


    #             # concerteza refatorar isso.
    #             teste_unidade = numero_entrada < 10  # 1
    #             teste_dezena = numero_entrada < 100 and not teste_unidade  #10
    #             teste_centena = numero_entrada < 1000 and not teste_dezena and not teste_unidade #900
    #             # tem que testar para igual
    #             teste_milhar = numero_entrada >= 1000 #and not teste_centena and not teste_dezena and not teste_unidade # 9000
    #             # teste_milhar_dezena = numero_entrada < 100000 and not teste_milhar and not teste_centena and not teste_dezena and not teste_unidade #99000

    #             # esse teste parece nao estar sendo util 
    #             if teste_unidade:
    #                 palavra_saida = "{}".format(palavra)

    #             if teste_dezena or teste_centena :
    #                 palavra_saida = "{} e ".format(palavra)

    #             if teste_milhar:
    #                 palavra_saida = "{} mil e ".format(palavra)
                
    #             if test_case_especial_5:
    #                 if((teste_milhar) and test_case_especial_primeiro_1):
    #                     palavra_saida = "{} e".format(palavra)
    #                 else:
    #                     palavra_saida = "{} mil e ".format(palavra)

    #             list_string.append(palavra_saida)
        
    #     return list_string

    # # fazer algumas proteções para casa o valor nao tenha no dicionario
    # # tem que assegurar que o numero seja um inteiro
    # def _converte_numero(self,numero):
    #     return 
    

  
    # def _cria_lista_nomes(self):
    #     list_nomes = []
    #     for numero_entrada in self.list_entrada:
           
    #         teste_milhar_milhar = numero_entrada > 1000 
    #         teste_milhar_igual_milhar = numero_entrada == 1000 
    #         # teste_milhar = numero_entrada >= 900 and not teste_milhar_dezena # 9000

    #         # teste_milhar = numero_entrada > 1000 and numero_entrada < 10000
    #         # teste_milhar_dezena = numero_entrada >= 9999

    #         if teste_milhar_milhar:
    #             numero = int(numero_entrada/1000)
    #         elif teste_milhar_igual_milhar :
    #             numero = numero_entrada
    #         else:
    #             numero = numero_entrada
            
        
    
    #         list_nomes.append(
    #             {"num_s":numero_entrada,
    #              "num_ext":self._converte_numero(numero)})
                
    #     return list_nomes
        





# arrumando a entrada.
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


