import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = calcular_idade(ano_nascimento)
print(f"Você tem: {idade_em_dias} dias vividos.")
