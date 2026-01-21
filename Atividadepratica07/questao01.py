import pandas as pd

def processar_logs_treinamento(logs_treinamento):
    try:
        leitor = pd.read_csv(logs_treinamento)
        media = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"media: {media}, desvio_padrao: {desvio_padrao}"    
    

    except FileNotFoundError:
        return "Arquivo não encontrado."
    
    arquivo = input("Digite o nome do arquivo de log:")
    print(processar_logs_treinamento(arquivo))

