

"""
Módulo: Feature Branch
Aula: Feature Branch
"""

"Breach"  # Ramos de códigos distintos a partir de um ponto no seu histórico
"Tipos"   # LOCAL BRANCH  (projeto) [master ou origin/master]
"Tipos"   # REMOTE BRANCH (GitHub)  [origin/master]
"Acesso"  # No Pycharm: [ Git / Branches... ] ou canto inferior direito da tela da IDE

# Comando para branch comuns
def parte1():
    """
    listar todas branches locais
        1 - git branch
        2 - menu -> git -> branches

    listar todas branches, incluindo remotas
        1 - git branch --all

    listar todos repositórios remotos conectados
        1 - git remote -v

    conectar um repositório remoto
        1 - git remote add apelido link https ou ssh
        2 - menu -> git -> manage remotes -> name=apelido -> url=link SSH -> OK

    desconectar um repositório remoto
        1 - git remote rm apelido

    atualizar todas as branches remotas de todos rep. remotos
        1 - git fetch --all

    atualizar todas as branches remotas de determinado rep. remoto
        1 - git fetch repositorio

    criar uma branch local
        1 - git branch nome-da-branch
        2 - menu -> git -> new branch

    carregar os módulos de uma branch especifica
        1 - git checkout nome-da-branch
    """

# Alguns comando dessa aula que podem ser feitos alternativamente pelo Pycharm
def parte2():
    """
    [ Git / Manage Remotes... ]          # criar e conectar um repositório remoto (Pycharm)
    [ Git / Fetch ]                      # atualizar todas as branches remotas de todos rep. remotos (Pycharm)
    [ Git / Branches... / + New branch ] # criar um branch local (Pycharm)
    [ Git / Show Git Log ]               # verificar logs de braches feitas
    """

"===================="
# Ações feitas na aula
"===================="

# Explicação do contexto
def parte3():
    """
    1 - Foi feito 1 fork em aulas passadas, do repositório [ pythonpro / libpythonpro ] para [ renzon / libpythonpro ]
    2 - Depois desse fork, foi feito uma clonagem em [ renzon / libpythonpro ], para poder usar o repositório numa IDE
    3 - Nessa aula o procedimento de clonagem repete-se, copiando o link SSH
    4 - O repositório já está clonado (talvez fisicamente). A intenção agora é clonar o repositório remotamente
    """

# Criação de BRANCH REMOTO de nome: upstream
def parte4():
    """
    1 - git remote add apelido link SSH (CLONAR)
    2 - git remote -v                   (LISTAR)
    3 - git fetch -all                  (ATUALIZAR)
    """

# Criação de BRANCH LOCAL de nome: ramo
def parte5():
    """
    1 - [ menu -> git -> branches -> + new branch ] criação de um branch [ ramo ]
    2 - Aparentemente, [ menu -> git -> branches -> + new branch ] é usada para criar BRANCH LOCAL apenas
    3 - Ao criar o BRANCH LOCAL, a tela não muda, mas esse BRANCH tomar o lugar do BRANCH LOCAL anterior [ master ]
    4 - Altera-se em algo no projeto
    5 - [ menu -> git -> show git log ] teste para verificar se o log mostra as alterações nesse BRANCH LOCAL [ ramo ]
    """

# Migração entre BRANCHES
def parte6():
    """
    1 - No momento o BRANCH LOCAL logado é [ ramo ]
    2 - [ menu -> git -> branches -> local branches -> master -> seta -> checkout ] Reativar BRANCH LOCAL [ master ]
    3 - Diferente de criar um BRANCH e ele logar, o migrar causa alteração na tela
    4 - [ menu -> git -> branches -> local branches -> ramo -> seta -> checkout ] Reativar BRANCH LOCAL [ ramo ]
    5 - [ menu -> git -> branches -> local branches -> master -> seta -> delete ] Deletado BRANCH LOCAL [ master ]
    6 - No momento há somente um BRANCH LOCAL [ ramo ]
    """

