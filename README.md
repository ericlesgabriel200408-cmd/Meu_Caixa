### Olá , somos o grupo 28, composto por Ericles e Nathan. Abaixo está uma descrição de nosso projeto, suas funcionalidades e motivos da escolha.

1.
• Nome do projeto: Meu Caixa
• Tema escolhido: Controle Financeiro Pessoal
• Grupo: 28
• Integrantes: Ericles Gabriel Clemente Queiroz / Nathan Gabriel Nunes dos Santos
• Período/Turma: Matutino / 42_32160_Presencial_90

2.
• FIFO é uma fila onde o primeiro que entra é o primeiro que sai, no programa foi usada no Fila_pagamentos e despesas_pagas, para mostrar a primeria transação.
• LIFO é onde o ultimo que entrar é o primerio a sair, no programa ele foi utilizado no pilha_pagamentos_realizados.
• Não olhei muito pro lado do dicionário e ele foi tulizados apenas na ultima def do tarefas.py ele foi utilizado como .get na pilha_pagamentos_realizados.
• Lista e Tupla, Lista ela nos permite alterar informações, e a tupla ela é imutável.
• A lista foi utilizada nas variações globais para listar tudo e ficar no banco de dados para acessa-los sempre que possivel.
• A tupla foi ulizada com frequência para salvamento de dados e carregamentos de dados, assim não teria qualquer tipo de alteração no conteúdo já informado, garantindo melhor funcionamento das informações.
• Modularização ela é a divisão de partes de um programa, no caso nosso projeto foi dividido em 6 partes, sendo elas: Dados.py , Main.py , Tarefas.py , Utils.py , Readme.md e Changelog.md.

3. Como executar o projeto
• Versão do Python 3.12.3 
• Comando para executar no Terminal: python main.py
• Não temos nenhuma biblioteca externa, apenas padrões.

4.
Requisitos obrigatórios
• Cadastrar transação (descrição, valor, tipo: receita/despesa, categoria) ficou no adicionar transação
• Listar todas as transações com status: apenas as despesas.
• Fila de despesas pendentes — FIFO: mais antiga paga primeiro ficou no Despesas a pagar e Pagar despesas.
• Pilha de pagamentos realizados — LIFO: ficou no Despegas Pagas - Pilha_pagamento.
• Atualizar status: foi implementado diretamente no pagar despesas que logo após consta paga.
• Exibir saldo atual (receitas - despesas pagas) - Ele informa o saldo líquido que sobra para o usuário.
• Não foi utilizado bônus, mas usamos as dicas do try/except.

5. Dificuldades e aprendizados

• Durante Desenvolvimento/teste, estava tendo problemas com calculo e saldo, mesmo excluindo e adicionando coisas para concertar, descobrimos e aprendenmos uma coisa nova sobre o Json, mesmo concertando entava dando erro no calculo onde descobrimos que os dados ainda estavam salvos no json, então passamos a excluir e reiterar com novas informações conforme necessidade.
• Funções Desnecessárias, colocamos funções sem utlidade, onde ocupava espaço e atrapalhava o funcionamento do código. Então apredenemos a usar o que é necesserário que funcione antes de montar beleza, uma base firme para depois expandir.
• Importações é bem dificil de enteder, principalemnte para salvar dados, utilizei um tutorial para implementar e ainda tenho dúvidas que vou tentando aprender sobre.
