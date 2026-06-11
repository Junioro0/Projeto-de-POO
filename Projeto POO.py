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

    def fazer_pedido(self, entregador, produtos):
        return Pedido(self, produtos, entregador)

class Funcionario(Pessoa):
    def __init__(self, nome, telefone, cpf, salario):
        super().__init__(nome, telefone, cpf)
        self.salario = salario

    def mostrar_funcao(self):
        print(f"\n{self.nome} é um funcionário do restaurante. ")   

    def calcular_bonus(self):
        return self.salario * 0.10
    
class Entregador(Funcionario):
    def __init__(self, nome, telefone, cpf, salario, veiculo, entregas_realizadas):
        super().__init__(nome, telefone, cpf, salario)
        self.veiculo = veiculo
        self.entregas_realizadas = entregas_realizadas

    def mostrar_funcao(self):
        print(f"\n{self.nome} é entregador e realiza entregas de {self.veiculo}. ")

    def realizar_entrega(self, pedido):
        self.entregas_realizadas += 1
        pedido.status = "Entregue"
        print("entrega realizada")
    
    def calcular_bonus(self):
        return self.entregas_realizadas * 5

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostrar_produto(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")

class Pedido:
    def __init__(self, cliente, produtos, entregador, status = "em preparo"):
        self.cliente = cliente
        self.produtos = produtos
        self.entregador = entregador
        self.status = status

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
        
    def pagamento_cliente(self):
        valor = self.calcular_total() + self.calcular_frete()
        print(f"Pagamento realizado: R${valor:.2f}")

# Exemplo de uso

clientes = []
produtos = []
entregadores = []
pedidos = []
itens_pedido = []

cliente1 = Cliente("João ", "(51) 12345-678", "123.456.789-01", "Rua A, 123")
funcionario1 = Funcionario("Luis", "(51) 01020-3040","167.999.123-76", 3000 )
entregador1 = Entregador("Henrique", "(51) 8765-4321", "109.876.543-21", 2000, "Moto", 67)
produto1 = Produto("X-Burguer", 25)
produto2 = Produto("Refrigerante", 8)
pedido1 = Pedido(cliente1, [produto1, produto2], entregador1)
#pedido1.mostrar_pedido()

clientes.append(cliente1)
entregadores.append(entregador1)
produtos.append(produto1)
produtos.append(produto2)

funcionarios = [funcionario1, entregador1]

print("\n-- Demonstração de Polimorfismo -- \n")

for f in funcionarios:
    print(f"{f.nome}: R${f.calcular_bonus()}")

while True:
    print ("\n --SISTEMA DE DELIVERY-- \n")
    print ("opcão 1: cadastrar cliente")
    print ("opção 2: cadastrar entregador")
    print ("opção 3: cadastrar produto")
    print ("opção 4: fazer pedido")
    print ("opção 5: atualizar status do pedido")
    print ("opção 6: mostrar funções")
    print ("opção 7: mostrar pedidos")
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
        pedido = cliente.fazer_pedido(entregador, itens_pedido)
        pedidos.append(pedido)
        pedido.pagamento_cliente()
        print(f"Pedido de {cliente.nome} criado com sucesso!")

    elif opcao == 5:
        if not pedidos:
            print("Nenhum pedido encontrado.")
            continue

        print("Pedidos:")
        for i, p in enumerate(pedidos, 1):
                print(f"  {i}. {p.cliente.nome} – Status: {p.status}")

        indice = int(input("Número do pedido: ")) - 1

        if indice < 0 or indice >= len(pedidos):
            print("Opção inválida.")
            continue
        
        novo_status = input("Novo status: ")
        pedidos[indice].status = novo_status

        print(f"Status atualizado para '{novo_status}'.")

    elif opcao == 6:
        pessoas = clientes + entregadores

        for pessoa in pessoas:
            pessoa.mostrar_funcao()

    elif opcao == 7:

        if not pedidos:
            print("Nenhum pedido cadastrado.")
            continue

        for pedido in pedidos:
            pedido.mostrar_pedido()

    else:    print("Opção inválida.")
        