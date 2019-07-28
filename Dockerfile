from python:3.6

# adiciona o diretorio . (que significar o atual) para o diretorio do container /todo
ADD . /todo

# tranforma o diretorio /todo para ser o diretorio de trabalho 
WORKDIR /todo

# roda o comando para inslar os requirments.tex
RUN pip install -r requirements.txt