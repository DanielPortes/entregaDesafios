import json

# Abre o arquivo e carrega os dados JSON
with open('../../dados.json') as file:
    data = json.load(file)


day = []
valor = []

# Extrai os dados de cada objeto no array JSON
for obj in data:
    if obj['valor'] == 0.0:
        continue
    day.append(obj['dia'])
    valor.append(obj['valor'])


# Dia com o maior valor de faturamento
maiorFaturamento = max(valor)
diaMaiorFaturamento = day[valor.index(maiorFaturamento)]
print(f"Dia com menor valor: {diaMaiorFaturamento} - valor: {maiorFaturamento}")

# Com o menor valor de faturamento
menorFaturamento = min(valor)
diaMenorFaturamento = day[valor.index(menorFaturamento)]
print(f"Dia com maior valor: {diaMenorFaturamento} - valor: {menorFaturamento}")

# Media de faturamento ignorando os dias sem faturamento
print(f"Media dos dias com faturamento: {sum(valor) / len(valor)}")
