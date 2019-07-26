from parser_entrada import *

def test_ParserEntrada_sinal():
    bloco_teste = ["100",
                    "0",
                    "-10"]

    bloco_teste_saida =[False,
                    False,
                    True]
    
    for count,teste in enumerate(bloco_teste):

        parser_entrada = Parser_entrada(teste)
        saida = parser_entrada._detecta_sinal()
        
        assert saida == bloco_teste_saida[count]

def test_ParserEntrada_0():
    bloco_teste = ["100",
                    "0",
                    "-10"]

    bloco_teste_saida =[False,
                    True,
                    False]
    
    for count,teste in enumerate(bloco_teste):

        parser_entrada = Parser_entrada(teste)
        saida = parser_entrada._detecta_zero()
        
        assert saida == bloco_teste_saida[count]

def test_ParserEntrada_trata_sinal():
    bloco_teste = ["100",
                    "0",
                    "-10"]

    bloco_teste_saida =[[1,0,0],
                    [0],
                    [1,0]]
    
    for count,teste in enumerate(bloco_teste):

        parser_entrada = Parser_entrada(teste)
        saida = parser_entrada._trata_sinal_entrada()
        
        assert saida == bloco_teste_saida[count]

def test_ParserEntrada_Gera_Desena():
    bloco_teste = ["100",
                    "0",
                    "-10"]

    bloco_teste_saida =[[100,0,0],
                    [0],
                    [10,0]]
    
    for count,teste in enumerate(bloco_teste):

        parser_entrada = Parser_entrada(teste)
        saida = parser_entrada._gera_desena()
        
        assert saida == bloco_teste_saida[count]

def test_ParserEntrada_get_vetor_tratado():
    bloco_teste = ["100",
                    "0",
                    "-10",
                    "000"]

    bloco_teste_saida =[[100],
                    [0],
                    [10],
                    [0]]
    
    for count,teste in enumerate(bloco_teste):

        parser_entrada = Parser_entrada(teste)
        saida = parser_entrada.get_vetor_tratado()
        
        assert saida == bloco_teste_saida[count]