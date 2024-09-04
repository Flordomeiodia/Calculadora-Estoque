import somar, sub, mult, div, restoDiv, historico

def funcao_calculadora ():
    
    historico_calculadora = []

    while(True):
        try:
            print('Bem-vindo ao menu da calculadora, digite o número: ')
            print('(1) PARA REALIZAR A FUNÇÃO DE SOMA')
            print('(2) PARA REALIZAR A FUNÇÃO DE SUBTRAÇÃO')
            print('(3) PARA REALIZAR A FUNÇÃO DE MULTIPLICAÇÃO')
            print('(4) PARA REALIZAR A FUNÇÃO DE DIVISÃO')
            print('(5) PARA REALIZAR A FUNÇÃO DE RESTO DE DIVISÃO')
            print('(6) PARA REALIZAR A FUNÇÃO DE RESTO DE DIVISÃO')
            print('(0) PARA SAIR DA CALCULADORA')

            opcao = int(input('Digite o número que representa a sua escolha: '))

            if(opcao == 1):
                somar.soma()
                historico_calculadora.append('1 - FUNÇÃO DE SOMA')
            elif(opcao == 2):
                sub.subtracao()
                historico_calculadora.append('2 - FUNÇÃO DE SUBTRAÇÃO')
            elif(opcao == 3):
                mult.multiplicar()
                historico_calculadora.append('3 - FUNÇÃO DE MULTIPLICAÇÃO')
            elif(opcao == 4):
                div.dividir()
                historico_calculadora.append('4 - FUNÇÃO DE DIVISÃO')
            elif(opcao == 5):
                restoDiv.calcular_resto_divisao()
                historico_calculadora.append('5 - FUNÇÃO DE RESTO DA DIVISÃO')
            elif(opcao == 6):
                historico.consultar_historico(historico_calculadora)
            elif(opcao == 0):
                print('Obrigada por utilizar a calculadora, até breve.')
                break
            else:
                print('Opção inválida. Digite um número ente 0 e 6.')
        except Exception as e:
            print('Houve um erro, tente novamente.')
            print(e)

funcao_calculadora()