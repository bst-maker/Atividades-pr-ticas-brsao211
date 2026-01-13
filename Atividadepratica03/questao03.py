temperatura = float(input("Digite a temperatura em Celsius: "))
origem = input("Digite a unidade de origem (C, F ou k): ").upper()
destino = input("Digite a unidade de destino (C, F ou k): ").upper()


if origem == destino:
    resultado = temperatura

elif origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif destino == "K":
        resultado = temperatura + 273.15

    elif origem == "F":
        if destino == "C":
            resultado = (temperatura - 32) * 5/9
    else:  # destino == "K"
        resultado = (temperatura - 32) * 5/9 + 273.15

else:
    if destino == "C":
        resultado = temperatura - 273.15
    else:  # destino == "F"
        resultado = (temperatura - 273.15) * 9/5 + 32

        print(f"{temperatura}°{origem} é igual a {resultado:.2f}°{destino}")