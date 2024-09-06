
nomes = ['Alex', 'Alexandre', 'Fulano', 'Cicrano', 'Beltrano', 'Alexandra', 'Joana', 'Maria', 'José', 'João']
try:
    indice = int(input('Informe um índice: '))

    print(nomes[indice] if indice >= 0 and indice < 10 else 'Índice inexistente') 
    # operador ternário e if / else para delimitar o índice, caso contrario o python não retorna corretamente ou vai por ultimo ou para o primeiro, diferente das outras linguagens
except Exception as e:
    print(f'Não foi possível retornar o nome da lista. {e}.')