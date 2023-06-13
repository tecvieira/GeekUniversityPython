"""
" Desenvolver um aplicativo para facilitar suas idas ao supermercado. Pediu um software que controlasse
uma lista de compras de supermercado. A proposta é a seguinte: A pessoa cadastra o produto e a quantidade
que precisar. O usuário ao ir ao supermercado localiza o produto e digita o preço unitário. Ao encerrar
as compras uma opção mostra ao usuário o valor total de suas compras para conferencia no caixa.
 Utilize o menu abaixo para ajudar a montar sua solução.
 Menu
 0- Fim 1- Cadastra Produtos
 2- Confere Lista de Produtos
 3- Confirma Produto
 4- Mostra Total a pagar Escolha:

Na opção 1 – deverá ser cadastrado o produto em uma lista chamada listaDeProdutos e a quantidade desejada
em uma lista chamada listaDeQuantidades. Para facilitar, podemos abstrair detalhes tipo (Kg, unidade,
volume, etc)

Na opção 2 – deverá ser mostrado dos dados cadastrados para conferência. Quando o produto já tiver no carrinho,
coloque um “OK” antes do nome. Exemplo:
Lista para conferência: Carne moída
– 1 Bolacha Maria
– 3 Ok - Chocolate
– 3 Fralda
- 2 Ok - Pão
- 8 Ok - Cerveja
Na opção 3 – você deverá localizar o produto e digitar o preço.
 O preço deverá ser digitado na listaDePrecos. Não esquecendo que o preço digitado deverá corresponder a
mesma posição do produto na listaDeProdutos. Exemplo, o chocolate está na posição [2] da listaDeProdutos,
portanto, seu preço deverá ficar na posição [2] na listaDePrecos. Na opção 4 – Deverás mostrar os produtos
que não foram comprados, os produtos que foram comprados e o preço total.
"""


escolha = 5
lista = []

while escolha != "0":
  print("Menu")
  print("0 - Fim")
  print("1 - Cadastra Produtos")
  print("2 - Confere Lista de Produtos")
  print("3 - Confirma Produto")
  print("4 - Mostra Total")
  escolha=input("Escolha uma opção:")
  if escolha == "0":
    escolha=input("Tem certeza que quer sair? 0 - Sim , 5 - Não")
  if escolha =="1":
    print("Cadastrando produto...")
    produto=input("Escolha o nome do produto:")
    quantidade=input("Escolha a quantidade do produto:")
    lista.append(["", produto, quantidade, 0])
  if escolha == "2":
    print("Exibindo produtos...")
    contador = 0
    for produto in lista:

      print(contador, "#", produto[0], " ", produto[1], "-", produto[2])
      contador=contador+1
  if escolha == "3":
    print("Confirmando produto...")
    posicao=input("Digite a posição do produto:")
    posicao_int = int(posicao)
    preco=input("Digite o preco do "+lista[posicao_int][1] + ":")
    lista[posicao_int][0] = "OK"
    lista[posicao_int][3] = preco
  if escolha == "4":
    print("Mostrando Todos Produtos...")
    print("Produtos que não foram comprados...")
    contador = 0
    for produto in lista:
      if produto[0] == "":
        print(contador,"#",produto[0], " ", produto[1], "-", produto[2], "R$", produto[3])
        contador=contador+1
    print("Produtos que foram comprados...")
    contador=0
    precototal=0
    for produto in lista:
      if produto[0] == "OK":
        print(contador, "#", produto[0], " ", produto[1], "-", produto[2], "R$", produto[3])
        contador=contador+1
        precototal=precototal+int(produto[2])*float(produto[3])
    print("Preco Total: R$", precototal)


print("Fim do programa!")
