# Importando biblioteca
import flet as ft

def main(page: ft.Page):
    # Evento de calcular IMC
    def calcular_imc(e):
        try:
            # Obtendo valores de peso e altura
            peso_valor = float(peso.value)
            altura_valor = float(altura.value)

            # Calcula o IMC
            imc = peso_valor / (altura_valor ** 2)

            # Classificação do IMC
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif 18.5 <= imc < 24.9:
                classificacao = "Peso normal"
            elif 25 <= imc < 29.9:
                classificacao = "Sobrepeso"
            elif 30 <= imc < 34.9:
                classificacao = "Obesidade grau 1"
            elif 35 <= imc < 39.9:
                classificacao = "Obesidade grau 2"
            else:
                classificacao = "Obesidade grau 3"

            # Atualiza o resultado
            result.value = f'{nome.value}, IMC: {imc:.2f}, Classificação: {classificacao}.'
        except ValueError:
            result.value = "Por favor, insira valores válidos para peso e altura."

        # Limpa os campos de entrada
        nome.value = ''
        peso.value = ''
        altura.value = ''

        page.update()

    page.title = "Calcular IMC"
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de entrada
    nome = ft.TextField(label='Nome')
    peso = ft.TextField(label='Peso', suffix_text='kg')
    altura = ft.TextField(label='Altura', suffix_text='m')
    result = ft.Text(size=30)

    # Adiciona elementos à página
    page.add(
        ft.Row(
            [ft.Text('Calcular IMC', size=40, weight='bold')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [peso],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [altura],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Calcular IMC", on_click=calcular_imc)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)