# try/except evitar crash no programa e enviar uma mensagem de erro
# Exception mostra qual o tipo de erro
try:
    numero = float(input('Informe umn numero: '))

    print(numero)
    print(type(numero))
except Exception as e:
    print(f'Não foi possível realizar a operação. {e}.')