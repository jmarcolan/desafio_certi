# desafio_certi
Realizando o desafio da certi


# Desafio 
Na linguagem de sua preferência, crie um servidor HTTP que, para cada requisição GET, retorne um JSON cuja chave extenso seja a versão por extenso do número inteiro enviado no path. Os números podem estar no intervalo [-99999, 99999].

# Exemplos:

- λ curl http://localhost:3000/1
```
{ "extenso": "um" }
```
- λ curl http://localhost:3000/-1042
```
{ "extenso": "menos mil e quarenta e dois" }
```
- λ curl http://localhost:3000/94587
```
{ "extenso": "noventa e quatro mil e quinhentos e oitenta e sete" }
```

- Nos mande o link do repositório no GitHub com o código em até sete dias úteis.
- Se você abrir um Pull Request (p.ex. do seu branch de desenvolvimento para o master) nós faremos o review e você terá a chance de corrigir os erros para uma segunda avaliação.
- Não esqueça do README.md com as instruções para rodar o servidor!
- Não esqueça dos "e"s separando milhares, centenas e dezenas (vide exemplo): "noventa e quatro mil e quinhentos e oitenta e sete". Esse não é o padrão da norma culta da língua portuguesa, e isso é intencional.
-É esperado que o código implemente o algoritmo de tradução.


Mesmo que não esteja com a lógica completa, nos envie o que conseguiu fazer até o momento.
Em caso de dúvidas sobre o desafio, mande um email para ept@certi.org.br e mzr@certi.org.br.

- Bônus: Crie um ambiente Docker para que possamos rodar seu servidor sem instalar dependências locais.

Outras coisas em que prestamos atenção no review: edge cases e tratamento de erros, testes unitários, estruturação e qualidade do código, uso do git...


# Para isolar a aplicação
Para usar a aplicação foi usado o [gerador de arquivo](https://github.com/bndr/pipreqs), que gera o arquivo requirements.txt necessário para usar o pip.

# Configuração do Travis
Para consrtuir o arquivo do Travis foi usado a [pagina do travis](https://docs.travis-ci.com/user/languages/python/). 

# Configuração do ambiente de desenvolvimento

O ambiente de desenvolvimento usado foi o Visual Studio Code. O meu VSCode tinha o [problema](https://stackoverflow.com/questions/52462599/visual-studio-code-python-timeout-waiting-for-debugger-connection)

# Heroku

O servidor foi posto em produção usando o [site heroku](www.heroku.com)


# Termos

- vetor tratado de numeros. Exemplo a lista [100,10,9] se torna [100,19]

- vetor explodido o numero 119 se torna a lista [100, 10, 9]


Dcomentação seguindo estilo do google.
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html