from os import system

def print_inicial():


    print("""
        T
        i
        a
        l
        y""")
    
def escolha():
    num = int(input('Escolha um número: '))
    return num

def condicao (num):
    if num == 5:
        print_inicial()

    else:
        system('cls')
        print('Você apagou tudo!')

def main():
    num = escolha()
    condicao(num)

if __name__ == '__main__':
    main()
