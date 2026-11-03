def buscar_cupom(codigo):
    return {"codigo": codigo, "percentual": 10}

def aplicar_desconto(codigo, preco):
    cupom = buscar_cupom(codigo)
    if cupom is None:
        return preco
    return preco * (1 - cupom["percentual"] / 100)
