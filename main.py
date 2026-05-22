# main.py do projeto financeiro
#coloquei todos os imports que trazem os dados salvos.
from dados import *
from utils import *
from tarefas import *

#Esse é o Painel que será utlizado.
#Antes de tudo fiz o Painel primeiro, para ter uma noção do que fazer nas tarefas e adicionar as funções no dados.py.
while True:
        print("\n ============== Gerenciador de Finanças Pessoais ===================")
        print("1 - Adicionar transação                  2 - Listar transações")
        print("3 - Remover transação                    4 - Análise financeira")
        print("5 - Despesas a pagar                     6 - Pagar despesas  ")
        print("7 - Despesas Pagas                       8 - Saldo atual")
        print("9 - Sair")
        print("\n ===================================================================")
        opcao = input("\nEscolha: ")
        
       
        if opcao == "1":
            adicionar_transacao()
            
        elif opcao == "2":
            listar_transacoes()
            
        elif opcao == "3":
            remover_transacao()
            
        elif opcao == "4":
            analise_financeira()
            
        elif opcao == "5":
            fila_pagamentos()
            
        elif opcao == "6":
            pagar_despesas()
            
        elif opcao == "7":
            pilha_pagamento_realizados()
            
        elif opcao == "8":
            saldo_atual()
            
        elif opcao == "9":
            limpar()
            print("Por hoje é isso. Seu controle financeiro está em dia e tudo foi salvo automaticamente. Te esperamos na próxima.") 
            break
        else:
            print("Opção inválida")
