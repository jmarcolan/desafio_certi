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

def test_converte_numero_lista_string1():

    bloco_teste = [[200, 20, 2],
                    [10,9],
                    [20,9],
                    [10000,9000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [10000,9000, 300,10,9],
                    [1],
                    [20000,9000, 300,10,9],
                    [90000,4000,500,80,7]]
    
    bloco_teste_saida =[[{'num_ext': 'duzentos', 'num_s': 200}, {'num_ext': 'vinte', 'num_s': 20}, {'num_ext': 'dois', 'num_s': 2}],
                    [{'num_ext': 'dezenove', 'num_s': 19}],
                    [{'num_ext': 'vinte', 'num_s': 20}, {'num_ext': 'nove', 'num_s': 9}],
                    [{'num_ext': 'dezenove', 'num_s': 19000}, {'num_ext': 'trezentos', 'num_s': 300}, {'num_ext': 'vinte', 'num_s': 20}, {'num_ext': 'um', 'num_s': 1}],
                    [{'num_ext': 'vinte', 'num_s': 20000}, {'num_ext': 'nove', 'num_s': 9000}, {'num_ext': 'trezentos', 'num_s': 300}, {'num_ext': 'vinte', 'num_s': 20}, {'num_ext': 'um', 'num_s': 1}],
                    [{'num_ext': 'dezenove', 'num_s': 19000}, {'num_ext': 'trezentos', 'num_s': 300}, {'num_ext': 'dezenove', 'num_s': 19}],
                    [{'num_ext': 'um', 'num_s': 1}],
                    [{'num_ext': 'vinte', 'num_s': 20000}, {'num_ext': 'nove', 'num_s': 9000}, {'num_ext': 'trezentos', 'num_s': 300}, {'num_ext': 'dezenove', 'num_s': 19}],
                   [{'num_ext': 'noventa', 'num_s': 90000}, {'num_ext': 'quatro', 'num_s': 4000}, {'num_ext': 'quinhentos', 'num_s': 500}, {'num_ext': 'oitenta', 'num_s': 80}, {'num_ext': 'sete', 'num_s': 7}]]
    for count,teste in enumerate(bloco_teste):
        parser_entrada = Converte_numero(teste)
        saida = parser_entrada._cria_lista_nomes()
        print(saida)
        assert saida == bloco_teste_saida[count]

# refatoracao de nomeclatura é necessaria
def test_converte_numero_lista_string_final():

    bloco_teste = [ [1000, 0,40,2],
                    [20000,9000, 300,10,9],
                    [200, 20, 2],
                    [10,9],
                    [20,9],
                    [10000,9000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [10000,9000, 300,10,9],
                    [1],
                    [20000,9000, 300,10,9],
                    [90000,4000,500,80,7],
                    [1],
                    [10],
                    [100],
                    [1000],
                    [2000],
                    [5000]]
   
#    
    for count,teste in enumerate(bloco_teste):
        parser_entrada = Converte_numero(teste)
        saida = parser_entrada._cria_vetor_frase()
        print(saida)
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
def test_numero_propiedades():
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
                    99999]

    for count,teste in enumerate(bloco_teste):
        numero_ = Numero(teste)
        print(numero_)

#         saida = parser_entrada._get_cases()

