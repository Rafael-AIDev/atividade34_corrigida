try:
    numero = int(input('Informe um número: '))

    print(f'{numero} é par.' if numero % 2 == 0 else f'{numero} é ímpar')

except Exception as e:
    print(f'Não foi possível verificar o número. {e}.')