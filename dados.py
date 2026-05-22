# Dados que serão usados para funções do sistema de finanças
# LIFO,FIFO o status e categorias foi implementado no adicionar transação
# Assim o tipo de categoria fica disponivel para a escolha do usuário

fila_pagamentos = []
''' - Uma lista para armazenar as contas que o usuário deseja pagar. estrutura FIFO'''
pagar_despesas = []
''' - Lista de despesas a pagar mostrando a mais antiga no topo. estrutura FIFO'''
pilha_pagamento_realizados = []
''' - Lista de despesas pagas mostrando a mais recente no topo. estrutura LIFO'''