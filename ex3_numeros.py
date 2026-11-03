def analisar_numero(numero):
    if numero > 0:
        sinal = "Positivo"
    elif numero < 0:
        sinal = "Negativo"
    else:
        sinal = "Zero"
    paridade = "par" if numero % 2 == 0 else "ímpar"
    return f"{sinal} e {paridade}"
