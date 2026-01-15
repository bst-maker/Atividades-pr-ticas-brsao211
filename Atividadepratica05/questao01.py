def calcular_gorjeta(valor_conta, percentual_gorjeta):
    gorjeta = valor_conta * (percentual_gorjeta / 100)
    return gorjeta


valor_conta = float(input("Digite o valor da conta: R$ "))
percentual_gorjeta = float(input("Digite o percentual da gorjeta (%): "))   

gorjeta = calcular_gorjeta(valor_conta, percentual_gorjeta)
print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")