

"""
Módulo: criacao_de_release.py
Aula: Criação de Release
"""

"OBS"  # Não entendi o motivo dos procedimentos dessa aula, por isso vou deixar aqui somente a transcrição

def parte_1():
    """
    - Anteriormente, em uma aula que eu não sei, foi criado um branch [ 18 ], que representa uma [ issue ]
    - O repositório local [ libpythonpro ], contêm o pacote de mesmo nome, e o arquivo [ setup.py ] na sua raiz
    - https://github.com/pythonbr/libpythonpro
    - Ir a aba [ branch ], selecionando o branch [ #18 ]
    - Botão [ New pull request ] -> [ Rebase and merge ] -> [ Confirm rebase and merge ]
    - Retorno ao repositório local, é preciso sair do branch [ 18 ], pois está resolvido, voltando ao branch [ master ]
    - git checkout master
    - git pull origin master
    - git tag 0.1 (número da versão criada no pacote [ libpythonpro ], no arquivo [ .__init__.py ])
    - git push --tags
    - https://github.com/pythonprobr/libpythonpro
    - Ir a aba [ tags ], nessa aba, está o histórico de todas as tags criadas, que podem ser baixadas
    - Abaixo das tags, há links para download de cada versão
    - [ zip / botão direito / copy link address ]
    - [ /home/seu_user/PycharmProjects/ ]
    - python3 -m venv .venv
    - source .venv/bin/activate
    - pip install ctrl + v do link
    """
