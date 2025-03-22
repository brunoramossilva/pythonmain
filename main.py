from os import system


# PetCIn


animais = [{'nome':'Toby', 'raca':'Vira-lata', 'vacinado':False},
           {'nome':'Mel', 'raca':'Gato(a)', 'vacinado':True},
           {'nome':'Saddam', 'raca':'Vira-lata', 'vacinado':False}]


def voltar_main():
    resposta = input('Digite qualquer coisa para voltar ao menu principal: ')
    main()


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
        '3. Vacinar animal;\n'
        '4. Sair do programa.'
        '\n\nDigite um número: '))
        return num
    
    except ValueError:
        system('cls')
        print('Opção Inválida!')
        escolha()


def condicao (num):

    if num == 1:
        system('cls')
        print('Cadastrar Novo Animal:', end=('\n\n'))
        nome_animal = input('Digite o nome do animal: ')
        raca_animal = input('Digite a raça do animal: ')
        vacina_animal = input('O animal está vacinado? (Y/N): ')

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
        system ('cls')
        print('Lista de Animais:\n')
        for animal in animais:

            if animal['vacinado']:
                vacinado = ('Vacinado(a)')
            else:
                vacinado = ('Não vacinado(a)')

            print(f'- | {animal['nome']} | {animal['raca']} | {vacinado} |')
        print('')
        voltar_main()

    elif num == 3:
        print('Vacinar Animal:')

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
