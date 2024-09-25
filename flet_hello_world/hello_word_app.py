import flet as ft

def main(page: ft.Page): # colocar as outras funções dentro da função main
    page.title = "Olá Mundo!"
    page.scroll = "adaptative"

    #declaração de variáveis
    nome = ft.TextField(label='Nome')
    texto = 'Meu texto'
    # para adicionar alguma coisa é dentro do page.add
    page.add(
        ft.Text('Olá, mundo!', size=30, color='#FAEBD7', weight='bold'),
        #ft.TextField(label='Nome')
        nome,
        ft.TextButton('Clique aqui'),
       ft.Text(texto)
    )
    page.update()

ft.app(main)# serve para executar o programa a janelinha