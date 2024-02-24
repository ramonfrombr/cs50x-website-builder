# Usa compreensão de dicionário em vez disso

alunos = ["Hermione", "Harry", "Ron"]

grifinorias = [{"nome": aluno, "casa": "Grifinória"} for aluno in alunos]

print(grifinorias)