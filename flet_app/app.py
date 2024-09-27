import flet as ft

# função principal
def main(page: ft.Page):
    # ação do evento on_change
    def acao(e):# esse e é de evento
        result.value = texto.value
        page.update()
    #configuração da janela
    page.title = "Meu Flet App"
    page.scroll = "adaptative"
    page.theme_mode = ft.ThemeMode.LIGHT

    #declaração de variáveis
    texto = ft.TextField(label="Digite aqui o seu texto", on_change=acao)# tipo caixa de texto, ps a ação deve ser criada dentro do main, on_change é em tempo real
    result = ft.Text(size=30)

    #Conteúdo da janela
    page.add(
        texto,
        result
    )

    # atualização da janela
    page.update()

#executa a aplicação
ft.app(main)