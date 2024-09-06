import os

notas = []

while True:
    opcao = input('1 para inserir nota ou 2 para calcular a média: ')
    os.system('cls')
    match opcao:
        case '1':
            try:
                nova_nota = float(input('Informe um valor de 0 a 10: ').replace(',', '.'))
                if nova_nota >= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print('Nota inserida com sucesso.')
                else:
                    print('Nova inválida')
            except Exception as e:
                print(f'Não foi possível inserir a nota. {e}.')
            finally:
                continue
        case '2':
            break
        case _:
            print('Opção inválida')
            continue
# o loop parou, mas o programa não, sai do loop e dá print
print(f'Média: {(sum(notas)/len(notas)):,.2f}')