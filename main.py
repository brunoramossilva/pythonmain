from os import system

def finalizar_programa():
    resposta = (input('Deseja finalizar o programa? Y/N: '))
    if resposta.lower() == 'y':
        quit()
    else:
        print('Voltando ao menu principal...')
        main()

def print_inicial():

    print("""T
i
a
l
y""")
    
def escolha():
    try:
        num = int(input('Escolha um número entre 1 e 2: '))
        return num
    except ValueError:
        print('Opção Inválida!')
        finalizar_programa()

def condicao (num):
    if num == 1:
        print_inicial()
        finalizar_programa()

    elif num == 2:
        system('cls')
        print('Você apagou tudo!')
        finalizar_programa()
    else:
        input('Número inválido.\nDigite qualquer coisa para voltar ao menu principal: ')
        main()

def main():
    system('cls')
    num = escolha()
    condicao(num)

if __name__ == '__main__':
    main()
