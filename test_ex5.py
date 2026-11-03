from unittest.mock import patch
from ex5_senha import verificar_senha, criar_conta

def test_senha_valida():
    assert verificar_senha("abc12345") is True

def test_senha_invalida():
    assert verificar_senha("abc1") is False          # curta
    assert verificar_senha("abcdefgh") is False      # sem número
    assert verificar_senha("12345678") is False      # sem letra

def test_verificar_senha_foi_chamada():
    with patch("ex5_senha.verificar_senha") as mock_senha:
        mock_senha.return_value = True
        criar_conta("Carlos", "abc12345")
        mock_senha.assert_called_once()

def test_verificar_senha_chamada_com_senha_correta():
    with patch("ex5_senha.verificar_senha") as mock_senha:
        mock_senha.return_value = True
        criar_conta("Carlos", "minhaSenha1")
        mock_senha.assert_called_once_with("minhaSenha1")

def test_mock_senha_valida():
    with patch("ex5_senha.verificar_senha") as mock_senha:
        mock_senha.return_value = True
        assert criar_conta("Carlos", "qualquer") == "Conta criada com sucesso"

def test_mock_senha_invalida():
    with patch("ex5_senha.verificar_senha") as mock_senha:
        mock_senha.return_value = False
        assert criar_conta("Carlos", "qualquer") == "Senha inválida"
