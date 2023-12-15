def replace_incorrect_translations(translated_content):
    """
    Replaces incorrect code translations
    """
    translated_content.replace("TODO", "FAZER")
    translated_content.replace("TO-DO", "FAZER")
    translated_content.replace("int principal(", "int main(")
    return translated_content

def replace_incorrect_translations_checks(translated_content):
    """
    Replaces incorrect code translations for originals in check files
    """
    translated_content.replace("importar ", "import ")
    translated_content.replace("check50.verificar", "check50.check")
    translated_content.replace("check50.existe", "check50.exists")
    translated_content.replace("check50.c.compila", "check50.c.compile")
    translated_content.replace("check50.executar", "check50.run")
    translated_content.replace(".entradas(", ".stdin(")
    translated_content.replace(".rejeitar()", ".reject()")
    translated_content.replace(".saída(", ".stdout(")
    translated_content.replace(".sair(0)", ".exit(0)")
    return translated_content

def remove_leading_and_trailing_quote(translated_content):
    """
    Removes unwanted leading and trailing quotes
    """
    # remove " at the end of file
    if translated_content.startswith("'"):
        translated_content = translated_content[1:]
    if translated_content.startswith('"'):
        translated_content = translated_content[1:]

    # remove ' at the end of file
    if translated_content.endswith("'"):
        translated_content = translated_content[:-1]
    if translated_content.endswith('"'):
        translated_content = translated_content[:-1]
    return translated_content
