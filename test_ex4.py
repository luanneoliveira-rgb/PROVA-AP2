from unittest.mock import patch
from ex4_saudacao import buscar_nome, gerar_saudacao

def test_saudacao_gerada_corretamente():
    with patch("ex4_saudacao.buscar_nome") as mock_nome:
        mock_nome.return_value = "Carlos"
        assert gerar_saudacao(1) == "Olá, Carlos! Seja bem-vindo."

def test_buscar_nome_foi_chamada():
    with patch("ex4_saudacao.buscar_nome") as mock_nome:
        mock_nome.return_value = "Carlos"
        gerar_saudacao(1)
        mock_nome.assert_called_once()

def test_buscar_nome_chamada_com_id_correto():
    with patch("ex4_saudacao.buscar_nome") as mock_nome:
        mock_nome.return_value = "Ana"
        gerar_saudacao(42)
        mock_nome.assert_called_once_with(42)

def test_mock_com_diferentes_nomes():
    for nome in ["Carlos", "Ana", "Beatriz"]:
        with patch("ex4_saudacao.buscar_nome") as mock_nome:
            mock_nome.return_value = nome
            assert gerar_saudacao(1) == f"Olá, {nome}! Seja bem-vindo."

def test_buscar_nome_real():
    assert buscar_nome(1) == "Carlos"
    assert buscar_nome(999) == "Visitante"
