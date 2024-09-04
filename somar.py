#fazendo conta de somar
#Na teoria é Num1 + Num2 = resultado
def soma():
    X = int(input("Digite o primeiro número da conta:"))
    Y = int(input("Digite o segundo número da conta:"))
    resultado_Soma = X + Y # type: ignore
    print("Resultado da sua conta:{}".format(resultado_Soma))



