import os 
import time

try:
    numero = int(input('Informe um número inteiro positivo: '))

    os.system('cls')

    print( 'Contagem regressiva')
    for i in range(numero, -1, -1):
         # tipo de range, a quantidade de vezes, segundo parâmetro até onde a repetição vai, depois, o terceiro parâmetro o número de passos
         print(f'{i}...')
         time.sleep(1)
         os.system('cls')
except Exception as e:
     print(f'Não foi possível realizar a contagem. {e}.')