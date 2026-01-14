pares = 0
impares = 0

while True:
    try:
        entrada = input("Digite um número inteiro ou 'sair' para encerrar: ")

        if entrada.lower() == 'sair':
            break

        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é par.")
            pares += 1
        else:
            print(f"O número {numero} é ímpar.")
            impares += 1

    except ValueError:
        print("Você deve digitar apenas números inteiros.") 

        print(f"quantidade de números pares: {pares}")
        print(f"quantidade de números ímpares: {impares}")
        