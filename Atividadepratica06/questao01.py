import random
import string

def gerar_senha(tamanho_senha):
    caracteres = string.ascii_letters + string.digits + "@#$%&*"
    senha = ''
    for _ in range(tamanho_senha):
        senha += random.choice(caracteres)

    return senha


tamanho = int(input("Digite o tamanho da senha desejada: "))
senha = gerar_senha(tamanho)
print(f"senha: {senha}")

