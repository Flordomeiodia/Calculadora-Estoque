import somar, sub, mult, div, restoDiv

def funcao_calculadora ():
    while(True):
        try:
            print('Bem-vindo ao menu da calculadora, digite o número: ')
            print('(1) PARA REALIZAR A FUNÇÃO DE SOMA')
            print('(2) PARA REALIZAR A FUNÇÃO DE SUBTRAÇÃO')
            print('(3) PARA REALIZAR A FUNÇÃO DE MULTIPLICAÇÃO')
            print('(4) PARA REALIZAR A FUNÇÃO DE DIVISÃO')
            print('(5) PARA REALIZAR A FUNÇÃO DE RESTO DE DIVISÃO')
            print('(0) PARA SAIR DA CALCULADORA')

            opcao = int(input('Digite o número que representa a sua escolha: '))

            if(opcao == 1):
                somar.soma()
            elif(opcao == 2):
                sub.subtracao()
            elif(opcao == 3):
                mult.multiplicar()
            elif(opcao == 4):
                div.dividir()
            elif(opcao == 5):
                restoDiv.calcular_resto_divisao()
            elif(opcao == 0):
                print('Você saiu do sitema de estoque da loja.')
                break
            else:
                print('Opção inválida. Digite um número ente 0 e 4.')
        except:
            print('Opção inválida. Digite um número ente 0 e 4.')

funcao_calculadora()