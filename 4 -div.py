def dividir():
    try:
        num1 = int(input('Digite o primeiro número:'))
        num2 = int(input('Digite o segundo número: '))
            
        resultado_divisao = num1 / num2
        print('O resultado desta operação é = {}'.format(resultado_divisao))

    except ZeroDivisionError as e:
        print('Divisão por zero não permitida. Por favor, digite um número válido.')
        print(e)
    except ValueError as e:
        print('Por favor, digite um número válido.')
        print(e)