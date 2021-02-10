

"""
Módulo: pyenv_no_ubuntu.py
Aula: Pyenv no Ubuntu
"""

# Bibliotecas relevantes antes de instalar o Pyenv
def parte1():
    """
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev
    """

# Instalação do Pyenv
"OBS"  # Pyenv instala Python no OS, sem afetar o Python existente no OS
def parte2():
    """
    1 - curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    2 - Ao final da instalação, podem ser recomendadas configurações binárias, então copie-as
    """

# Configuração dos binários do Pyenv
def parte3():
    """
    1 - Ir à rota: [ /home/seu_user/.bashrc ] (na aula, foi uso um comando: [ vim .bashrc ])
    2 - Abrir o módulo
    3 - Inserir na linha final:

        export PATH="/home/seu_user/.pyenv/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"

    4 - Salvar
    5 - Fechar o terminal
    6 - Reabrir o terminal
    7 - pyenv (se a instalação teve êxito, o Pyenv será chamado no terminal)
    """

# Listar versões do Pyenv para escolher qual delas instalar, e tornar a versão do Python global
def parte4():
    """
    1 - pyenv install -l
    2 - Procurar na listagem, a versão inteiramente numérica mais atual e instalar

        EXEMPLO: 3.9.1

    3 - pyenv install 3.9.1
    4 - pyenv global 3.9.1
    """

# Instalar um ambiente virtual usando Pyenv e atualizar (caso necessário)
def parte5():
    """
    1 - Criar um diretório ou abrir um projeto Python/Django
    2 - No terminal: [ python3 -m venv .venv ]

        SOBRE .venv:
            2.1 - É o nome do ambiente virtual
            2.2 - O ponto é para evitar criar dois diretórios, criando apenas um

    4 - pyenv install -l (verificar a versão numérica mais atual sem o prefixo [ -dev ])
    5 - pyenv versions

    SE O RETORNO FOR IGUAL A VERSÃO NUMÉRICA:
        5.1 - pyenv global versão [ EXEMPLO: pyenv global 3.9.1 ]

    CASO NÃO SEJA:
        5.2 - pyenv install versão numérica mais atual do item 4. [ EXEMPLO: pyenv install 3.9.1 ]
        5.3 - pyenv global versão [ EXEMPLO: pyenv global 3.9.1 ]
    """

# Desinstalar um ambiente virtual
def parte6():
    """
    1 - Não sei exatamente se há um comando
    2 - O que eu sei é que, ao criar um ambiente virtual, você ativa este (isso pelo virtualenv)
    3 - No pyenv, você ativa manualmente: [ source .venv/bin/activate ]
    4 - Para desativar, precisa estar ativado, caso contrário, não funcionará
    5 - Para desativar: [ deactivate ]
    """
