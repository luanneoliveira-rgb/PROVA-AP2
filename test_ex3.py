from ex3_numeros import analisar_numero

def test_positivo_par():
    assert analisar_numero(10) == "Positivo e par"

def test_positivo_impar():
    assert analisar_numero(7) == "Positivo e ímpar"

def test_negativo_par():
    assert analisar_numero(-4) == "Negativo e par"

def test_negativo_impar():
    assert analisar_numero(-3) == "Negativo e ímpar"

def test_zero():
    assert analisar_numero(0) == "Zero e par"
