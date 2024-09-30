# Importando biblioteca
import flet as ft
from deep_translator import GoogleTranslator

def main(page: ft.Page):
    page.title = "Tradutor"
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT

    # Evento de tradução
    def traduzir(e):
        try:
            # Obtendo texto do usuário
            texto_usuario = texto.value
            
            # Realiza a tradução
            traducao = GoogleTranslator(source='auto', target='pt').translate(texto_usuario)

            # Atualiza o resultado
            resultado.value = f'Tradução: {traducao}'
        except Exception as ex:
            resultado.value = f'Erro: {ex}'

        # Limpa o campo de entrada
        texto.value = ''
        page.update()

    # Campos de entrada
    texto = ft.TextField(label='Digite o texto a ser traduzido', multiline=True)
    resultado = ft.Text(size=20)

    # Adiciona elementos à página
    page.add(
        ft.Row(
            [ft.Text('Tradutor', size=40, weight='bold')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [texto],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Traduzir", on_click=traduzir)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [resultado],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)
