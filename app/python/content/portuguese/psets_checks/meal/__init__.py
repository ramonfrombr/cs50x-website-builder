```python
import check50
from re import escape


@check50.check()
def existe():
    """meal.py existe"""
    check50.exists("meal.py")
    check50.include("testing.py")


@check50.check(existe)
def teste_horarios():
    """convert converte com sucesso os horários em decimal"""
    testes = {"7:30": 7.5, "14:15": 14.25, "22:00": 22.0}
    for horario in testes:
        check50.run("python3 testing.py").stdin(horario, prompt=True).stdout(testes[horario]).exit()
    

@check50.check(teste_horarios)
def teste_cafe_da_manha():
    """entrada de 7:00 gera saída \"hora do café da manhã\""""
    entrada = "7:00"
    saida = "hora do café da manhã"
    check50.run("python3 meal.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(teste_horarios)
def teste_cafe_da_manha():
    """entrada de 7:30 gera saída \"hora do café da manhã\""""
    entrada = "7:30"
    saida = "hora do café da manhã"
    check50.run("python3 meal.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(teste_horarios)
def teste_almoco():
    """entrada de 12:42 gera saída \"hora do almoço\""""
    entrada = "12:42"
    saida = "hora do almoço"
    check50.run("python3 meal.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(teste_horarios)
def teste_almoco():
    """entrada de 13:00 gera saída \"hora do almoço\""""
    entrada = "13:00"
    saida = "hora do almoço"
    check50.run("python3 meal.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(teste_horarios)
def teste_jantar():
    """entrada de 18:32 gera saída \"hora do jantar\""""
    entrada = "18:32"
    saida = "hora do jantar"
    check50.run("python3 meal.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(teste_horarios)
def teste_sem_saida():
    """entrada de 11:11 não gera saída"""
    entrada = "11:11"
    saida = ""
    check50.run("python3 meal.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

 
def regex(horario):
    """corresponde sem diferenciar maiúsculas e minúsculas com espaços em branco em ambos os lados"""
    return fr'(?i)^\s*{escape(horario)}\s*$'
```  