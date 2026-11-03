def verificar_senha(senha):
    return (
        len(senha) >= 8
        and any(c.isdigit() for c in senha)
        and any(c.isalpha() for c in senha)
    )

def criar_conta(nome, senha):
    if verificar_senha(senha):
        return "Conta criada com sucesso"
    return "Senha inválida"
