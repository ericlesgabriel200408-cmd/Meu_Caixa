import json
import os

def mostrar_dados():                                                # Mostrar os dados que forem adicionados.
    dados = carregar_dados()
    for transacao in dados:
        print(f"Tipo: {transacao['tipo']}, Valor: {transacao['valor']}, Categoria: {transacao['categoria']}, Descrição: {transacao['descricao']}, Data: {transacao['data']}")

def limpar():
    os.system("cls")                                                # Limpa a tela no Windows
    
def salvar_dados(transacoes):
    with open("dados.json", "w") as arquivo:                        # Salva os dados em um arquivo Json para facilitar e evitar perdas de dados
        json.dump(transacoes, arquivo)
def carregar_dados():
    try:
        with open("dados.json", "r") as arquivo:                    # Carrega os dados do arquivo Json para o programa
            return json.load(arquivo)
    except FileNotFoundError:                                       # Retorna uma lista vazia se o arquivo não existir.
        return []                                                   # (Observação: usei a IA nesse momento para consultar como facilitar o salvamento e arquivos de dados pois estava com dúvidas nessa parte.)
    
def adicionar_transacao():                                          # Adicionada para facilitar a adição de transações, contendo as informações necesárias.
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
        "data": data
    }
    dados.append(transacao)
    salvar_dados(dados)

def listar_transacoes():   # Função obriatória para listar as transações, escrevi o print em uma linha para diminuir o tamanho do código.
    dados = carregar_dados()
    for transacao in dados:
        print(f"Tipo: {transacao['tipo']}, Valor: {transacao['valor']}, Categoria: {transacao['categoria']}, Descrição: {transacao['descricao']}, Data: {transacao['data']}")

def remover_transacao():   # Função obrigatória para remover trasações de escolha do usuáro.
    dados = carregar_dados()
    listar_transacoes()
    lista = int(input(" Escolha o número da trasanção que deseja remover: "))
    if lista >= 0 and lista < len(dados):
        del dados[lista]
        salvar_dados(dados)
    else:
        print("Opção inválida.")
        
def saldo_atual():        # Função para mostrar o saldo atual disponível, somando as receitas e subtraindo as despesas.
    dados = carregar_dados()
    saldo = 0
    for transacao in dados:
        if transacao["tipo"] == "receita":
            saldo += transacao["valor"]
        elif transacao["tipo"] == "despesa":
            saldo -= transacao["valor"]
    print(f"Saldo atual: R$ {saldo:.2f}")             #coloquei o 2f para mostrar duas casas decimais, deixar mais bonito e caso tenha valor de centavos.
    
def analise_financeira():  # Função para análise financeira, mostrando o total de receitas, despesas e saldo.
    dados = carregar_dados()
    total_receitas = 0
    total_despesas = 0
    for transacao in dados:
        if transacao["tipo"] == "receita":
            total_receitas += transacao["valor"]
        elif transacao["tipo"] == "despesa":
            total_despesas += transacao["valor"]
    saldo = total_receitas - total_despesas             # Cálculo do saldo para mostrar na análise financeira. Pro usuário ter uma visão geral de suas finanças e não apenas do saldo atual.
    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")    
    print(f"Saldo: R$ {saldo:.2f}")
    
def status():              # Função para mostrar o status financeiro, mostrando se o usuário está no azul ou no vermelho.
    dados = carregar_dados()
    saldo = 0
    for transacao in dados:
        if transacao["tipo"] == "receita":
            saldo += transacao["valor"]
        elif transacao["tipo"] == "despesa":
            saldo -= transacao["valor"]
    if saldo >= 0:
        print("Status: No azul")
    else:
        print("Status: No vermelho")