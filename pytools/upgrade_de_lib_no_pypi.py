

"""
Módulo: upgrade_de_lib_no_pypi.py
Aula: Upgrade de Lib no PyPi
"""

def parte_1():
    """
    - retorno ao repositório local, no contexto [ libpythonpro ]
    - [ raiz / new / file / MANIFEST.in ], abrindo como arquivo de [ .txt ]
    - abrir esse arquivo, e incluir o conteúdo: (se esses arquivos existirem no seu projeto)

        include README.md
        include LICENSE

    - foi explicado que, como houve uma alteração no projeto já publicado, é preciso alterar a versão
    - ir ao pacote [ libpythonpro ] -> arquivo [ .__init__.py ] -> e modificar [ __version__ = 0.1 ]
    - a cada nova mudança, a versão muda, nesse caso, a cada [ 0.1 ], portanto [ __version__ = 0.2 ]
    - python setup.py sdist (modificando no pacote [ dist ], o arquivo [ .zip ])
    - caso o repositório local não esteja ativado, ativar
    - twine upload dist/* (as credenciais sempre são pedidas)
    - https://pypi.org/project/nome_seu_pacote/ (acessar seu projeto publicado)
    - atualizar a página (a versão terá sido atualizada)
    - pip install libpythonpro
    - git tag 0.2 (número da versão criada no pacote [ libpythonpro ], no arquivo [ .__init__.py ])
    - git add .
    - git commit -m 'msg'
    - git push --tags
    - git push
    - https://github.com/pythonprobr/libpythonpro/releases (ir ao rep. remoto e acessar aba [ tags ])
    """
