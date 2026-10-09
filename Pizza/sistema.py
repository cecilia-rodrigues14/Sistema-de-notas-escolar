#Programa principal: menu e telas.
import banco
import utilidades

def mostrar_menu():
    print('\n==================')
    print('Sistema de notas escolar')
    print('====================')
    print('1 - Cadastrar aluno')
    print('2 - Listar alunos')
    print('3 - Buscar aluno por nome')
    print('4 - Atualizar notas')
    print('5 - Remover aluno')
    print('6 - Relatório da turma')
    print('0 - Sair')
    return input('Escolha uma opção: ')

def mostrar_aluno(aluno):
    '''Mostra uma linha com os dados de um aluno.'''
    id_aluno, nome, nota1, nota2 = aluno
    media = utilidades.calcular_media(nota1, nota2)
    situacao = utilidades.situacao(media)
    print(f'[{id_aluno:>3}] {nome:<50}'
          f'N1:{nota1:>4.1f} N2: {nota2:>4.1f}'
          f'Média: {media:>4.1f} {situacao}')

def cadastrar_aluno():
    print('\n--- Cadstrar aluno ---')
    nome = utilidades.ler_texto('Nome: ')
    nota1 = utilidades.ler_nota('Nota 1 (0 a 10): ')
    nota2 = utilidades.ler_nota('Nota 2 (0 a 10): ')
    banco.inserir_aluno(nome, nota1, nota2)
    print('Aluno cadastrado com sucesso!')

def listar_alunos():
    print('\n--- Listar alunos ---')
    alunos = banco.listar_alunos()
    if len(alunos) == 0:
        print('Nenhum aluno encontrado.')
        return
    for aluno in alunos:
        mostrar_aluno()

def buscar_aluno():
    print('\n--- Buscar Aluno ---')
    texto = utilidades.ler_texto('Digite parte do nome: ')
    alunos = banco.buscar_por_nome(texto)
    if len(alunos) == 0:
        print('Nenhum aluno encontrdo')
    for aluno in alunos:
        mostrar_aluno()

def atualizar_notas():
    print('\n--- Atualizar Notas ---')
    id_aluno = utilidades.ler_inteiro('Digite o ID do aluno: ')
    aluno = banco.buscar_por_id(id_aluno)
    if aluno is None:
        print('Aluno não encontrado.')
        return
    mostrar_aluno()
    nota1 = utilidades.ler_nota('Nova nota 1: ')
    nota2 = utilidades.ler_nota('Nova nota 2: ')
    print('Notas atualizadas')

def remover_aluno():
    print('\n--- Remover Aluno ---')
    id_aluno = utilidades.ler_inteiro('Digite o ID do aluno: ')
    aluno = banco.buscar_por_id(id_aluno)
    if aluno is None:
        print('Aluno não encontrado.')
        return
    mostrar_aluno()
    confirma = input('Tem certeza que deseja remover? (S/N): ').lower()
    if confirma == 'S':
        banco.remover_aluno(id_aluno)
        print('Aluno Removido.')
    else:
        print('Remoção cancelada')

def mostrar_relatorio():
    print('\n--- Relatório da turma ---')
    alunos = banco.listar_alunos()
if len(alunos) == 0:
    print('Nenhum aluno cadastrado') 
    return

    somas_medias = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    melhor_nome = 0
    melhor_media = 0

    for id_aluno, nome, nota1, nota2 in alunos:
        media = utilidades.calcular_media(nota1, nota2)
        soma_medias += 1

    if situacao == 'Aprovado':
        aprovados += 1
    elif situacao == 'Recuperção':
        recuperacao += 1
    else:
        reprovados += 1
    if media > melhor_media:
        melhor_media = media
        melhor_nome = nome
