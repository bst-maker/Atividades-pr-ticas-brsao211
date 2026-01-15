def calcular_desconto(valor_produto, percentual_desconto):
    desconto = valor_produto * (percentual_desconto / 100)
    valor_final = valor_produto - desconto
    return  valor_final


valor_produto = float(input("Digite o valor do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

desconto = calcular_desconto(valor_produto, percentual_desconto)
print(f"O valor final do produto com desconto é: R$ {desconto:.2f}")