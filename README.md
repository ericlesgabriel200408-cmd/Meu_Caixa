#  Meu Caixa, um Gerenciador de Finanças Pessoais em Python

> - **Projeto Final de Programação de Computadores** 
> - **Entrega: 21/05/2026** 
> - **Profa. Andrea Ono Sakai** 
> - **Turma: Matutino/(42_32160_Presencial_90)** 

---

###  Grupo 28 - Integrantes
* **Ericles Gabriel Clemente Queiroz**
* **Nathan Gabriel Nunes dos Santos**

Abaixo está a descrição detalhada do nosso projeto.

---

## 1. Sobre o Projeto e Escolha do Tema
O projeto consiste em um sistema de **Controle Financeiro Pessoal**. A escolha partiu da nossa necessecidade, e utilidade em si do projeto, em organizar nossas próprias contas e despesas no dia a dia, com o bônus de mesmo após o termino do projeto, continuar sendo usado e aprimorado.

---

## 2. Conceitos de Estrutura de Dados Utilizados

* **Fila - FIFO (First In, First Out):** Aplicada no gerenciamento de despesas a pagar. No sistema, as funções `fila_pagamentos()` e `pagar_despesas()` simulam essa estrutura. Os novos gastos entram no final da fila e, idealmente, a conta mais antiga deve ser visualizada primeiro.
* **Pilha - LIFO (Last In, First Out):** Aplicada no histórico de contas já pagas. A função `pilha_pagamento_realizados()` agrupa as contas com o status `"pago"`. A lógica de pilha garante que os últimos pagamentos realizados fiquem posicionados no topo para facilitar a conferência das movimentações mais recentes.
* **Dicionários:** É a estrutura central de dados do programa. Cada movimentação cadastrada é guardada como um dicionário contendo as chaves: `tipo`, `valor`, `categoria`, `descricao`, `data` e `status`.
* **Listas:** Utilizadas como coleções dinâmicas estruturadas (como `dados["transacoes"]`), que permitem adicionar, interagir com a listar(iterar) e remover elementos livremente antes de salvá-los no armazenamento.
* **Tuplas:** Utilizadas para `salvar_dados = []` e `carregar_dados = []` , garantindo a base dos dados nas tuplas.
* **Modularização:** O sistema foi dividido em **4 módulos funcionais de código**:
  * `main.py`: Contém o loop do painel interativo e os desvios condicionais (`if/elif`).
  * `dados.py`: Inicializa e define as estruturas de dados globais de persistência.
  * `tarefas.py`: Onde reside toda as funções globais, lógica de negócios, cálculos e filtros do sistema.
  * `utils.py`: Responsável por funções utilitárias do terminal, como o comando de limpar a tela.

---

## 3. Como Executar o Projeto

### Pré-requisitos
* **Python 3.12.3** (ou superior).
* O projeto foi construído utilizando apenas módulos nativos padrão do Python (`json` e `os`), e não foi usado biblioteca externa.

### Inicialização via Terminal
python main.py

---

## 4. Funcionalidades implementadas 
 Foram implementadas os requisitos do Tema "Controle Financeiro Pessoal":
   - Cadastrar transação (descrição, valor, tipo: receita/despesa, categoria) ficou no adicionar transação
   - Dicionários foi utilizado no adicionar trasação: tipo,categoria,data .
   - Listar todas as transações com status: apenas as despesas.
   - Fila de despesas pendentes — FIFO: mais antiga paga primeiro ficou no Despesas a pagar e Pagar despesas.
   - Pilha de pagamentos realizados — LIFO: ficou no Despegas Pagas - Pilha_pagamento.
   - Atualizar status: foi implementado diretamente no pagar despesas que logo após consta paga.
   - Exibir saldo atual (receitas - despesas pagas) - Ele informa o saldo líquido que sobra para o usuário.
   - Não foi utilizado bônus, mas usamos as dicas do try/except.

---

## 5. Dificuldades e aprendizados 
- Durante  a fase de desenvolvimento e testes, estavamos tendo problemas com os cálculos e saldos, mesmo excluindo e adicionando novas linhas de código para consertar os erros de cálculo. Aprendemos sobre .json e como suas funcionalidades servem para salvamento de dados, onde, o salvamentos dos valores de .json remanscente causavam conflito com os novos dados.  
