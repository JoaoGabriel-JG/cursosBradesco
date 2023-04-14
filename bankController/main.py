from client import Cliente, Conta

c1 = Cliente('Leonardo', '119999-9999')
conta = Conta(c1.nome , 6565, 0)

print(c1.nome, ' e ', c1.telefone)
print(conta.titular, ' número: ', conta.numero, ' seu saldo: ', conta.saldo)
