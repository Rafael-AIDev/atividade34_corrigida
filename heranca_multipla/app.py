from modulo import *

if __name__ == "__main__":
    # instancia objeto da subclasse
    h = Filho('','','','',0.0,0.0,'')

    # entrada de dados
    h.nome = input('Informe o nome: ')
    h.email = input('Informe o email: ')
    h.profissao = input('Informe a profissao: ')
    h.olhos = input('Informe a cor dos olhos: ')
    h.peso = float(input('Informe o peso em kg: ').replace(',','.'))
    h.altura = float(input('Informe a altura em metros: ').replace(',','.'))
    h.cor_cabelo = input('Informe a cor dos cabelos: ')

    '''
    print(h.nome)
    print(h.email)
    print(h.profissao)
    print(h.olhos)
    print(h.peso)
    print(h.altura)
    print(h.cor_cabelo)
    '''
    # saída de dados
    h.exibir_cartao_visitas()
    h.exibir_físico()