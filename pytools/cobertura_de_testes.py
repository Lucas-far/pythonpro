

"""
Módulo: cobertura_de_testes.py
Aula: Cobertura de Testes
"""

"----------------------------------------------------- INSTALAÇÃO -----------------------------------------------------"

""  # pip install pytest-cov
""  # pip freeze > requirements.txt

"------------------------------------------------------- BRANCH -------------------------------------------------------"

""  # No contexto da aula, a integração do [ pytest cov ] é feita em uma branch local de nome [ 23 ]
""  # Sendo assim, o contexto da aula acontecerá dentro desta branch

"------------------------------------------------- COMANDO PARA TESTE -------------------------------------------------"

"SINTAXE"  # pytest nome_do_pacote_de_testes/nome_dos_arquivos_de_teste --cov=nome_do_pacote_de_testes
"EXEMPLO"  # pytest tests/tests.py --cov=tests
"TRAVIS"   # O [ pytest cov ] pode ser integrado ao arquivo [ .travis.yml ], no seu campo [ script ]

"-------------------------------------------------------- OBS ---------------------------------------------------------"

""  # Lembrar que um primeiro teste já deve ser feito, para testar o funcionamento
""  # Tendo o [ pytest cov ] gerado um relatório com sucesso, pode-se prosseguir com as próximas etapas

"------------------------------------------ WEBSITE PARA CONSULTA DE TESTES -------------------------------------------"

""  # https://codecov.io -> logar com github -> acessar os repositórios -> escolher o repositório alvo
""  # Na página do repositório alvo, há um grupo de abas no topo da página. Clique a aba [ settings ]
""  # Ao abrir, procure pelo link [ Badge ], e copie o link [ markdown ]
""  # Lembrando que, esses ícones de badges são colados ao conteúdo do arquivo [ README.md ]

"----------------------------------------- CONFIGURAÇÕES ADICIONAIS NO TRAVIS -----------------------------------------"

""  # No arquivo [ .travis.yml ], no campo [ install ], adicionar: [ codecov ]
""  # --------------------------- criar um campo [ after success ] e adicionar: [ codecov ]


def exemplo():
    """
    install:
      - pip install -q -r requirements.txt codecov
    after success:
      - codecov
    """


"------------------------------------------------ PROCEDIMENTOS FEITOS ------------------------------------------------"

""  # Instalação do [ Pytest cov ]
""  # Execução do teste
""  # Vinculação de conta Github com [ Codecov ]
""  # Configuração da instalação do [ Codecov ] não no repositório local, mas na execução do [ Travis ]

"--------------------------------------------- PROCEDIMENTOS GIT E GITHUB ---------------------------------------------"

""  # git add .
""  # git commit -m 'added Pytest cov'
""  # git push
""  # Se você for o dono do projeto, o próximo passo é verificar se o [ Travis ] executa o build

"CASO CONTRÁRIO"

""  # O repositório local do professor está vinculado a dois repositórios remotos
""  # O branch [ 23 ] foi criado para integrar o [ Pytest cov ] ao projeto
""  # O push do branch [ 23 ], é enviado a um dos repositórios remotos vinculados
""  # O branch [ 23 ] é enviado ao dono do repositório cujo qual você está vinculado
""  # Como o professor é o dono do repositório, através de uma conta diferente, ele acessa o branch [ 23 ]
""  # Aceita-se o branch criando um PULL REQUEST deste, passando como comentário [ close #23 ]
""  # Por último, o [ Travis ] pode ser verificado, para saber se a build é feita
