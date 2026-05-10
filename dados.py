# Dados que serão usados para funções do sistema de finanças
 # função para limpar a tela e deixar ela mais bonita e organizada - já está no utils.py e tarefas.py
limpar = []

carregar_dados = []  # função para carregar os dados adcionados nos arquivos, detalhe o prório vs.code gerou o arquivo json. depois pesquesei as maneiras de utlizar ele.

salvar_dados = []    # função para salvar os dados adicionados nos arquivos, detalhe o prório vs.code gerou o arquivo json.

adicionar_transacao = []   # função para adicionar transações, contendo as informações necessárias para rodar o sistema.

listar_transacoes = []     # função para listar as transações, mostrando as informações necessárias. Aqui adicionamos a funçao de Lista.

remover_transacao = []     # função para remover transações, mostrando as informações necessárias para escolher a transação a ser removida.

saldo_atual = []           # função para mostrar o saldo atual disponível.

analise_financeira = []    #A ideia aqui foi para deixar organizado e mostrar todas as receitas/gastos do usuário de forma organizada.

despesas_a_pagar = []     #Uma lista para armazenar as contas que o usuário deseja pagar.

pagar_despesas = []       #FIFO - Lista de despesas a pagar mostrando a mais antiga no topo.

despesas_pagas = []       #LIFO - Lista de despesas pagas mostrando a mais recente no topo.

adicionar_salario = []

salario = ["receita"]     #Após juntar essas variaveis conseguir rodar a opção de saldo atual, pois estava separada e tava dando erro no saldo.

#Detalhe importante, pesqusei no CHAT GPT ele informou e explicou o uso do json e essa variavel para facilitar alterações futuras, ainda tenho muitas duvidas de como ela funciona.
arquivo = "dados.json"  # Variável para armazenar o nome do arquivo onde os dados serão salvos e carregados. Facilita a manutenção do código, caso seja necessário mudar o nome do arquivo no futuro.

#A escolha de um gerenciador financeiro foi por 2 motivos, Primeiro para mim (Ericles) foi por conta que eu ja pensava em algo para
#me ajudar com as minhas contas e organizar minhas finanças pessoais, mas queira fazer um teste em programar para ver.
#o segundo motivo foi do (Nathan) ele achou uma funionalidae util para o dia a dia, então chegamos a conslusão dessa escolha.