class contabancaria:
    """
Cria uma conta bancaria e permite fazer saques e depositos

    """
    def __init__(self, id, titular, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f"conta {self.id} criada com sucesso para {self.titular} com saldo inicial de R${self.saldo:.2f}.")  
    def __str__(self):
        return f"A Conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} realizado com sucesso na conta {self.id}.")
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente para saque de R${valor:,.2f} na conta {self.id}.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado com sucesso na conta {self.id}.")

c1 = contabancaria( 1, "João", 3000)
c1.depositar(500)
c1.sacar(200000)
print(c1)