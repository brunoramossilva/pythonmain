from os import system

# PetCIn

animais = []

def finalizar_programa():

    resposta = (input('Deseja finalizar o programa? (Y/N): '))
    if resposta.lower() == 'y':
        quit()
    elif resposta.lower() == 'n':
        print('Voltando para o menu principal...')
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
        'Digite um número: '))
        return num
    
    except ValueError:
        system('cls')
        print('Opção Inválida!')
        escolha()


def condicao (num):

    if num == 1:
        system ('cls')
        animal = input('Digite o nome do animal: ')
        animais.append(animal)
        print(f'{animal} adicionado(a) com sucesso na lista!')

        resposta = input ('Deseja cadastrar outro animal? (Y/N): ')
        if resposta.lower() == 'y':
            system ('cls')
            condicao(num)
        else:
            system ('cls')
            main()

    elif num == 2:
        for animal in animais:
            print(f'{animal};')
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
