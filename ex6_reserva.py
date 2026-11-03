ASSENTOS_DISPONIVEIS = {1, 2, 3, 4, 5}

def verificar_assento(numero_assento):
    return numero_assento in ASSENTOS_DISPONIVEIS

def reservar_assento(numero_assento):
    return "Assento reservado"

def confirmar_reserva(numero_assento):
    if verificar_assento(numero_assento):
        return reservar_assento(numero_assento)
    return "Assento indisponível"
