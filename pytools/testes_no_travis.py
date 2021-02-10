

"""
Módulo: testes_no_travis.py
Aula: Testes no Travis
"""

def logica_da_aula():
    """
    - O professor, em aulas anteriores, criou testes no seu repositório local, e um deles está equivocado
    - A intenção é realizar um COMMIT/PUSH no repositório local, com esse erro presente
    - .................................... passando a hash da issue [ close #21 ]
    - O objetivo da COMMIT/PUSH visa configurar os testes para rodar no Travis
    - Após o envio desse COMMIT/PUSH, gera-se um BRANCH, do qual pode ser requisitado um PULL REQUEST
    - Quando o Travis for acessado, ele vai travar, pois o erro proposital é alcançado
    - Volta-se ao repositório local, corrige-se o erro
    - Só que, ao invés de ser efetuado um novo COMMIT/PUSH, é usado uma opção do Git chamada: [ amend commit ]
    """

# Criação de um arquivo [ .flake8 ]
def parte_1():
    """
    [flake8]
    max-line-length = 120
    exclude =

      .pytest_cache
    """

# Criação de um arquivo [ .travis.yml ]
"OBS"  # Para a integração funcionar, é preciso a execução de um COMMIT e PUSH, após a criação do arquivo
"OBS"  # O procedimento de integração não acontece imediatamente
def parte_2():
    """
    language: python
    python:
      - "3.9"
    install:
      - pip install -r requirements.txt
    script:
      - flake8
      - pytest 'tests.py'
    """
