from unittest.mock import patch
from exemplo_desconto import aplicar_desconto

def test_desconto_aplicado():
    with patch("exemplo_desconto.buscar_cupom") as mock_cupom:
        mock_cupom.return_value = {"codigo": "ABC", "percentual": 20}
        assert aplicar_desconto("ABC", 100) == 80
        mock_cupom.assert_called_once_with("ABC")

def test_cupom_inexistente():
    with patch("exemplo_desconto.buscar_cupom") as mock_cupom:
        mock_cupom.return_value = None
        assert aplicar_desconto("XXX", 100) == 100
        mock_cupom.assert_called_once()
