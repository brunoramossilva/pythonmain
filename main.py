from os import system
import time


animais = [{'nome':'Toby', 'raca':'Vira-lata', 'vacinado':False},
           {'nome':'Mel', 'raca':'Gato(a)', 'vacinado':True},
           {'nome':'Saddam', 'raca':'Vira-lata', 'vacinado':False}]

def voltar_main():
    '''
    Essa função é responsável por retornar para o menu principal da aplicação.
    
    Inputs:
    - Qualquer entrada.

    Outputs:
    - Retorna para o menu principal.
    '''
    input('Digite qualquer coisa para voltar ao menu principal: ')
    system('cls')
    print('Voltando ao menu principal, aguarde...')
    time.sleep(1.5)
    main()

def exibir_subtitulo(mensagem):
    '''
    Essa função é responsável por exibir os subtítulos das telas.
    '''
    system ('cls')
    tamanho = len(mensagem)
    print('-#' * (tamanho // 2))
    print(mensagem)
    print('-#' * (tamanho // 2))
    print()

def finalizar_programa():
    '''
    Essa função é responsável por finalizar o programa.

    Inputs:

    - Qualquer tecla.
    '''
    system('cls')
    resposta = (input('Deseja finalizar o programa? (Y/N): '))
    if resposta.lower() == 'y':
        quit()
    elif resposta.lower() == 'n':
        main()
    else:
        print('Opção inválida')
        finalizar_programa()

def print_inicial():
    '''
    Função responsável por exibir o título do programa.
    '''
    system ('cls')
    print ('-#' * 11)

    print ("""
█▀█ █▀▀ ▀█▀ █▀▀ █ █▄░█
█▀▀ ██▄ ░█░ █▄▄ █ █░▀█
           """)
    
    print ('-#' * 11, end='\n\n')

def escolha():
    '''
    Função responsável por armazenar a escolha do usuário.

    Inputs:

    - Número escolhido pelo usuário.

    Outputs:

    - Retorna o número escolhido.
    '''
    try:
        num = int(input('1. Cadastrar novo animal;\n'
        '2. Ver lista de animais cadastrados;\n'
        '3. Alterar status de vacinação do animal;\n'
        '4. Sair do programa.'
        '\n\nDigite um número: '))
        return num
    
    except ValueError:
        system('cls')
        print('Opção Inválida!')
        escolha()

def cadastrar_animal():
    '''
    Essa função é responsável por cadastrar um novo animal na lista.

    Inputs:

    - Nome do animal;
    - Raça do animal;
    - Status de vacinação do animal;
    - Se o usuário deseja cadastrar um outro animal.

    Outputs:

    - Insere o animal descrito na lista de animais cadastrados.
    '''
    nome_animal = input('Digite o nome do animal: ')
    raca_animal = input(f'{nome_animal} é da raça: ')
    vacina_animal = input(f'{nome_animal} está vacinado(a)? (Y/N): ')

    if vacina_animal.lower() == 'y':
        vacinado = True
    else:
        vacinado = False

    dados_animal = {'nome':nome_animal, 'raca':raca_animal, 'vacinado':vacinado}
    animais.append(dados_animal)
    
    system('cls')
    print(f'{nome_animal} adicionado(a) com sucesso na lista!')

    resposta = input ('Deseja cadastrar outro animal? (Y/N): ')

    if resposta.lower() == 'y':
        system ('cls')
        cadastrar_animal()
    else:
        system ('cls')
        main()

def listagem_animais():
    '''
    Inputs:

    - N/A.

    Outputs:

    - Exibe a lista de animais cadastrados.
    '''
    print(f'{'  Nome do Animal'.ljust(20)} | {'Raça do animal'.ljust(18)} | {'Status de vacinação'}')
    print(f'{'                     |'}                    |')
    for animal in animais:
        vacinado = 'Vacinado(a)' if animal['vacinado'] else 'Não vacinado(a)'
        print(f'  {animal['nome'].ljust(18)} | {animal['raca'].ljust(18)} | {vacinado};')
    print('')
    voltar_main()

def status_animal():
    '''
     Inputs:

    - Nome do animal que o usuário deseja alterar o status de vacinação.

    Outputs:

    - Altera o status de vacinação do animal escolhido.
    '''
    nome_animal = input('Digite o nome do animal que você deseja alterar o status de vacinação: ')
    animal_encontrado = False
    for animal in animais:
        if nome_animal == animal['nome']:
            animal_encontrado = True
            system('cls')
            print('Animal encontrado com sucesso!')
            time.sleep(1)
            system('cls')
            animal['vacinado'] = not animal['vacinado']
            mensagem = f'Status de vacinação de {nome_animal} alterado para vacinado(a) com sucesso!' if animal['vacinado'] else f'Status de vacinação de {nome_animal} alterado para não vacinado(a) com sucesso!'
            print(mensagem,end=('\n\n'))
            voltar_main()
    if not animal_encontrado:
        print('Infelizmente não foi possível localizar o animal que você digitou.\n\nTente novamente:')
        voltar_main()

def condicao (num):
    '''
    Essa função é responsável por estabelecer o que o programa irá executar a partir da entrada do usuário.
    '''
    if num == 1:
        exibir_subtitulo('Cadastrando um Novo Animal')
        cadastrar_animal()
        
    elif num == 2:
        exibir_subtitulo('Listagem de Animais')
        listagem_animais()

    elif num == 3:
        exibir_subtitulo('Alterando Status de Vacinação do Animal')
        status_animal()

    elif num == 4:
        finalizar_programa()

    else:
        input('Número inválido.\nDigite qualquer coisa para voltar ao menu principal: ')
        main()

def main():
    system ('cls')
    print_inicial()
    num = escolha()
    condicao(num)


if __name__ == '__main__':
    main()
