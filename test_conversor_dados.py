from conversor_dados import *

# def test_answer():
#     assert inc(3) == 4




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
    
