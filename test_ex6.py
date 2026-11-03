from unittest.mock import patch
from ex6_reserva import confirmar_reserva

def test_reserva_realizada_com_sucesso():
    with patch("ex6_reserva.verificar_assento") as mock_verificar, \
         patch("ex6_reserva.reservar_assento") as mock_reservar:
        mock_verificar.return_value = True
        mock_reservar.return_value = "Assento reservado"
        assert confirmar_reserva(3) == "Assento reservado"

def test_assento_indisponivel():
    with patch("ex6_reserva.verificar_assento") as mock_verificar, \
         patch("ex6_reserva.reservar_assento") as mock_reservar:
        mock_verificar.return_value = False
        assert confirmar_reserva(3) == "Assento indisponível"

def test_verificar_assento_foi_chamada():
    with patch("ex6_reserva.verificar_assento") as mock_verificar, \
         patch("ex6_reserva.reservar_assento"):
        mock_verificar.return_value = True
        confirmar_reserva(7)
        mock_verificar.assert_called_once_with(7)

def test_reservar_chamada_quando_disponivel():
    with patch("ex6_reserva.verificar_assento") as mock_verificar, \
         patch("ex6_reserva.reservar_assento") as mock_reservar:
        mock_verificar.return_value = True
        confirmar_reserva(7)
        mock_reservar.assert_called_once_with(7)

def test_reservar_nao_chamada_quando_indisponivel():
    with patch("ex6_reserva.verificar_assento") as mock_verificar, \
         patch("ex6_reserva.reservar_assento") as mock_reservar:
        mock_verificar.return_value = False
        confirmar_reserva(7)
        mock_reservar.assert_not_called()
