#Esse import json é para salvar os dados, esse import os é para limpar a tela, pesquisei antes de adicionar, ele serve para limpar tela de wiondows.
import json
import os

#Uma observação para deixar claro, não tenho conhecimento de importação de j.son e nem como usar um limpa tela.
#então abri o youtube pesquisei e segui alguns passos para fazer, conseguir implementar graças a um tutorial.

def limpar():
    os.system("cls")
    
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
            "salario": 0,
            "transacoes": []
        }
        
#A aprtir daqui fui fazendo e testanto funções, pesquisando erros e os concertando.

#Foi colocado uma função de Salário a parte, assim o usuário não precisa ficar revendo, pois ficara salvo, ele precisará apenas informar o que será receita adicional e despesas.
def adicionar_salario():
    salario = float(input("Digite o valor do seu salário líquido: R$ "))
    dados["salario"] = salario
    dados = carregar_dados()
    
    salvar_dados(dados)

    print("Salário adicionado com sucesso!")

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

#Tive um pouco de dificuldade para fazer funcioanar, pois receita e salario tinha feito como variaveis separadas, após juntar funcionou.
def saldo_atual():
    dados = carregar_dados()
    
    saldo = dados["salario"]
    
    for transacao in dados["transacoes"]:
        
        if transacao["tipo"] == "receita":
            saldo += transacao["valor"]
            
        elif transacao["tipo"] == "despesa":
            saldo -= transacao["valor"]

    print(f"Saldo atual: R$ {saldo:.2f}")
    
 #Para dar um claresa dos gastos, gasnhos , saldo em uma só lista , assim facilita a leitura.
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
        saldo = total_receitas - total_despesas             # Cálculo do saldo para mostrar na análise financeira. Pro usuário ter uma visão geral de suas finanças e não apenas do saldo atual.
        print("====== Relatório Finaceiro ======")
        print(f"Total de receitas: R$ {total_receitas:.2f}")
        print(f"Total de despesas: R$ {total_despesas:.2f}")    
        print(f"Saldo: R$ {saldo:.2f}")
    except FileNotFoundError:
        print("Nenhum dado foi inserido ainda!!")

 #Coloquei essa função pois não tinha sentido ser considerado despesas e não incluir ela para pagar depois.
def despesas_a_pagar():
    dados = carregar_dados()

    for transacao in dados["transacoes"]:
        if transacao["tipo"] == "despesa":
            print(
                f"Categoria: {transacao['categoria']} | "
                f"Valor: R$ {transacao['valor']:.2f}"
            )
            salvar_dados(dados)

#Assim caso deseje pagar e reitar menos 1 dos gastos deixa mais simples o uso.
def pagar_despesas():
    dados = carregar_dados()
    despesas_a_pagar = []
    
    for transacao in dados["transacoes"]:
        if transacao["tipo"] == "despesa":
            despesas_a_pagar.append(transacao)      #buscar apenas as despesas.

    # Aqui  é pra olhar se existe despesas adicionada.
    if len(despesas_a_pagar) == 0:
        print("Não há despesas a pagar.")
        return

    print("=== Despesas a pagar ===")

    for i, despesa in enumerate(despesas_a_pagar):
        print(
            f"{i} - {despesa['categoria']} | "
            f"R$ {despesa['valor']:.2f}"
        )
    escolha = int(input("Escolha o número da despesa: "))
    if 0 <= escolha < len(despesas_a_pagar):
        despesa_paga = despesas_a_pagar[escolha]
        despesa_paga["status"] = "pago"
        salvar_dados(dados)
        print("Despesa paga com sucesso!")
    else:
        print("Opção inválida.")

#Com isso aqui liata o que foi pago, e evita o usuário de repetir a conta, ou até mesmo dele esquecer que pagou.
def despesas_pagas():
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
    