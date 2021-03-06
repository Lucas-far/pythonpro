

"""
Módulo: arquivo_setup.py
Aula: Arquivo Setup.py
"""

"OBS"  # Não entendo o propósito disso
"OBS"  # Arquivo criado como [ setup.py ] na raiz de um projeto seu (no meu caso, Django)

# Modelo de um setup
def parte_1():
    """
    1 - https://github.com/pythonprobr/libpythonpro/blob/master/setup.py
    2 - copiar o conteúdo do arquivo [ setup.py ]
    3 - ir ao seu repositório local do projeto
    4 - raiz / new / python file / setup
    5 - colar o conteúdo do modelo
    """

# Estrutura do modelo (apenas como backup)
def esqueleto():
    """
    import codecs
    import os
    import sys

    from distutils.util import convert_path
    from fnmatch import fnmatchcase
    from setuptools import setup, find_packages


    def read(fname):
        return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


    ""  # Provided as an attribute, so you can append to these instead
    ""  # of replicating them:

    standard_exclude = ["*.py", "*.pyc", "*$py.class", "*~", ".*", "*.bak"]
    standard_exclude_directories = [".*", "CVS", "_darcs", "./build", "./dist", "EGG-INFO", "*.egg-info"]

    ""  # (c) 2005 Ian Bicking and contributors; written for Paste (http://pythonpaste.org)
    ""  # Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
    ""  # Note: you may want to copy this into your setup.py file verbatim, as
    ""  # as you can't import this from another package, when you don't know if that package is installed yet.


    def find_package_data(
        where=".", package="", exclude=standard_exclude, exclude_directories=standard_exclude_directories,
        only_in_packages=True, show_ignored=False
                          ):
        '''
        Return a dictionary suitable for use in ``package_data`` in a distutils ``setup.py`` file.
        The dictionary looks like:: {"package": [files]}

        Where ``files`` is a list of all the files in that package that don"t match anything in ``exclude``.

        If ``only_in_packages`` is true, then top-level directories that are not packages won"t be included
        (but directories under packages will).

        Directories matching any pattern in ``exclude_directories`` will be ignored;
        by default directories with leading ``.``, ``CVS``, and ``_darcs`` will be ignored.

        If ``show_ignored`` is true, then all the files that aren"t included in package data are shown on stderr
        (for debugging purposes).

        Note patterns use wildcards, or can be exact paths (including leading ``./``), and all searching is case-insensitive.
        '''

        out = {}
        stack = [(convert_path(where), "", package, only_in_packages)]
        while stack:
            where, prefix, package, only_in_packages = stack.pop(0)
            for name in os.listdir(where):
                fn = os.path.join(where, name)
                if os.path.isdir(fn):
                    bad_name = False
                    for pattern in exclude_directories:
                        if (fnmatchcase(name, pattern)
                                or fn.lower() == pattern.lower()):
                            bad_name = True
                            if show_ignored:
                                print("Directory %s ignored by pattern %s" %
                                      (fn, pattern), file=sys.stderr)
                            break
                    if bad_name:
                        continue
                    if (os.path.isfile(os.path.join(fn, "__init__.py"))
                            and not prefix):
                        if not package:
                            new_package = name
                        else:
                            new_package = package + "." + name
                        stack.append((fn, "", new_package, False))
                    else:
                        stack.append((fn, prefix + name + "/", package, only_in_packages))
                elif package or not only_in_packages:
                    # is a file
                    bad_name = False
                    for pattern in exclude:
                        if (fnmatchcase(name, pattern)
                                or fn.lower() == pattern.lower()):
                            bad_name = True
                            if show_ignored:
                                print("File %s ignored by pattern %s" %
                                      (fn, pattern), file=sys.stderr)
                            break
                    if bad_name:
                        continue
                    out.setdefault(package, []).append(prefix + name)
        return out


    PACKAGE = "libpythonpro"
    NAME = PACKAGE
    DESCRIPTION = "Módulo para exemplificar construção de projetos Python no curso PyTools"
    AUTHOR = "Renzo Nuccitelli"
    AUTHOR_EMAIL = "renzo@python.pro.br"
    URL = "https://github.com/pythonprobr/libpythonpro"
    VERSION = __import__(PACKAGE).__version__

    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license="GNU AFFERO GENERAL PUBLIC LICENSE",
        url=URL,
        packages=find_packages(exclude=["tests.*", "tests"]),
        package_data=find_package_data(PACKAGE, only_in_packages=False),
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
            "Framework :: Pytest",
        ],
        install_requires=[
            'requests'
        ],
        zip_safe=False,
    )
    """

# Configuração do modelo (alteração de dados)
"OBS"  # Nessa aula, há um pacote, e eu não sei ele já o tinha criado nas aulas anteriores, ou nessa
"OBS"  # O nome do pacote == nome do projeto (não sei se é mandatório/convenção)
"OBS"  # Na variável [ setup ], será preciso consultar o arquivo [ classificadores.txt ] (ver def parte_2)
"OBS"  # Ou então, consultar -> https://pypi.org/pypi?%3Aaction=list_classifiers
"OBS"  # [ setup ] [ par=classifiers ] é alterado, baseado na opinião do professor em relação ao projeto dele
def parte_2():
    """
    PACKAGE = 'nome do pacote do seu projeto'
    NAME = PACKAGE
    DESCRIPTION = 'descrição do arquivo readme.md'
    AUTHOR = 'Seu nome'
    AUTHOR_EMAIL = 'Seu email'
    URL = 'Link do seu projeto no Github'
    VERSION = Ir ao diretório do pacote, abrir [ __init__.py ] e inserir [ __version__ = 'int.int' ] EX: '0.1'

    setup(
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        license=read('LICENSE') ou license="GNU AFFERO GENERAL PUBLIC LICENSE"
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
            'Programming Language :: Python :: 3.9',
            'Framework :: Django :: 2.2',
        ],
        install_requires=[
            'nomes de dependências sem sua versão' (pelo professor, só foi usado a biblioteca [ requests ])
        ]
    )
    """
