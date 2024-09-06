import os

nomes = []
# look infinito por causa da lista vazia
while True:
    novo_nome = input('Informe o novo nome ou deixe em branco para encerrar: ')
    os.system('cls')
    if novo_nome != '':
        try:
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.')
        except Exception as e:
            print(f'Não foi possível inserir o nome. {e}.')
        finally:
            # finally pertence ao try/except, ele executa o finally, mesmo se o try e o except forem executados
            continue

    else:
        break

nomes.sort()

print(f'Número de nomes na lista {len(nomes)}.')
for nome in nomes:
    print(nome)