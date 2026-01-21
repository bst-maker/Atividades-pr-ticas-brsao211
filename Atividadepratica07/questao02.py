import csv
from subprocess import DETACHED_PROCESS

def escrever_csv(nome_arquivo, dados):
    try:
        with open (nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
        return f"Dados escritos com sucesso no arquivo {nome_arquivo}"

    except Exception as e:
        return f"Erro ao escrever no arquivo: {e}"
    

    dados = [
        ['Ana', 28, 'São Paulo'],
        ['Bruno', 34, 'Rio de Janeiro'],
        ['Carla', 22, 'Belo Horizonte']
    ]

nome_arquivo = input("Digite o nome do arquivo CSV a ser criado:")
print(escrever_csv(nome_arquivo, dados ))
 
         # type: ignore
