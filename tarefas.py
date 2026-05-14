## Aqui estão as Variaveis globais uliizadas no Gerenciador Financeiro
limpar = []
carregar_dados = []
salvar_dados = [] 
adicionar_transacao = []
listar_transacoes = []
remover_transacao = []
saldo_atual = []
analise_financeira = []
arquivo = "dados.json"

#Esse import "json" é para salvar os dados
# esse import "os" é para limpar a tela, pesquisei antes de adicionar, ele serve para limpar tela de wiondows.
import json
import os
import utils

#Uma observação para deixar claro, não tenho conhecimento de importação de j.son e nem como usar um limpa tela.
#então abri o youtube pesquisei e segui alguns passos para fazer, conseguir implementar graças a um tutorial.

import json

try:
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
except:
    dados = []
    
def salvar_dados(dados):
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_dados():
    try:
        with open("dados.json", "r") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "transacoes": []
        }
        
#A aprtir daqui fui fazendo e testanto funções, pesquisando erros e os concertando.

def adicionar_transacao():
    dados = carregar_dados()
    tipo = input("Tipo (receita/despesa): ")
    valor = float(input("Valor: "))
    categoria = input("Categoria: ")
    descricao = input("Descrição: ")
    data = input("Data (DD/MM/AAAA): ")
    transacao = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
        "data": data,
        "status": "pendente"
    }
    dados["transacoes"].append(transacao)
    salvar_dados(dados)
    print("Transação adicionada com sucesso!")
    
#Caso adicione uma informação errada ele pode excluir e colocar novamente.
def remover_transacao():
    dados = carregar_dados()
    listar_transacoes()
    escolha = int(input("Escolha o número da transação que deseja remover: "))
    if escolha >= 0 and escolha < len(dados["transacoes"]):
        transacao_removida = dados["transacoes"].pop(escolha)
        salvar_dados(dados)
        print(f"Transação '{transacao_removida['descricao']}' removida com sucesso.")
    else:
        print("Opção inválida.")
        return
        
#Aqui usei return para garantir caso não tenha adicionado nada, estava com tendo problema pra ele listar sem adicionar nada.
def listar_transacoes():
    dados = carregar_dados()

    if not dados["transacoes"]:
        print("Nenhuma transação cadastrada.")
        return

    for i, transacao in enumerate(dados["transacoes"]):
        print(
            f"{i} - Tipo: {transacao['tipo']}, "
            f"Valor: R$ {transacao['valor']:.2f}, "
            f"Categoria: {transacao['categoria']}"
        )

#Tive um pouco de dificuldade para fazer funcioanar, mas tentativas de erro conseguir arrumar.
def saldo_atual():
    dados = carregar_dados()
    #Aqui só tinha faltado colocar o valor para saldo uma coisa simples de resolver , tava tão afoito que não prestei atenção.
    saldo = 0
    
    for transacao in dados["transacoes"]:
        
        if transacao["tipo"] == "receita":
            saldo += transacao["valor"]

        elif transacao["tipo"] == "despesa":
            saldo -= transacao["valor"]
    print(f"Saldo atual: R$ {saldo:.2f}")
    
 #Para dar um claresa dos gastos, ganhos , saldo em uma só lista , assim facilita a leitura.
def analise_financeira():
    dados = carregar_dados()
    try:
        total_receitas = 0
        total_despesas = 0
        for transacao in dados["transacoes"]:
            if transacao["tipo"] == "receita":
                total_receitas += transacao["valor"]
            elif transacao["tipo"] == "despesa":
                total_despesas += transacao["valor"]
        saldo = total_receitas - total_despesas
        print("====== Relatório Finaceiro ======")
        print(f"Total de receitas: R$ {total_receitas:.2f}")
        print(f"Total de despesas: R$ {total_despesas:.2f}")    
        print(f"Saldo: R$ {saldo:.2f}")
    except FileNotFoundError:
        print("Nenhum dado foi inserido ainda!!")

# Fiz essa função para gerar um lista de pagamento que o usuário adicionar como "despesa"
def fila_pagamentos():
    dados = carregar_dados()

    for transacao in dados["transacoes"]:
        if transacao["tipo"] == "despesa":
            print(
                f"Categoria: {transacao['categoria']} | "
                f"Valor: R$ {transacao['valor']:.2f}"
            )
            salvar_dados(dados)

#Assim caso deseje realizar o pagamento, essa função gera a lista de despesas para efetuar o pagamento
def pagar_despesas():
    dados = carregar_dados()
    fila_pagamentos = []
    
    for transacao in dados["transacoes"]:
        if transacao["tipo"] == "despesa":
            fila_pagamentos.append(transacao)      #buscar apenas as despesas.

    # Aqui  é pra olhar se existe despesas adicionada.
    if len(fila_pagamentos) == 0:
        print("Não há despesas a pagar.")
        return

    print("=== Despesas a pagar ===")

    for i, despesa in enumerate(fila_pagamentos):
        print(
            f"{i} - {despesa['categoria']} | "
            f"R$ {despesa['valor']:.2f}"
        )
    escolha = int(input("Escolha o número da despesa: "))
    if 0 <= escolha < len(fila_pagamentos):
        despesa_paga = fila_pagamentos[escolha]
        despesa_paga["status"] = "pago"
        salvar_dados(dados)
        print("Despesa paga com sucesso!")
    else:
        print("Opção inválida.")

#Com isso aqui faz uma pilha do que foi pago, e evita o usuário de repetir a conta, ou até mesmo dele esquecer que pagou.
def pilha_pagamento_realizados():
    dados = carregar_dados()
    despesas_pagas = []
    for transacao in dados["transacoes"]:
        if (
            transacao["tipo"] == "despesa"
            and transacao.get("status") == "pago"
        ):
            despesas_pagas.append(transacao)
    if len(despesas_pagas) == 0:
        print("Nenhuma despesa foi paga.")
        return
    
    print("\n=== DESPESAS PAGAS ===")
    for i, despesa in enumerate(despesas_pagas):
        print(
            f"{i} - "
            f"{despesa['categoria']} | "
            f"R$ {despesa['valor']:.2f}"
        )
    