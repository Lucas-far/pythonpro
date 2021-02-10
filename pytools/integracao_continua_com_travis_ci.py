

"""
Módulo: integracao_continua_com_travis_CI.py
Aula          || Integração Contínua com Travis CI
Palavra_chave ||
Objetivo      ||
"""

"Definição"  # é uma integração contínua (continuous integration) para evitar execução de tarefas manuais reincidentes

# Criação de um conta e tornar repositórios integráveis ao Travis
def parte1():
    """
    1 - https://travis-ci.org/ ---> será mudado para o domínio [ https://travis-ci.com/ ]
    2 - Signup com sua conta GitHub

    MÉTODO 1:
    3 - https://travis-ci.org/getting_started
    4 - activate all repositories [ botão ]

    MÉTODO 2:
    3 - Na página inicial do Travis: [ avatar / settings ]
    4 - Ao carregar, você verá seus repositórios, ative aquele que você quer integrar ao Travis
    """

# Escolher um emblema para inserir em repositório local, no arquivo [ README.md ]
def parte2():
    """
    1 - Ir ao avatar / botão esquerdo / settings / clicar em um repositório
    2 - Procurar e clicar em uma borda de nome: [ build ]
    3 - Esta abrirá um [ Status Image ] com campos [ BRANCH ] [ FORMAT ] [ RESULT ]
    4 - No campo [ FORMAT ], escolher [ markdown ] e copiar o retorno do campo [ RESULT ]
    """

# Configuração do Travis no seu repositório local
"OBS"  # através da criação do arquivo [ .yml ], você conseguirá dizer ao [ Travis CI ] o que fazer
"OBS"  # o gatilho para o [ Travis CI ] agir, é a ação do [ PUSH ], do Github
"OBS"  # [ Travis CI ] funciona a partir do segundo [ PUSH ]
def parte3():
    """
    1 - No seu repositório [ raiz / botão direito / new / file / .travis.yml ]
    2 - Conteúdo do arquivo:

        language: python
        python:
          - "3.9"
        install:
          - pip install -r requirements.txt
        script:
          - flake8

    OBS SOBRE AS CHAVES:
        - python (para saber a versão, no terminal, digitar [ python -V e copiar o retorno aqui ])
        - install (pip install -r requirements-dev.txt pode ser criado, ao invés, caso haja dependências separadas)
    """
