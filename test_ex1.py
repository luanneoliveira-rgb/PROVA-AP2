from ex1_notas import classificar_nota

def test_nota_8_aprovado():
    assert classificar_nota(8) == "Aprovado"

def test_nota_6_recuperacao():
    assert classificar_nota(6) == "Recuperação"

def test_nota_4_reprovado():
    assert classificar_nota(4) == "Reprovado"

def test_nota_10_aprovado():
    assert classificar_nota(10) == "Aprovado"

def test_nota_negativa_invalida():
    assert classificar_nota(-1) == "Nota inválida"

def test_nota_11_invalida():
    assert classificar_nota(11) == "Nota inválida"

def test_limites():
    assert classificar_nota(7) == "Aprovado"
    assert classificar_nota(6.9) == "Recuperação"
    assert classificar_nota(5) == "Recuperação"
    assert classificar_nota(4.9) == "Reprovado"
    assert classificar_nota(0) == "Reprovado"
