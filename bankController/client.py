class Cliente:
    def __init__(self, n, fone):
        self.nome = n
        self.telefone = fone

class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular