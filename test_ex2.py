from ex2_texto import analisar_texto

def test_cinco_palavras():
    assert analisar_texto("Hoje o dia está lindo") == 5

def test_uma_palavra():
    assert analisar_texto("Python") == 1

def test_frase_vazia():
    assert analisar_texto("") == 0

def test_espacos_no_inicio_e_no_fim():
    assert analisar_texto("   olá mundo   ") == 2

def test_varios_espacos_entre_palavras():
    assert analisar_texto("um    dois     três") == 3

def test_somente_espacos():
    assert analisar_texto("     ") == 0
