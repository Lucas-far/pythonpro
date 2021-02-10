

"""
Módulo: chaves_ssh.py
Aula: Chaves SSH
"""

# Clonar um repositório (manualmente, sem auxílio de uma IDE)
def parte1():
    """
    1 - Um repositório pode ser clonado via link: [ https ] ou [ ssh ] em sua página no GitHub
    2 - Ir ao botão [ code (atualmente) ] e copiar o link SSH
    3 - No terminal

        EXEMPLO 1: git clone git@github.com:codingforentrepreneurs/eCommerce.git
        EXEMPLO 2: git clone git@github.com:codingforentrepreneurs/eCommerce.git one-ecommerce

        OBS: O primeiro exemplo foi clonado com o nome original do repositório
        OBS: O segundo exemplo foi clonado com um nome alternativo para o repositório
    """

# Comandos git para ambientes virtuais conectados a um repositório
def parte2():
    """
    1 - git init
    2 - git status
    3 - git add .
    4 - git commit -m 'Mensagem obrigatória'
    5 - git push
    """

# Criar no OS, sua chave SSH pessoal, para usar no GitHub
def parte3():
    """
    1 - [ Ubuntu  ] ssh-keygen -t rsa
    1 - [ Windows ] ssh-keygen.exe -t rsa

    -------------------------------------------------------------------------------------------------------------------
    OBS: Em 1, eu creio que após "rsa", pode usar [ 'seu_email_github' ], mas não estou certo
    -------------------------------------------------------------------------------------------------------------------

    2 - Digitar uma passphrase

       EXEMPLO: umafrasepodevalermuitacoisamasaomesmotempopodenaovalernada

    --------------------------------------------------------------------------------------------------------------------
    OBS: Um diretório é criado em: [ /home/seu_user/.ssh ]
    --------------------------------------------------------------------------------------------------------------------

    3 - Serão criados: [ public key / key fingerprint = SHA256 / key's randomart ]
    4 - Ir ao diretório [ /home/seu_user/.ssh ], procurar por [ cat id_rsa.pub ], abrir e [ ctrl + c ]
    5 - Ir ao site do Github
    6 - Fazer o caminho: [ Avatar / Settings / SSH and GPG keys / New ssh key ]
    7 - No campo [ title ], dar o nome desejado à chave
    8 - No campo [ key ], [ ctrl + v ]
    9 - Salvar
    """
