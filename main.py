# main.py do projeto financeiro
#coloquei todos os imports que traz os dados salvos.
from dados import *
from utils import *
from tarefas import *

#Esse é o Painel que será utlizado.
#Antes de tudo fiz o Painel primeiro, para ter uma noção do que fazer nas tarefas e adicionar as funções no dados.py.
while True:
        print("\n === Gerenciador de Finanças Pessoais ==========")
        print("1 - Adicionar Salário")
        print("2 - Adicionar transação")
        print("3 - Listar transações")
        print("4 - Remover transação")
        print("5 - Análise financeira")
        print("6 - Despesas a pagar")
        print("7 - Pagar despesas")
        print("8 - Despesas pagas")
        print("9 - Saldo atual")
        print("0 - Sair")
        opcao = input("\nEscolha: ")
        

        if opcao == "1":
            adicionar_salario()
            
        elif opcao == "2":
            adicionar_transacao()
            
        elif opcao == "3":
            listar_transacoes()
            
        elif opcao == "4":
            remover_transacao()
            
        elif opcao == "5":
            analise_financeira()
            
        elif opcao == "6":
            despesas_a_pagar()
            
        elif opcao == "7":
            pagar_despesas()
            
        elif opcao == "8":
            despesas_pagas()
            
        elif opcao == "9":
            saldo_atual()
            
        elif opcao == "0":
            limpar()
            print("Por hoje é isso. Seu controle financeiro está em dia e tudo foi salvo automaticamente. Te esperamos na próxima.") 
            break
        else:
            print("Opção inválida")