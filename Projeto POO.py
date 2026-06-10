class Pessoa:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")

    def mostrar_funcao(self):
        print(f"\n{self.nome} é uma pessoa do sistema. ")
        
class Cliente(Pessoa):
    def __init__(self, nome, telefone, cpf, endereco):
        super().__init__(nome, telefone, cpf)
        self.endereco = endereco

    def mostrar_funcao(self):
        print(f"\n{self.nome} é um cliente e pode realizar pedidos. ")

    def fazer_pedido(self, pedido):
        print(f"\n{self.nome} fez um pedido: {pedido}")

class Funcionario(Pessoa):
    def __init__(self, nome, telefone, cpf, salario):
        super().__init__(nome, telefone, cpf)
        self.salario = salario

    def mostrar_funcao(self):
        print(f"\n{self.nome} é um funcionário do restaurante. ")   

class Entregador(Funcionario):
    def __init__(self, nome, telefone, cpf, salario, veiculo, entregas_realizadas):
        super().__init__(nome, telefone, cpf, salario)
        self.veiculo = veiculo
        self.entregas_realizadas = entregas_realizadas

    def mostrar_funcao(self):
        print(f"\n{self.nome} é entregador e realiza entregas de {self.veiculo}. ")

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostrar_detalhes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco}")
class Pedido:
    def __init__(self, cliente, produtos, entregador):
        self.cliente = cliente
        self.produtos = produtos
        self.entregador = entregador
        self.status = "Em preparo"
    def mostrar_pedido(self):
        print(f"Pedido de {self.cliente.nome}:")
        for produto in self.produtos:
            print(f"- {produto.nome}: R${produto.preco}")
        print(f"Total: R${self.calcular_total()}")
        print(f"Frete: R${self.calcular_frete()}")
        print(f"Entregador: {self.entregador.nome}")
        print(f"Status: {self.status}")
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    def remover_produto(self, produto):
        self.produtos.remove(produto)
    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total
    def calcular_frete(self):
        if self.calcular_total() > 100:
            return 0
        else:
            return 10
# Exemplo de uso
clientes = []
produtos = []
entregadores = []
pedidos = []
itens_pedido = []

cliente1 = Cliente("João ", "(51) 12345-678", "123.456.789-01", "Rua A, 123")
entregador1 = Entregador("Henrique", "(51) 8765-4321", "109.876.543-21", 2000, "Moto", 67)
produto1 = Produto("X-Burguer", 25)
produto2 = Produto("Refrigerante", 8)
pedido1 = Pedido(cliente1, [produto1, produto2], entregador1)
#pedido1.mostrar_pedido()

clientes.append(cliente1)
entregadores.append(entregador1)
produtos.append(produto1)
produtos.append(produto2)

while True:
    print ("--cadastro de clientes-- \n")
    print ("opcão 1: cadastrar cliente")
    print ("opção 2: cadastrar entregador")
    print ("opção 3: cadastrar produto")
    print ("opção 4: fazer pedido")
    print ("opção 5: atualizar status do pedido")
    print ("opção 6: mostrar funções")
    print ("opção 0: sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        print("Adeus")
        break

    if opcao == 1:
        nome = input("Nome do cliente: ")
        telefone = input("Telefone do cliente: ")
        cpf = input("CPF do cliente: ")
        endereco = input("Endereço do cliente: ")
        cliente = Cliente(nome, telefone, cpf, endereco)
        clientes.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado com sucesso!")

    elif opcao == 2:
        nome = input("Nome do entregador: ")
        telefone = input("Telefone do entregador: ")
        cpf = input("CPF do entregador: ")
        salario = float(input("Salário do entregador: "))
        veiculo = input("Veículo do entregador: ")
        entregador = Entregador(nome, telefone, cpf, salario, veiculo, 0)
        entregadores.append(entregador)
        print(f"Entregador {entregador.nome} cadastrado com sucesso!")

    elif opcao == 3:
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        produto = Produto(nome, preco)
        produtos.append(produto)
        print(f"Produto {produto.nome} cadastrado com sucesso!")

    elif opcao == 4:
        cliente_nome = input("Nome do cliente: ")
        cliente = next((c for c in clientes if c.nome == cliente_nome), None)
        if not cliente:
            print("Cliente não encontrado.")
            continue
        produto_nomes = input("Produtos (separados por vírgula): ").split(",")
        itens_pedido = []
        for nome in produto_nomes:
            produto = next((p for p in produtos if p.nome == nome.strip()), None)
            if produto:
                itens_pedido.append(produto)
            else:
                print(f"Produto '{nome.strip()}' não encontrado.")
            
        entregador_nome = input("Nome do entregador: ")
        entregador = next((e for e in entregadores if e.nome == entregador_nome), None)
        if not entregador:
            print("Entregador não encontrado.")
            continue
        pedido = Pedido(cliente, itens_pedido, entregador)
        pedidos.append(pedido)
        print(f"Pedido de {cliente.nome} criado com sucesso!")

    elif opcao == 5:
        if not pedidos:
            print("Nenhum pedido encontrado.")
            continue

        print("Pedidos:")
        for i, p in enumerate(pedidos, 1):
                print(f"  {i}. {p.cliente.nome} – Status: {p.status}")

        idx = int(input("Número do pedido: ")) - 1

        if idx < 0 or idx >= len(pedidos):
            print("Opção inválida.")
            continue
        
        novo_status = input("Novo status: ")
        pedidos[idx].status = novo_status

        print(f"Status atualizado para '{novo_status}'.")

    elif opcao == 6:
        pessoas = clientes + entregadores

        for pessoa in pessoas:
            pessoa.mostrar_funcao()

    else:    print("Opção inválida.")
        


