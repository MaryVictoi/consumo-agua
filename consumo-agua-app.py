# Entrada de dados
tipo_imovel = input(
    "Informe o tipo de imóvel (comercial, casa ou apartamento): "
).lower()

consumo = float(
    input("Informe o consumo mensal de água em m³: ")
)

# Análise do consumo
if tipo_imovel == "comercial":
    mensagem = (
        "A tarifa comercial será aplicada. "
        "Consulte o plano corporativo."
    )

elif tipo_imovel == "apartamento" and consumo < 10:
    mensagem = (
        f"Seu consumo foi de {consumo:.1f} m³. "
        "Excelente! O consumo está econômico."
    )

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    mensagem = (
        f"Seu consumo foi de {consumo:.1f} m³. "
        "O consumo está moderado e dentro do padrão residencial."
    )

else:
    mensagem = (
        f"Seu consumo foi de {consumo:.1f} m³. "
        "O consumo está elevado. Verifique possíveis vazamentos "
        "e adote medidas para economizar água."
    )

# Saída de dados
print("\n--- Resultado da análise ---")
print(f"Tipo de imóvel: {tipo_imovel}")
print(mensagem)
