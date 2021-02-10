

"""
Módulo: criacao_e_execucao_de_testes.py
Aula: Criação e Execução de Testes
"""

# Configuração inicial
def parte_1():
    """
    - No contexto da aula, há o projeto/repositório local [ libpythonpro ]
    - Dentro do projeto, há um pacote de mesmo nome
    - [ botão direito / new / python package / tests ], tendo criado o pacote, agora cria-se o arquivo
    - [ botão direito / new / python file / tests ]
    - pytest libpythonpro/tests (não funcionou para mim)
    - então eu recortei o pacote [ tests ] para a raiz
    - deletei o pacote [ libpythonpro ]
    - entrei no pacote [ tests ]
    - pytest tests.py
    """

# Configurar o [ Pytest ] como teste principal no [ Pycharm ]
def parte_2():
    """
    File -> Settings -> Tools -> Python Integrated Tools -> Default test runner = pytest

    EXECUTAR TESTE
        botão direito no arquivo [ .py ] de teste (igual Unittest)
    """

# Exemplo de testes
def parte_3():
    """
    def make_dict(chave, valor):
        return {chave: valor}

    def test_make_dict():
        assert make_dict('chave', 'valor') == {'chave': 'valor'}

    def turn_list_into_str(list_items: list):
        return "".join(list_items)

    def test_turn_list_into_str():
        assert turn_list_into_str(['123']) == '123'
    """
