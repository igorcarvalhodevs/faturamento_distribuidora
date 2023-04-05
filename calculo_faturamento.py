import json

# Lendo os dados de faturamento diário do arquivo JSON
with open('C:\\Users\\DESKTOP\\desktop\\faturamento\\faturamento.json', 'r') as f:
    faturamento_diario = json.load(f)

# Calculando o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario.values())
maior_valor = max(faturamento_diario.values())

# Calculando a média mensal de faturamento diário
faturamento_total = sum(faturamento_diario.values())
dias_no_mes = len(faturamento_diario)
media_mensal = faturamento_total / dias_no_mes

# Calculando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = 0
for valor in faturamento_diario.values():
    if valor > media_mensal:
        dias_acima_da_media += 1

# Imprimindo os resultados
print(f"Menor valor de faturamento diário: R${menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")