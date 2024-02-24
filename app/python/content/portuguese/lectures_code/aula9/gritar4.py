# Usa list comprehension

def principal():
    gritar("Este", "é", "o", "CS50")

def gritar(*palavras):
    em_maiusculo = [palavra.upper() for palavra in palavras]
    print(*em_maiusculo)

if __name__ == "__main__":
    principal()