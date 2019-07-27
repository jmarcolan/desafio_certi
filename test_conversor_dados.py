from conversor_dados import *


def test_inverte_lista():
    bloco_teste = [[200, 20, 2],
                    [10,9],
                    [20,9],
                    [10000,9000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [10000,9000, 300,10,9],
                    [1]]

    bloco_teste_saida =[[2, 20, 200],
                    [9, 10],
                    [9, 20],
                    [1, 20, 300, 9000, 10000],
                    [1, 20, 300, 9000, 20000],
                    [9, 10, 300, 9000, 10000],
                    [1]]
    
    for count,teste in enumerate(bloco_teste):

        parser_entrada = Arrumando_entrada(teste)
        saida = parser_entrada._inverte_a_lista()
        
        assert saida == bloco_teste_saida[count]
    

def test_encontra_posicoes_excecao():
    
    
    bloco_teste = [[200, 20, 2],
                    [10,9],
                    [20,9],
                    [10000,9000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [10000,9000, 300,10,9],
                    [1]]

    bloco_teste_saida =[[1],
                    [1],
                    [1],
                    [1,4],
                    [1,4],
                    [1,4],
                    []]
    for count,teste in enumerate(bloco_teste):

        parser_entrada = Arrumando_entrada(teste)
        saida = parser_entrada._encontrando_posicao_critica()
        
        assert saida == bloco_teste_saida[count]
    
def test_regra_excecao():

    bloco_teste = [[200, 20, 2],
                    [10,9],
                    [20,9],
                    [10000,9000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [10000,9000, 300,10,9],
                    [1],
                    [20000,9000, 300,10,9]]

    bloco_teste_saida =[[False],
                    [True],
                    [False],
                    [False,True],
                    [False,False],
                    [True,True],
                    [],
                    [True,False]]

    for count,teste in enumerate(bloco_teste):

        parser_entrada = Arrumando_entrada(teste)
        saida = parser_entrada._testando_regra_excecao()
        
        assert saida == bloco_teste_saida[count]
#     bloco_teste_resposta = [[200, 20, 2],
#                     [19],[20,9],
#                     [19000, 300,20,1],
#                     [20000,9000, 300,20,1],
#                     [19000, 300,19]]
    

def test_saida_arrumada():

    bloco_teste = [[200, 20, 2],
                    [10,9],
                    [20,9],
                    [10000,9000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [10000,9000, 300,10,9],
                    [1],
                    [20000,9000, 300,10,9]]
    
    bloco_teste_saida =[[200, 20, 2],
                    [19],
                    [20,9],
                    [19000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [19000, 300,19],
                    [1],
                    [20000,9000, 300,19]]

    for count,teste in enumerate(bloco_teste):
        parser_entrada = Arrumando_entrada(teste)
        saida = parser_entrada._arrumando_entrada()
        assert saida == bloco_teste_saida[count]


# Os testes precisam de refatoracao no seu nome
# Os testes precisam de casos no qual de erro
# Os negativos serão tratos a posteriori

# comecar os testes para a classe Converte_numero

        # assert saida == bloco_teste_saida[count]


# def test_converte_numero_get_test_cases():

#     bloco_teste = [ [1000, 0,40,2],
#                     [20000,9000, 300,10,9],
#                     [200, 20, 2],
#                     [10,9],
#                     [20,9],
#                     [10000,9000, 300,20,1],
#                     [20000,9000, 300,20,1],
#                     [10000,9000, 300,10,9],
#                     [1],
#                     [20000,9000, 300,10,9],
#                     [90000,4000,500,80,7],
#                     [1],
#                     [10],
#                     [100],
#                     [1000],
#                     [2000],
#                     [5000]]

#     for count,teste in enumerate(bloco_teste):
#         parser_entrada = Converte_numero(teste)
#         saida = parser_entrada._get_cases()
#         print(saida)
# arrumar o teste para ver se ele extrai as caracteristicas dos numeros

def test_c_Numero():
        #caso fuja o valor do dicionario quebra e.g(9999)
    bloco_teste = [ 1,
                    9,
                    10,
                    19,
                    90,
                    100,
                    900,
                    1000,
                    2000,
                    5000,
                    10000,
                    9000]

    for count,teste in enumerate(bloco_teste):
        numero_ = Numero(teste)
        print(numero_)
        # aqui dentro tem que testar se esta vinco as propiedade dos numero de forma correta

def test_c_Converte_numero():
        # notar que as entrada esperada aqui tem que ser do dicionario
        bloco_teste = [ 1,
                    9,
                    10,
                    19,
                    90,
                    100,
                    900,
                    1000,
                    2000,
                    5000,
                    10000,
                    9000]
        for count,teste in enumerate(bloco_teste):
                numero_ = Numero(teste)
                print(numero_.get_nome())



def test_c_Conversor_dados_nome():
        bloco_teste = [ [1000, 100,40,2],
                    [20000,9000, 300,19],
                    [200, 20, 2],
                    [19],
                    [20,9],
                    [19000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [19000, 300,19],
                    [1],
                    [20000,9000, 300,19],
                    [90000,4000,500,80,7],
                    [1],
                    [10],
                    [100],
                    [1000],
                    [2000],
                    [5000]]

        bloco_teste_saida = ['mil e cento e quarenta e dois',
                              'vinte e nove mil e trezentos e dezenove',
                               'duzentos e vinte e dois',
                                'dezenove',
                                'vinte e nove',
                                 'dezenove mil e trezentos e vinte e um',
                                 'vinte e nove mil e trezentos e vinte e um',
                                 'dezenove mil e trezentos e dezenove',
                                 'um',
                                 'vinte e nove mil e trezentos e dezenove',
                                 'noventa e quatro mil e quinhentos e oitenta e sete',
                                 'um',
                                 'dez',
                                 'cem',
                                 'mil',
                                 'dois mil',
                                 'cinco mil']

        for count,teste in enumerate(bloco_teste):
                recebe = Conversor(teste)

                vetor_palavras = recebe.get_nome_extenso()
                
                # palavra = recebe.valores_convertidos_vetor._deci_de_vetor()
                # print(vetor_palavras)
                assert vetor_palavras == bloco_teste_saida[count]

def test_c_Vetor_dados_nome():
        # o teste tem que ser com os valores tratados
        bloco_teste = [ [1000, 100,40,2],
                    [20000,9000, 300,19],
                    [200, 20, 2],
                    [19],
                    [20,9],
                    [19000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [19000, 300,19],
                    [1],
                    [20000,9000, 300,19],
                    [90000,4000,500,80,7],
                    [1],
                    [10],
                    [100],
                    [1000],
                    [2000],
                    [5000]]

        bloco_teste_saida = ['mil e cento e quarenta e dois',
                              'vinte e nove mil e trezentos e dezenove',
                               'duzentos e vinte e dois',
                                'dezenove',
                                'vinte e nove',
                                 'dezenove mil e trezentos e vinte e um',
                                 'vinte e nove mil e trezentos e vinte e um',
                                 'dezenove mil e trezentos e dezenove',
                                 'um',
                                 'vinte e nove mil e trezentos e dezenove',
                                 'noventa e quatro mil e quinhentos e oitenta e sete',
                                 'um',
                                 'dez',
                                 'cem',
                                 'mil',
                                 'dois mil',
                                 'cinco mil']

        for count,teste in enumerate(bloco_teste):
                recebe = Vetor_dados(teste)

                vetor_palavras = recebe.get_nome()
                
                # palavra = recebe.valores_convertidos_vetor._deci_de_vetor()
                # print(vetor_palavras)
                assert vetor_palavras == bloco_teste_saida[count]







