from conversor_dados import *

def test_answer():
    assert inc(3) == 4


def test_arruma_entrada():
    
    
    bloco_teste = [[200, 20, 2],
                    [10,9],
                    [20,9],
                    [10000,9000, 300,20,1],
                    [20000,9000, 300,20,1],
                    [10000,9000, 300,1,9],
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
    
# def test_arruma_entrada():
#     converso = Arrumando_entrada()
    
#     bloco_teste = [[200, 20, 2],
#                     [10,9],[20,9],
#                     [10000,9000, 300,20,1],
#                     [20000,9000, 300,20,1],
#                     [10000,9000, 300,1,9]]

#     bloco_teste_resposta = [[200, 20, 2],
#                     [19],[20,9],
#                     [19000, 300,20,1],
#                     [20000,9000, 300,20,1],
#                     [19000, 300,19]]
    
