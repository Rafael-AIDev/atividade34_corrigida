class Pessoa:
    # método construtor
    def __init__ (self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    # métodos especias 

    # NOTE: a função str() serve para retornar representações de valores que sejam legíveis para as pessoas
    def __str__(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} e meu email é {self.email}."
    
    # NOTE: a função repr() é para gerar representações que o interpretador python consegue ler (ou levantará uma exceção SyntaxError, se não houver sintaxe equivalente)
    def __repr__ (self):
        return f"Pessoal ({self.nome}, {self.idade}, {self.email})"
    
    def __len__(self):
        return self.nome
    
    def __del__(self): # método destrutor, ele destroi o objeto no programa, utilidade limpeza de mémoria, retirar os restos dos dados da mémoria RAM, no final do dia o computador está mais lento, desvantagem perde em eficiência, ganha em memória. No Java, no android, os aplicativos são feitos em java então se um app consome 2 gb em java vai consumir 4 gb
        print(f"O objeto {self.nome} foi eliminado com sucesso.")
        # não se usa encapsulamento em métodos especiais não precisa colocar tipo self.__nome só precisa colocar self.nome
        # orientação orientada a objeto quando for criar para o usuário, já quando for criar para bancos, usará programação estrutural mesmo
    