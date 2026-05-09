# main.py do projeto financeiro
from dados import *
from utils import *
from tarefas import *
def menu():
    while True:
        
        print("\n === Gerenciador de Finanças Pessoais ==========")
        print("1 - Adicionar transação")
        print("2 - Listar transações")
        print("3 - Remover transação")
        print("4 - Análise financeira")
        print("5 - Status")
        print("6 - Pagar despesas")
        print("7 - Despesas pagas")
        print("8 - Saldo atual")
        print("0 - Sair")
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
            status()
            
        elif opcao == "6":
            pagar_despesas()
            
        elif opcao == "7":
            despesas_pagas()
            
        elif opcao == "8":
            saldo_atual()
            
        elif opcao == "0":
            limpar()
            print("Por hoje é isso. Seu controle financeiro está em dia e tudo foi salvo automaticamente. Te esperamos na próxima.")
            
            limpar()
            break
        else:
            print("Opção inválida")

menu()