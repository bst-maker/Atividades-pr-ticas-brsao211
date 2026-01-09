distancia_percorrida = float(input("Digite a distância percorrida em km: ")
combustível_gasto = float(input("Digite o combustível gasto em litros"))

consumo_medio = distancia_percorrida / combustível_gasto

print(f"Consumo médio: {consumo_medio:.2f} km/l")
print(f"Distância: {distancia_percorrida:.2f} km")   
print(f"Combustível gasto: {combustível_gasto:.2f} l")