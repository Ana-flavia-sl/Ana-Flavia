preco_dia = 90
preco_km = 0.20
dias = int(input("quantos dias o carro foi alugado?"))
kms = float(input(" quantos KMs foram percorrido?"))
custo_dias = dias * preco_dia
custo_kms =kms * preco_km
total = custo_dias + custo_kms
print("===== RECIBO de aluguel =====")
print (f"dias alugados: {dias} dias x R${preco_dia}) = R${custo_dias}")
print (f"km rodado: {kms}km x R${preco_dia} = R${custo_dias}")
print(f"TOTAL A PAGAR: R${total}")
print("============================")
      