# NOTE: enunciado do programa
'''
Completem o programa: o usuário vai informar o nome e o CPF, e o programa informa qual a agência, conta e saldo. E aí o usuário vai poder escolher se deseja fazer saque, depósito ou sair do programa
herança multipla dé problema de manutenção de código, uma subclasse recebe métodos e atributos de duas superclasses
'''
import os
from modulo import *

if __name__ == "__main__":
    cc = ContaCorrente('Fulano', '123.456.789-12', '1001-1', '10010-1', 0)

    #entrada de dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o CPF do titular: ')

    while True:
        # saída de dados
        print(f'Nome: {cc.nome}.')
        print(f'CPF: {cc.cpf}.')
        print(f'Agência: {cc.agencia}.')
        print(f'Conta: {cc.conta}.')
        print(f'Saldo R$: {cc.conta}.')

        # NOTE: exibe  menu
        print('1 - Consultar o saldo')
        print('2 - Fazer depósito')
        print('3 - Fazer saque.')
        print('4 - Sair do programa')

        # usuário informa a opção desejada
        opcao = input('Informe a opção desejada: ')
         
        os. system('cls')
        match opcao:
            case '1':
                print('Consultar saldo\n')
                print(f'Saldo disponível: R$ {cc.consultar_saldo():,.2f}')
                continue
            case '2':
                valor = float(input('Informe o valor do depósito: R$ ').replace(',','.'))
                if valor > 0:
                    cc.saldo = cc.fazer_deposito(valor)
                    print('Depósito efetuado com sucesso')
                else:
                    print('Valor inválido.')
                continue
            case '3':
                valor = float(input('Valor do saque: R$ ').replace(',','.'))
                if valor <= cc.saldo:
                    cc.saldo = cc.fazer_saque(valor)
                    print('Saque efetuado com sucesso.')
                else:
                    print('Não foi possível efetuar o saque.')
                continue
            case '4':
                print('Programa encerrado')
                break
            case _:
                print('Opção inválida')
                continue
    






