from sistema import *

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
                        "29319",
                        "94587",
                        "1",
                        "10",
                        "100",
                        "1000",
                        "2000",
                        "5000",
                        "1042",
                        "0"]


        bloco_teste_saida = ['um mil e cento e quarenta e dois',
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
                                 'um mil',
                                 'dois mil',
                                 'cinco mil',
                                 "um mil e quarenta e dois",
                                 "zero"]

        for count,teste in enumerate(bloco_teste):
                recebe = Transforma_numero_extensao(teste)

                vetor_palavras = recebe.get_saida()
                
                # palavra = recebe.valores_convertidos_vetor._deci_de_vetor()
                # print(vetor_palavras)
                assert vetor_palavras == bloco_teste_saida[count]
