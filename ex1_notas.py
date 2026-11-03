def classificar_nota(nota):
    if nota < 0 or nota > 10:
        return "Nota inválida"
    if nota >= 7:
        return "Aprovado"
    if nota >= 5:
        return "Recuperação"
    return "Reprovado"
