def calcular_resto_divisao():
        
    try:
        num1 = int(input('Digite o primeiro número:'))
        num2 = int(input('Digite o segundo número: '))
                
        resultado_resto_divisao = num1 % num2
        print('O resultado desta operação é = {}'.format(resultado_resto_divisao))
    except ZeroDivisionError as e:
        print('Divisão por zero não permitida. Por favor digite um número válido')
        print(e)
    except ValueError as e:
        print('Ops! Isso não é um número. Por favor digite um número válido.')
        print(e)

calcular_resto_divisao() 