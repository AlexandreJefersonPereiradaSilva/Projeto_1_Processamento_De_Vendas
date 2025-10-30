arquivo=open("vendas_dia.txt", "r")
for linha in arquivo:
    valor = float(linha.strip())
    total = total + valor

arquivo.close()

print("Soma de Vendas:", total)

