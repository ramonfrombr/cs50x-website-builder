```python
import json
import os
import shlex
import itertools

import check50

@check50.check()
def valido():
    """projeto existe e é um programa Scratch válido"""

    # Garantir que haja apenas um arquivo .sb3.
    filenames = [filename for filename in os.listdir() if filename.endswith(".sb3")]

    if len(filenames) > 1:
        raise check50.Failure("mais de um arquivo .sb3 encontrado. Certifique-se de que haja apenas um!")
    elif not filenames:
        raise check50.Failure("nenhum arquivo .sb3 encontrado")

    filename = filenames[0]

    # Garantir que o arquivo .sb2 descompactado contenha um arquivo .json.
    if check50.run(f"unzip {shlex.quote(filename)}").exit():
        raise check50.Failure("arquivo .sb3 inválido")
    check50.exists("project.json")

    with open("project.json") as f:
        project = json.load(f)

    return project["targets"]

@check50.check(valido)
def dois_personagens(projeto):
    """projeto contém pelo menos dois personagens"""

    num_personagens = sum(not target["isStage"] for target in projeto)

    if num_personagens < 2:
        raise check50.Failure(f"apenas {num_personagens} personagem{'' if num_personagens == 1 else 's'} encontrado, 2 necessários")

@check50.check(valido)
def nao_gato(projeto):
    """projeto contém um personagem que não é um gato"""

    ids_spr_gato = {"bcf454acf82e4504149f7ffe07081dbc",
                    "0fb9be3e8397c983338cb71dc84d0b25"}

    if all(target["isStage"] or {costume["assetId"] for costume in target["costumes"]} == ids_spr_gato for target in projeto):
        raise check50.Failure("nenhum personagem que não seja um gato encontrado")

@check50.check(valido)
def tres_blocos(projeto):
    """projeto contém pelo menos três scripts"""

    num_blocos = sum(len(target["blocks"]) for target in projeto)
    if num_blocos < 3:
        raise check50.Failure(f"apenas {num_blocos} script{'' if num_blocos == 1 else 's'} encontrado, 3 necessários")

@check50.check(valido)
def usa_condicao(projeto):
    """projeto usa pelo menos uma condição"""

    if not contem_blocos(projeto, ["control_repeat", "control_if_else", "control_if", "motion_ifonedgebounce"]):
        raise check50.Failure("nenhuma condição encontrada, 1 necessária")

@check50.check(valido)
def usa_laco(projeto):
    """projeto usa pelo menos um laço"""

    # Procurar nos scripts do projeto algum bloco de repetição, repita até, ou sempre.
    if not contem_blocos(projeto, ["control_forever", "control_repeat_until", "control_repeat"]):
        raise check50.Failure("nenhum laço encontrado, 1 necessário")

@check50.check(valido)
def usa_variavel(projeto):
    """projeto usa pelo menos uma variável"""

    if not any(target["variables"] for target in projeto):
        raise check50.Failure("nenhuma variável encontrada, 1 necessária")

@check50.check(valido)
def usa_bloco_customizado(projeto):
    """projeto usa pelo menos um bloco customizado"""

    if "custom_block" not in json.dumps(projeto):
        raise check50.Failure("nenhum bloco customizado encontrado, 1 necessário")

def contem_blocos(projeto, opcodes):
    """Retorna se o projeto contém algum bloco com seus nomes em opcodes"""
    return any(any((isinstance(bloco, dict) and bloco["opcode"] in opcodes) for bloco in target["blocks"].values())
               for target in projeto)
```