```python
importar check50

HASHES = {
    "muppet_01.jpg" : 'b782475a5dd3b0d7b3202cebc8a70f5d795dd196e9c18564691d5edc11ccf7c9',
    "muppet_02.jpg" : 'f989a97f95563f587e158bb55a1fc6dba075f1e221acec988612caaa0d1a6b78',
    "muppet_03.jpg" : 'fa7b30def84d46559c54e718d167de93e52785f9b613db8a647ddcfbbe9aff98',
    "muppet_04.jpg" : '8f59304412e181f1a18d3b36ad88d7b2911a7eea8f471c7e437e2cbed5893152',
    "muppet_05.jpg" : 'eeb531294c2211ba578dafe5c1f53d974f77312cec5b7bcc315c2bb429b3ac1d',
    "muppet_06.jpg" : '4918f1f41fa872e2807fd325d4e460bcce9b1f23660cdf0e73dc3127fccc1046',
}


@check50.verificar()
def existe():
    """shirt.py existe"""
    check50.existe("shirt.py")
    check50.incluir("shirt.png")


@check50.verificar(existe)
def test_argumentos_menos():
    """shirt.py sai dado nenhum argumento de linha de comando"""
    saida = check50.rodar("python3 shirt.py").saida()
    if saida == 0:
        raise check50.Falha(f"Código de saída esperado não nulo.")


@check50.verificar(existe)
def test_extensao_invalida():
    """shirt.py sai dado um arquivo sem a extensão .jpg, .jpeg ou .png"""
    check50.incluir("invalid_extension.bmp")
    saida = check50.rodar("python3 shirt.py invalid_extension.bmp").saida()
    if saida == 0:
        raise check50.Falha(f"Código de saída esperado não nulo.")


@check50.verificar(existe)
def test_arquivo_inexistente():
    """shirt.py sai dado um arquivo inexistente"""
    saida = check50.rodar("python3 shirt.py non_existent_file.jpg").saida()
    if saida == 0:
        raise check50.Falha(f"Código de saída esperado não nulo.")


@check50.verificar(existe)
def test_extensao_incompativel():
    """shirt.py sai com um arquivo de saída com extensão diferente do arquivo de entrada"""
    check50.incluir("muppet_01.jpg")
    saida = check50.rodar("python3 shirt.py muppet_01.jpg muppet_01_out.png").saida()
    if saida == 0:
        raise check50.Falha(f"Código de saída esperado não nulo.")


@check50.verificar(existe)
def test_argumentos_mais():
    """shirt.py sai dado mais de dois argumentos de linha de comando"""
    for arquivo in ["muppet_01.jpg", "muppet_02.jpg", "muppet_03.jpg"]:
        check50.incluir(arquivo)
    saida = check50.rodar("python3 lines.py muppet_01.jpg muppet_02.jpg muppet_03.jpg").saida()
    if saida == 0:
        raise check50.Falha(f"Código de saída esperado não nulo.")


@check50.verificar(existe)
def test_muppet_01():
    """shirt.py exibe corretamente a camisa em muppet_01.jpg"""
    testar_camisa("muppet_01.jpg")


@check50.verificar(existe)
def test_muppet_02():
    """shirt.py exibe corretamente a camisa em muppet_02.jpg"""
    testar_camisa("muppet_02.jpg")


@check50.verificar(existe)
def test_muppet_03():
    """shirt.py exibe corretamente a camisa em muppet_03.jpg"""
    testar_camisa("muppet_03.jpg")


@check50.verificar(existe)
def test_muppet_04():
    """shirt.py exibe corretamente a camisa em muppet_04.jpg"""
    testar_camisa("muppet_04.jpg")


@check50.verificar(existe)
def test_muppet_05():
    """shirt.py exibe corretamente a camisa em muppet_05.jpg"""
    testar_camisa("muppet_05.jpg")


@check50.verificar(existe)
def test_muppet_06():
    """shirt.py exibe corretamente a camisa em muppet_06.jpg"""
    testar_camisa("muppet_06.jpg")


def testar_camisa(foto):
    check50.incluir(foto)
    check50.rodar(f"python3 shirt.py {foto} {foto[:-4]}_out.jpg").saida(0)
    hash = check50.hash(f"{foto[:-4]}_out.jpg")
    if hash != HASHES[foto]:
        raise check50.Falha("Imagem não corresponde")
```  