from modulo import *

if __name__ == "__main__":
    cc = ContaCorrente('Fulano', '123.456.789-12', '1001-1', '10010-1', 0)

    #entrada de dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o CPF do titular: ')

    # saída de dados
    print(f'Nome: {cc.nome}.')
    print(f'CPF: {cc.cpf}.')
    print(f'Agência: {cc.agencia}.')
    print(f'Conta: {cc.conta}.')


'''
Completem o programa: o usuário vai informar o nome e o CPF, e o programa informa qual a agência, conta e saldo. E aí o usuário vai poder escolher se deseja fazer saque, depósito ou sair do programa
'''