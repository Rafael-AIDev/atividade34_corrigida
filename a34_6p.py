import math

def primo(numero):
    if numero < 2:
        return False
    else:
        ...
    for i in range(2, int(math.sqrt(numero)) +1 ):
        if numero % i == 0:
            return False
        else:
            ...

    return True

if __name__ == '__main__':
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    print('Lista de números primos: ')

    for numero in numeros:
        if primo(numero):
            print(f'O número {numero} é primo')
        else:
            ...

# os três pontos significa para o python ignorar aquele trecho de código