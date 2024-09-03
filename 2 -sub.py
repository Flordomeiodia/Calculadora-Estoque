#fazendo conta de subtração
#Na teoria é Num1 - Num2 = resultado

def Subtracao():
    X = float(input("Digite o primeiro número da conta:"))
    Y = float(input("Digite o segundo número da conta:"))
    resultado_Subtração: X - Y  # type: ignore
    print ('O Resultado da sua subtração é:{} '.format(resultado_Subtração))