# Explicações sobre BRANCH REMOTO e criação de um BRANCH LOCAL a partir de um BRANCH REMOTO
def parte7():
    """
    1 - BRANCH REMOTOS, normalmente são criados em trabalhos de equipe, para recebem PULL REQUESTS
    2 - Anteriormente, foi criado um BRANCH REMOTO [ upstream ], e este pode criar um novo BRANCH LOCAL
    3 - [ Git -> branches -> remote branches -> upstream -> seta -> checkout as new local brench ] com nome [ master ]
    4 - Nesse momento, volta-se a ter dois BRANCHES LOCAIS:
        ramo
        master = criado do BRANCH REMOTO = upstream

    5 - COMMIT/PUSH (o painel de PUSH precisa ser modificado)
    6 - No painel de PUSH, há um link, normalmente configurado ao nome do BRANCH LOCAL padrão [ master ]
    7 - No painel de PUSH, modificar esse link para [ origin ]
    8 - PUSH
    9 - Segundo o instrutor, a intenção disso é sincronizar o BRANCH REMOTA com o LOCAL
    """

# Procedimentos pós-sincronização: criar um BRANCH LOCAL para cada nova alteração desejada
def parte8():
    """
    1 - Resumo atual: BRANCH REMOTA [ upstream ] criou BRANCH LOCAL [ master ] + COMMIT/PUSH + link = origin + PUSH
    2 - Não fica claro se os procedimentos anteriores são mandatórios para que o resto possa ser feito
    3 - Tomando por base que "sim", agora, para cada nova alteração, cria-se um novo BRANCH LOCAL
    4 - [ menu -> git -> branches -> + new branch ] que no contexto, recebe o nome [ 4 ]
    5 - Como já explicado, ao criar um BRANCH LOCAL novo, este é ativado, sobescrevendo o ativado anteriormente
    6 - Portanto, mudanças posteriores, acontecem nesse BRANCH LOCAL nomeado [ 4 ]
    7 - Altera-se algo do projeto
    8 - COMMIT/PUSH (mensagem do commit com a sintaxe close #4, pois a alteração é feita para resolver um ISSUE)
    9 - No repositório matriz [ pythonpro / libpythonpro ], surge uma mensagem informando o BRANCH que recebeu PUSH
    10 - Há um botão dropdown com um símbolo de BRANCH, que mostra os BRANCHES ativos (não foi alterado)
    11 - Junto ao dropdown, deve haver um botão [ Compare and pull request ]
    """

# Quando o PULL REQUEST é aceito
def pull_request():
    """
    1 - [ Compare and pull request ] -> [ create pull request ] -> [ Rebase and merge ] -> [ Confirm rebase and merge ]
    2 - O código será integrado ao repositório original/matriz
    3 - [ menu -> git -> branches -> local branches -> 4 -> seta -> delete -> delete tracked branch ]
    4 - [ git fetch upstream ] talvez [ git fetch --all ] também seja uma opção
    5 - [ menu -> git -> branches -> local branches -> upstream -> seta -> merge ]
    6 - COMMIT/PUSH
    7 - Recomendação de efetuar sempre que possível [ git fetch ] para manter o código atualizado
    """

# Quando o PULL REQUEST é negado
def pull_request2():
    """
    1 - [ Menu -> git -> branches -> local branches -> master -> seta -> checkout ] Retornar ao BRANCH LOCAL [ master ]
    2 - [ Menu -> git -> branches -> local branches -> 4 -> seta -> delete ]  Deletar BRANCH LOCAL [ 4 ]
    """

#  transcrição de uma mensagem da aula que parece ser importante
def mensagem2():
    """
    A ideia do feature branch é que a branch master sempre fica sincronizada com o upstream para não ter o
    trabalho de reverter código toda hora

    1 - master [ BRANCH LOCAL ]
    2 - upstream [ BRANCH REMOTA ]
    """
