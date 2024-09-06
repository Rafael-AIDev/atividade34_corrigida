import os

quadrado    = lambda l: l**2
circulo     = lambda r: 3.14*r**2
triangulo   = lambda b, h: (b*h)/2
trapezio    = lambda b_menor,b_maior,h: ((b_maior + b_menor)*h)/2

if __name__ == "__main__":
    while True:
        print('1- Quadrado')
        print('2- Círculo')
        print('3- Triângulo')
        print('4- Trapézio')
        print('5- Sair')

        opcao = input('Opção desejada: ')

        os.system('cls')

        match opcao:
            case '1':
                try:
                    lado = float(input('Informe o lado do quadrado: ').replace(',', '.'))
                    print(f'Área de quadrado: {quadrado(lado)}.')
                except Exception as e:
                    print(f'Não foi possível calcular a área . {e}.')
                finally:
                    continue

            case '3':
                try:
                    base = float(input('Informe a base  do triângulo: ').replace(',', '.'))
                    altura = float(input('Informe a altura  do triângulo: ').replace(',', '.'))
                    print(f'Área de quadrado: {triangulo(b, h))}.')
                except Exception as e:
                    print(f'Não foi possível calcular a área . {e}.')
                finally:
                    continue

# terminar o script, só copiar e mudar os nomes das variáveis
# a questão 12 já foi feita