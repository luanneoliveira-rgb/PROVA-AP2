def buscar_nome(usuario_id):
    nomes = {1: "Carlos", 2: "Ana", 3: "Beatriz"}
    return nomes.get(usuario_id, "Visitante")

def gerar_saudacao(usuario_id):
    nome = buscar_nome(usuario_id)
    return f"Olá, {nome}! Seja bem-vindo."
