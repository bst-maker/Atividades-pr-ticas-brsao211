

try:
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        operação = input("Digite a operação (+, -, *, /): ")

        if operação == "+":
            resultado = numero1 + numero2
        elif operação == "-":
            resultado = numero1 - numero2
        elif operação == "*":
            resultado = numero1 * numero2
        elif operação == "/":
            resultado = numero1 / numero2
        else:
            raise Exception()
        
        print(f"O resultado é: {resultado}")
        break

except ValueError:
        print("Você deve digitar apenas números.")
except ZeroDivisionError:
        print("Não é possível dividir por zero.")   
except Exception:
        print("Operação inválida. Tente novamente.")

        