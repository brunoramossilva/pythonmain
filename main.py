from os import system
import time


animais = [{'nome':'Toby', 'raca':'Vira-lata', 'vacinado':False},
           {'nome':'Mel', 'raca':'Gato(a)', 'vacinado':True},
           {'nome':'Saddam', 'raca':'Vira-lata', 'vacinado':False}]


def voltar_main():
    input('Digite qualquer coisa para voltar ao menu principal: ')
    system('cls')
    print('Voltando ao menu principal, aguarde...')
    time.sleep(1.5)
    main()


def exibir_subtitulo(mensagem):
    system ('cls')
    tamanho = len(mensagem)
    print('-#' * (tamanho // 2))
    print(mensagem)
    print('-#' * (tamanho // 2))
    print()


def finalizar_programa():
    resposta = (input('Deseja finalizar o programa? (Y/N): '))
    if resposta.lower() == 'y':
        quit()
    elif resposta.lower() == 'n':
        main()
    else:
        print('Opção inválida')
        finalizar_programa()


def print_inicial():
    system ('cls')
    print ('-#' * 11)

    print ("""
█▀█ █▀▀ ▀█▀ █▀▀ █ █▄░█
█▀▀ ██▄ ░█░ █▄▄ █ █░▀█
           """)
    
    print ('-#' * 11, end='\n\n')


def escolha():
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


def status_animal():
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

    if num == 1:
        exibir_subtitulo('Cadastrando um Novo Animal')
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
            condicao(num)
        else:
            system ('cls')
            main()

    elif num == 2:
        exibir_subtitulo('Listagem de Animais')
        for animal in animais:

            if animal['vacinado']:
                vacinado = ('Vacinado(a)')
            else:
                vacinado = ('Não vacinado(a)')

            print(f'• Nome do animal: {animal['nome']} | Raça do animal: {animal['raca']} | Status de vacinação: {vacinado};')
        print('')
        voltar_main()

    elif num == 3:
        system('cls')
        exibir_subtitulo('Alterando Status de Vacinação do Animal')
        status_animal()

    elif num == 4:
        system('cls')
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
