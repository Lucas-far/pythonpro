

"""
Módulo: fork.py
Aula: Pull Request Não Aceito
"""

"OBS"  # Issues podem ser entendido como uma forma alternativa de PULL REQUEST
def parte1():
    """
    1 - [ Issues ] é um dos menus visíveis na página de um repositório
    2 - pessoas normais ou contribuidores postam tópicos sobre algum possível bug ou ideia para o repositório
    3 - cada novo tópico postado, gera uma id, representada por [ #int ]
    4 - esse [ #int ] pode ser mencionado em mensagem de COMMIT, via terminal ou IDE
    5 - caso o COMMIT tenha o objeto de solucionar uma issue, mencionar [ close #int ]
    6 - Após o COMMIT/PUSH, estará disponível um PULL REQUEST, baseado na mudança feita por você
    7 - Na área de postagem do PULL REQUEST, escrevendo o seu [ close #id ], deve aparecer a sua [ Issue ]
    8 - Enviar o PULL REQUEST

    SOBRE PULL REQUEST
    OBS:
        1 - Caso haja algum erro no PULL REQUEST, usuários podem fazer uso da opção [ file changed ] [ + ]
        2 - Então pode-se criar uma edição, como uma forma de aviso, e enviar para a pessoa que fez o PULL REQUEST

    SOBRE PULL REQUEST NÃO ACEITO
        1 - Caso a PULL REQUEST não tenha progresso, pode-se escrever uma mensagem e usar o botão [ Close and comment ]
        2 - No seu projeto clonado, fazer: [ git reset --hard HEAD^1 ]
        3 - O valor inteiro representa a quantidade de commits que deve-se retornar
    """
