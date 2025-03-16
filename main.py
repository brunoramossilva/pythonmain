from os import system

animais = []

def finalizar_programa():
    resposta = (input('Deseja finalizar o programa? Y/N: '))
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
    print ('-#' * 10)
    print ('      PetCIn ')
    print ('-#' * 10, end='\n\n')
    
def escolha():
    try:
        num = int(input('1. Cadastrar novo animal;\n'
        '2. Ver lista de animais cadastrados;\n'
        'Digite um número: '))
        return num
    except ValueError:
        print('Opção Inválida!')
        finalizar_programa()

def condicao (num):
    if num == 1:
        animal = input('Digite o nome do animal: ')
        animais.append(animal)
        print(f'{animal} adicionado(a) com sucesso na lista!')
        resposta = input ('Cadastrar outro animal? (Y/N): ')
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
