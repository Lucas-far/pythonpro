

"""
Módulo: instalação_local_de_pacote.py
Aula: Instalação Local de Pacote
"""

# Instruções de continuação
def parte_1():
    """
    PARTE 1
    - Na aula [ Instalação de Libs com PIP ], o professor criou um pacote [ raiz / new / python package / libpythonpro ]
    - A intenção disso, era preparar o projeto para que este funcione como uma biblioteca
    - Segundo o professor, nesse pacote, será mantido o código fonte com a resolução dos problemas
    - Eu não sei qual a razão de fazer isso

    PARTE 2
    - Segundo o professor, o objetivo dessa aula é instalar o [ setup ] localmente, a partir do código-fonte
    - Segundo o professor, isso é feito para testar se a instalação é bem-sucedida antes de publicar o pacote no Pypi
    - Ele vai até sua pasta de projetos do Pycharm [ Pycharm Projects ]
    - O local escolhido é apropriado, já que o projeto que possui o [ setup ], encontra-se nesse local

    PARTE 3
    - Supondo que a rota onde se quer testar o projeto, seja: [ /home/seu_user/PycharmProjects ]
    - Então, cria-se um ambiente virtual (eu criaria uma pasta antes de fazer isso)
    - python3 -m venv .venv
    - source .venv/bin/activate
    - Supondo que o projeto com o arquivo [ setup ], esteja em: [ /home/lucas/PycharmProjects/libpythonpro ]
    - pip install -e ./libpythonpro/ (como o professor fez)
    - pip install -e /home/lucas/PycharmProjects/libpythonpro (como eu acho mais seguro fazer)
    - Ou seja, logado em um ambiente virtual, usa-se o comando de instalação, passando a rota do projeto
    """
