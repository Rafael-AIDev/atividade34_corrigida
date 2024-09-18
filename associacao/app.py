from modulo import *

if __name__ == "__main__":
    aluno1 = Aluno('','','')

    aluno1.nome = input('Informe o nome do aluno: ')
    aluno1.matricula = input('Informe a matrícula do aluno: ')
    aluno1.cpf = input('Informe o cpf do aluno: ')

    aluno2 = Aluno('','','')

    aluno2.nome = input('Informe o nome do 2º aluno: ')
    aluno2.matricula = input('Informe a matrícula do 2º aluno: ')
    aluno2.cpf = input('Informe o cpf do 2º aluno: ')

    # instancia o curso
    curso1 = Curso('',0,'')

    curso1.nome = input('Informe o nome do curso: ')
    curso1.duracao = int(input('Informe a duração do curso: '))
    curso1.turno = input('Informe o turno do curso: ')

    #instancia o 2º curso
    curso2 = Curso('',0,'')

    curso2.nome = input('Informe o nome do 2º curso: ')
    curso2.duracao = int(input('Informe a duração do 2º curso: '))
    curso2.turno = input('Informe o turno do 2º curso: ')

    #cadastrando os alunos instanciados no curso instanciado
    aluno1.inscrever_curso(curso1)
    aluno1.inscrever_curso(curso2)
    aluno2.inscrever_curso(curso1)
 
    # cadastrando os alunos instanciados no curso instanciado
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)

    # saída de dados
    print(f'Aluno {aluno1.nome} de matrícula {aluno1.matricula} está inscrito no curso {aluno1.listar_curso()}')
    print(f'Aluno {aluno2.nome} de matrícula {aluno2.matricula} está inscrito no curso {aluno2.listar_curso()}')
    print(f'No curso {curso1.nome} estão matriculados os alunos: {curso1.listar_alunos()}')
    print(f'No curso {curso2.nome} estão matriculados os alunos: {curso2.listar_alunos()}')


