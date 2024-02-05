```python
import check50
import check50.py
import check50.flask
import os


# Defina API_KEY com um valor fictício. O código do distro olha para este valor, mas não é usado nas verificações.
os.environ["API_KEY"] = "foo"


@check50.check()
def existe():
    """app.py existe"""
    check50.exists("app.py")
    check50.include("lookup.py")
    check50.py.append_code("helpers.py", "lookup.py")


@check50.check(existe)
def inicializacao():
    """aplicação inicia"""
    Finance().get("/").status(200)


@check50.check(inicializacao)
def pagina_registro():
    """página de registro tem todos os elementos necessários"""
    Finance().validate_form("/register", ["username", "password", "confirmation"])


@check50.check(pagina_registro)
def registro_simples():
    """registro de usuário tem êxito"""
    Finance().register("_cs50", "ohHai28!", "ohHai28!").status(200)


@check50.check(pagina_registro)
def registro_campo_vazio_falha():
    """registro com campo vazio falha"""
    for user in [("", "crimson", "crimson"), ("jharvard", "crimson", ""), ("jharvard", "", "")]:
        Finance().register(*user).status(400)


@check50.check(pagina_registro)
def registro_senha_incompativel_falha():
    """registro com senha incompatível falha"""
    Finance().register("check50user1", "thisiscs50", "crimson").status(400)


@check50.check(pagina_registro)
def registro_rejeita_nome_usuario_duplicado():
    """registro rejeita nome de usuário duplicado"""
    user = ["elfie", "Doggo28!", "Doggo28!"]
    Finance().register(*user).status(200).register(*user).status(400)


@check50.check(inicializacao)
def pagina_login():
    """página de login tem todos os elementos necessários"""
    if Finance().page_exists("/signin"):
        Finance().validate_form("/signin", ["username", "password"])
        return
    Finance().validate_form("/login", ["username", "password"])


@check50.check(registro_simples)
def pode_logar():
    """logar como usuário registrado tem êxito"""
    Finance().login("_cs50", "ohHai28!").status(200).get("/", follow_redirects=False).status(200)


@check50.check(pode_logar)
def pagina_cotacao():
    """página de cotação tem todos os elementos necessários"""
    Finance().login("_cs50", "ohHai28!").validate_form("/quote", "symbol")


@check50.check(pagina_cotacao)
def cotacao_lida_simbolo_invalido():
    """cotação lida símbolo de ticker inválido"""
    Finance().login("_cs50", "ohHai28!").quote("ZZZ").status(400)


@check50.check(pagina_cotacao)
def cotacao_lida_simbolo_vazio():
    """cotação lida com símbolo de ticker em branco"""
    Finance().login("_cs50", "ohHai28!").quote("").status(400)


@check50.check(pagina_cotacao)
def cotacao_lida_simbolo_valido():
    """cotação lida com símbolo de ticker válido"""
    (Finance().login("_cs50", "ohHai28!")
              .quote("AAAA")
              .status(200)
              .content(r"28\.00", "28.00", name="body"))


@check50.check(pode_logar)
def pagina_compra():
    """página de compra tem todos os elementos necessários"""
    Finance().login("_cs50", "ohHai28!").validate_form("/buy", ["shares", "symbol"])


@check50.check(pagina_compra)
def compra_lida_simbolo_invalido():
    """compra lida com símbolo de ticker inválido"""
    Finance().login("_cs50", "ohHai28!").transaction("/buy", "ZZZZ", "2").status(400)


@check50.check(pagina_compra)
def compra_lida_acoes_incorretas():
    """compra lida com ações fracionárias, negativas e não numéricas"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/buy", "AAAA", "-1").status(400)
              .transaction("/buy", "AAAA", "1.5").status(400)
              .transaction("/buy", "AAAA", "foo").status(400))


@check50.check(pagina_compra)
def compra_lida_valida():
    """compra lida com compra válida"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/buy", "AAAA", "4")
              .content(r"112\.00", "112.00")
              .content(r"9,?888\.00", "9,888.00"))


@check50.check(compra_lida_valida)
def pagina_venda():
    """página de venda tem todos os elementos necessários"""
    (Finance().login("_cs50", "ohHai28!")
              .validate_form("/sell", ["shares"])
              .validate_form("/sell", ["symbol"], field_tag="select"))


@check50.check(compra_lida_valida)
def venda_trata_acoes_invalidas():
    """venda trata número inválido de ações"""
    Finance().login("_cs50", "ohHai28!").transaction("/sell", "AAAA", "8").status(400)


@check50.check(compra_lida_valida)
def venda_trata_valida():
    """venda trata venda válida"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/sell", "AAAA", "2")
              .content(r"56\.00", "56.00")
              .content(r"9,?944\.00", "9,944.00"))


class Finance(check50.flask.app):
    """Extensão da classe flask.App que adiciona funções específicas do Finance"""

    APP_NAME = "app.py"

    def __init__(self):
        """Função auxiliar para registrar usuário"""
        super().__init__(self.APP_NAME)

    def register(self, username, password, confirmation):
        """Registrar novo usuário"""
        form = {"username": username, "password": password, "confirmation": confirmation}
        return self.post("/register", data=form)

    def login(self, username, password):
        """Função auxiliar para fazer login"""
        route = "/login"
        if self.page_exists("/signin"):
            route = "/signin"
        return self.post(route, data={"username": username, "password": password})

    def quote(self, ticker):
        """Consultar a aplicação para uma cotação para o `ticker`"""
        return self.post("/quote", data={"symbol": ticker})

    def transaction(self, route, symbol, shares):
        """Enviar solicitação para a `rota` ("/buy" ou "/sell") para realizar a transação relevante"""
        return self.post(route, data={"symbol": symbol, "shares": shares})

    def validate_form(self, route, fields, field_tag="input"):
        """Certificar-se de que o formulário HTML na `rota` possui campos de entrada fornecidos por `fields`"""
        if not isinstance(fields, list):
            fields = [fields]

        content = self.get(route).content()
        required = {field: False for field in fields}
        for tag in content.find_all(field_tag):
            try:
                name = tag.attrs["name"]
                if required[name]:
                    raise Error("encontrado mais de um campo chamado \"{}\"".format(name))
            except KeyError:
                pass
            else:
                check50.log("encontrado campo \"{}\" necessário".format(name))
                required[name] = True

        try:
            missing = next(name for name, found in required.items() if not found)
        except StopIteration:
            pass
        else:
            raise check50.Failure(f"esperado encontrar campo {field_tag} com o nome \"{missing}\", mas nenhum foi encontrado")

        if content.find("button", type="submit") is None:
            raise check50.Failure("esperado botão para enviar formulário, mas nenhum foi encontrado")

        return self

    def page_exists(self, route):
        return self.get(route).status() == 200
```  