from sistema import *

from servidor import *
def test_Transforma_numero_extensao():
        bloco_teste = [ "1142" ,
                        "29319",
                        "222",
                        "19",
                        "29",
                        "19321",
                        "29321",
                        "19319",
                        "1",
                        "94587",
                        "1",
                        "10",
                        "100",
                        "1000",
                        "2000",
                        "5000",
                        "1042",
                        "0",
                        "-29319",
                        "-1042",
                        "94587"]


        bloco_teste_saida = ['mil e cento e quarenta e dois',
                              'vinte e nove mil e trezentos e dezenove',
                               'duzentos e vinte e dois',
                                'dezenove',
                                'vinte e nove',
                                 'dezenove mil e trezentos e vinte e um',
                                 'vinte e nove mil e trezentos e vinte e um',
                                 'dezenove mil e trezentos e dezenove',
                                 'um',
                                 'noventa e quatro mil e quinhentos e oitenta e sete',
                                 'um',
                                 'dez',
                                 'cem',
                                 'mil',
                                 'dois mil',
                                 'cinco mil',
                                 "mil e quarenta e dois",
                                 "zero",
                                 'menos vinte e nove mil e trezentos e dezenove',
                                 "menos mil e quarenta e dois",
                                 "noventa e quatro mil e quinhentos e oitenta e sete"
                                 ]

        for count,teste in enumerate(bloco_teste):
                recebe = Transforma_numero_extensao(teste)

                vetor_palavras = recebe.get_saida()
                
                # palavra = recebe.valores_convertidos_vetor._deci_de_vetor()
                # print(vetor_palavras)
                assert vetor_palavras == bloco_teste_saida[count]


def test_Saida_Desafio_Certi():
        bloco_teste = [ "1142" ,
                        "29319",
                        "222",
                        "19",
                        "29",
                        "19321",
                        "1",
                        "94587",
                        "-1042",
                        "94587"]


        bloco_teste_saida = ['{"extenso": "mil e cento e quarenta e dois"}',
                        '{"extenso": "vinte e nove mil e trezentos e dezenove"}',
                        '{"extenso": "duzentos e vinte e dois"}',
                        '{"extenso": "dezenove"}',
                        '{"extenso": "vinte e nove"}',
                        '{"extenso": "dezenove mil e trezentos e vinte e um"}',
                        '{"extenso": "um"}',
                        '{"extenso": "noventa e quatro mil e quinhentos e oitenta e sete"}',
                        '{"extenso": "menos mil e quarenta e dois"}',
                        '{"extenso": "noventa e quatro mil e quinhentos e oitenta e sete"}'
                                 ]

        for count,teste in enumerate(bloco_teste):
                saida_extenso = Saida_Desafio_Certi(teste)

                texto = saida_extenso.saida()
                
                assert texto == bloco_teste_saida[count]

        
