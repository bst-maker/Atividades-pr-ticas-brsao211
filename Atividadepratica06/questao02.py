import requests 

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        dados = resposta.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        
        return f"""
                Nome: {nome}    
            Email: {email}
            Pais: {pais}
            """
    except Exception as e:
        return f"Erro ao obter dados do usuário: {e}"
    
  



if __name__ == "__main__":
    print(obter_usuario_aleatorio())