# importa a biblioteca 
import json

# classe ArquivoJson/ não terá atributos apenas métodos
class Manipulador:
    def criar_arquivo(self, nome_arquivo):
        try:
            usuarios = [
                {
                    'Código': 0,
                    'Nome': 'Admin',
                    'CPF': '000.000.000-00',
                    'E-mail': 'admin@admin.com.br',
                    'Profissão': 'Administrador'
                }
            ]

            # serializar objeto python como json/ funciona o de cima como um dicionário, pega o dicionário acima, converte para um objeto json, depois faz a gravação
            json_dados = json.dumps(usuarios)
            with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as f:
                f.write(json_dados)
            return f'{nome_arquivo}.json criado com sucesso'
        except Exception as e:
            return f'Não foi possível criar o arquivo. {e}'


    def abrir_arquivo(self, nome_arquivo):
        # desserializando objeto em python
        with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return dados
    
    def salvar_dados(self, usuarios, nome_arquivo):
        try: 
            with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f) # para dump é para acrescentar novos dados, dumps é para quando for criar um novoa arquivo
            return f'Dados gravados com sucesso.'
        except Exception as e:
            return f'Não foi possível salvar os dados. {e}'
        
    # destrutor
    def __del__(self):
        return 'Manipulador destruído.'
