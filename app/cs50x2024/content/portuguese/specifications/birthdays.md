# Aniversários

![captura de tela do site de aniversários](https://cs50.harvard.edu/x/2024/psets/9/birthdays/birthdays.png)

## Problema a resolver

Crie um aplicativo web para manter um registro dos aniversários dos amigos.

## Introdução

Abra [VS Code](https://cs50.dev/).

Comece clicando dentro da janela do terminal e, em seguida, execute `cd` sozinho. Você verá que o "prompt" se assemelha ao abaixo.

    $

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2023/fall/psets/9/birthdays.zip

seguido de Enter para baixar um ZIP chamado `birthdays.zip` no seu codespace. Tome cuidado para não esquecer o espaço entre `wget` e a URL a seguir, ou qualquer outro caractere!

Agora execute

    unzip birthdays.zip

para criar uma pasta chamada `birthdays`. Você não precisará mais do arquivo ZIP, portanto, execute

    rm birthdays.zip

e responda com "y" seguido por Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd birthdays

seguido por Enter para se mover (ou seja, abrir) esse diretório. Seu prompt agora deve se assemelhar ao abaixo.

    birthdays/ $

Se tudo ocorreu bem, execute

    ls

e você verá os seguintes arquivos e pastas:

    app.py  birthdays.db  static/  templates/

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde errou!

## Compreensão

Em `app.py`, você encontrará o início de um aplicativo web Flask. O aplicativo tem uma rota (`/`) que aceita solicitações `POST` (após o `if`) e `GET` (após o `else`). Atualmente, quando a rota `/` é solicitada via `GET`, o template `index.html` é renderizado. Quando a rota `/` é solicitada via `POST`, o usuário é redirecionado de volta para `/` via `GET`.

`birthdays.db` é um banco de dados SQLite com uma tabela, `birthdays`, que possui quatro colunas: `id`, `name`, `month` e `day`. Já existem algumas linhas nesta tabela, embora, em última análise, seu aplicativo web suporte a capacidade de inserir linhas nesta tabela!

No diretório `static` há um arquivo `styles.css` contendo o código CSS para este aplicativo web. Não é necessário editar este arquivo, embora você possa fazê-lo se desejar!

No diretório `templates` há um arquivo `index.html` que será renderizado quando o usuário visualizar seu aplicativo web.

## Detalhes da implementação

Conclua a implementação de um aplicativo web para permitir que os usuários armazenem e mantenham registros de aniversários.

- Quando a rota `/` for solicitada via `GET`, seu aplicativo web deverá exibir, em uma tabela, todas as pessoas do seu banco de dados juntamente com seus aniversários.
  - Primeiro, em `app.py`, adicione lógica no tratamento da solicitação `GET` para consultar o banco de dados `birthdays.db` para todos os aniversários. Passe todos esses dados para o seu template `index.html`.
  - Em seguida, em `index.html`, adicione lógica para renderizar cada aniversário como uma linha na tabela. Cada linha deve ter duas colunas: uma para o nome da pessoa e outra para o aniversário da pessoa.
- Quando a rota `/` é solicitada via `POST`, seu aplicativo web deve adicionar um novo aniversário ao seu banco de dados e, em seguida, renderizar novamente a página de índice.
  - Primeiro, em `index.html`, adicione um formulário HTML. O formulário deve permitir que os usuários digitem um nome, um mês de aniversário e um dia de aniversário. Certifique-se de que o formulário seja enviado para `/` (sua "ação") com um método `post`.
  - Então, em `app.py`, adicione lógica no tratamento da solicitação `POST` para `INSERT` uma nova linha na tabela `birthdays` com base nos dados fornecidos pelo usuário.

Opcionalmente, você também pode:

- Adicionar a capacidade de excluir e/ou editar entradas de aniversário.
- Adicionar quaisquer recursos adicionais de sua escolha!

## Dicas

### Crie um formulário por meio do qual os usuários possam enviar aniversários

Em `index.html`, observe o seguinte TODO:

    <!-- TODO: Criar um formulário para que os usuários enviem um nome, um mês e um dia -->

Lembre-se que, para criar um formulário, você pode usar o elemento HTML `form`. Você pode criar um elemento HTML `form` com as seguintes tags de abertura e fechamento:

    <form>
    </form>

Claro, um formulário ainda precisa de campos de entrada (e um botão por meio do qual o usuário pode enviar o formulário!). Lembre-se que os elementos HTML `input` criam, entre outras coisas, caixas de entrada em um formulário. Você pode especificar o atributo `type` para permitir a aceitação de `texto` ou `números`. Forneça também os elementos `input` com um atributo `name` para que você possa diferenciá-los.

    <form>
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
    </form>

Seu formulário pode se beneficiar de um botão no qual o usuário possa clicar para enviar seus dados. Adicione um elemento `input` do tipo `submit`, o que permitirá que o usuário faça exatamente isso. Se você quiser que o próprio botão tenha um texto explicativo, tente definir o atributo `value`.

    <form>
        <input name="name" placeholder="Nome" type="text">
        <input name="month" placeholder="Mês" type="number">
        <input name="day" placeholder="Dia" type="number">
        <input type="submit" value="Adicionar aniversário">
    </form>

Para onde os dados do usuário serão enviados? Atualmente, para lugar nenhum! Lembre-se de que você pode especificar o atributo `action` de um formulário para ditar qual rota deve ser solicitada após o envio do formulário. Os dados do formulário serão enviados junto com a solicitação resultante. O atributo `method` especifica qual método de solicitação HTTP usar ao enviar o formulário.

    <form action="/" method="post">
        <input name="name" placeholder="Nome" type="text">
        <input name="month" placeholder="Mês" type="number">
        <input name="day" placeholder="Dia" type="number">
        <input type="submit" value="Adicionar aniversário">
    </form>

Com isso, seu formulário deve estar perfeitamente funcional, embora ainda possa ser aprimorado! Considere adicionar valores `placeholder` para melhorar um pouco as coisas:

    <form action="/" method="post">
        <input name="name" placeholder="Nome" type="text">
        <input name="month" placeholder="Mês" type="number" min="1" max="12">
        <input name="day" placeholder="Dia" type="number" min="1" max="31">
        <input type="submit" value="Adicionar aniversário">
    </form>

E considere adicionar alguma _validação do lado do cliente_, para garantir que o usuário coopere com a intenção do seu formulário. Por exemplo, um campo `input` do tipo `number` também pode ter um atributo `min` e `max` especificado, que determinam o valor mínimo e máximo que um usuário pode inserir.

    <form action="/" method="post">
        <input name="name" placeholder="Nome" type="text">
        <input name="month" placeholder="Mês" type="number" min="1" max="12">
        <input name="day" placeholder="Dia" type="number" min="1" max="31">
        <input type="submit" value="Adicionar aniversário">
    </form>

### Adicione o envio de formulários de um usuário ao banco de dados

Em `app.py`, observe a seguinte tarefa pendente:

    # TODO: Adicione a entrada do usuário ao banco de dados

Lembre-se de que o Flask tem alguns métodos úteis para acessar dados de formulário enviados por `POST`! Em especial:

    # Acesse dados de formulário
    request.form.get(NOME)

em que `NOME` refere-se ao atributo `name` do elemento `input` específico com dados enviados. Se os elementos `input` forem nomeados como `nome`, `mês` e `dia`, você poderá acessar (e armazenar!) seus respectivos valores com:

    # Acesse dados de formulário
    nome = request.form.get("nome")
    mês = request.form.get("mês")
    dia = request.form.get("dia")

Agora, os valores enviados pelo usuário nos elementos de entrada `nome`, `mês` e `dia` estão disponíveis para você como variáveis Python.

O próximo passo é adicionar esses valores ao seu banco de dados! Graças a esta linha em particular

    db = SQL("sqlite:///birthdays.db")

`app.py` já estabeleceu uma conexão com `birthdays.db` sob o nome `db`. Agora você pode executar consultas SQL chamando `db.execute` com uma consulta SQL válida. Se você quiser adicionar o aniversário de Carter em 1º de janeiro, poderá executar a seguinte instrução SQL:

    INSERT INTO birthdays (name, month, day) VALUES('Carter', 1, 1);

Configure o `app.py` para executar a mesma consulta, mas com espaços reservados para os valores a inserir, conforme a seguir:

    # Acesse dados de formulário
    nome = request.form.get("nome")
    mês = request.form.get("mês")
    dia = request.form.get("dia")

    # Insira dados no banco de dados
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", nome, mês, dia)

E isso deve bastar! Tente enviar o formulário, abrindo `birthdays.db` e usando uma consulta `SELECT` para visualizar o conteúdo da tabela `birthdays`. Você deve ver os dados do formulário enviado disponíveis para você.

À medida que você cria aplicativos mais avançados, também vai querer adicionar _validação do lado do servidor_: ou seja, uma forma de verificar se os dados do usuário são válidos _antes_ de fazer qualquer outra coisa! Uma das primeiras validações que você pode fazer é se o usuário enviou algum dado! Se você tentar recuperar dados de formulário com `request.form.get` em que o usuário não enviou nada, `request.form.get` retornará uma string vazia. Você pode verificar esse valor no Python como a seguir:

    # Acesse dados do formulário
    nome = request.form.get("nome")
    if not nome:
        return redirect("/")

    mês = request.form.get("mês")
    if not mês:
        return redirect("/")

    dia = request.form.get("dia")
    if not dia:
        return redirect("/")

    # Insira dados no banco de dados
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", nome, mês, dia)

Agora, você não inserirá uma linha até ter certeza de que o usuário forneceu todos os dados necessários.

Algumas outras coisas ainda podem dar errado! E se o usuário não fornecer, de fato, um valor numérico para `mês` ou `dia`? Uma forma de verificar é `tentar` converter o valor em um inteiro com `int` e, se a conversão falhar, redirecionar o usuário de volta para a página inicial.

    # Acesse dados de formulário
    nome = request.form.get("nome")
    if not nome:
        return redirect("/")

    mês = request.form.get("mês")
    if not mês:
        return redirect("/")
    try:
        mês = int(mês)
    except ValueError:
        return redirect("/")

    dia = request.form.get("dia")
    if not dia:
        return redirect("/")
    try:
        dia = int(dia)
    except ValueError:
        return redirect("/")

    # Insira dados no banco de dados
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", nome, mês, dia)

E mesmo que o usuário insira um número, é melhor verificar se ele está na faixa correta!

    # Acesse dados de formulário
    nome = request.form.get("nome")
    if not nome:
        return redirect("/")

    mês = request.form.get("mês")
    if not mês:
        return redirect("/")
    try:
        mês = int(mês)
    except ValueError:
        return redirect("/")
    if mês < 1 ou mês > 12:
        return redirect("/")

    dia = request.form.get("dia")
    if not dia:
        return redirect("/")
    try:
        dia = int(dia)
    except ValueError:
        return redirect("/")
    if dia < 1 ou dia > 31:
        return redirect("/")

    # Insira dados no banco de dados
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", nome, mês, dia)

### Renderizando aniversários em `birthdays.db`

Uma vez que o usuário possa enviar aniversários e armazená-los em `birthdays.db`, sua próxima tarefa é garantir que esses aniversários sejam renderizados em `index.html`.

Primeiro, você precisará recuperar todos os aniversários de `birthdays.db`. Você pode fazer isso com a consulta SQL:

    SELECT * FROM birthdays;

Veja o seguinte TODO em `app.py`:

    # TODO: Exibir as entradas no banco de dados em index.html

Considere configurar `app.py` para executar essa consulta SQL cada vez que a página for carregada com uma solicitação `GET`:

    # Consultar todos os aniversários
    birthdays = db.execute("SELECT * FROM birthdays")

Agora, todos os aniversários na tabela `birthdays` de `birthdays.db` estão disponíveis para você em uma variável Python chamada `birthdays`. Em particular, os resultados da consulta SQL são armazenados como uma lista de dicionários. Cada dicionário representa uma linha retornada pela consulta, e cada chave no dicionário corresponde a um nome de coluna da tabela `birthdays` (por exemplo, “nome”, “mês” e “dia”).

Para renderizar esses aniversários em `index.html`, você pode contar com a função `render_template` do Flask. Você pode especificar que `index.html` deve ser renderizado com a variável `birthdays` especificando um argumento de palavra-chave, também chamado `birthdays`, e definindo-o igual à variável `birthdays` que você acabou de criar.

    # Consultar todos os aniversários
    birthdays = db.execute("SELECT * FROM birthdays")

    # Renderizar a página de aniversários
    return render_template("index.html", birthdays=birthdays)

Para esclarecer, o nome no lado esquerdo do `=`, `birthdays`, é o nome pelo qual você pode acessar os dados dos aniversários dentro do próprio `index.html`.

Agora que `index.html` está sendo renderizado com acesso aos dados de aniversários, você pode usar Jinja para renderizar os dados corretamente. Jinja, como Python, pode percorrer os elementos de uma lista. E Jinja, como Python, pode acessar os elementos de um dicionário por suas chaves. Nesse caso, a sintaxe Jinja para fazer isso é o nome do dicionário, seguido por um `.`, e, em seguida, o nome da chave para acessar.

    {% for birthday in birthdays %}
        <tr>
            <td></td>
            <td>/</td>
        </tr>
    {% endfor %}

E é isso! Tente recarregar a página para ver os aniversários renderizados.

### Passo a passo

<div class="alert alert-primary" data-alert="primary" role="alert"><p>Este vídeo foi gravado quando o curso ainda usava o CS50 IDE para escrever o código. Embora a interface possa parecer diferente do seu espaço de código, o comportamento dos dois ambientes deve ser bastante semelhante!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/HXwvj8x1Fcs"></iframe>

<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/lVwv4o8vmvI"></iframe></details>

### Testando

Sem `check50` para este conjunto de problemas! Mas certifique-se de testar sua aplicação web adicionando alguns aniversários e garantindo que os dados apareçam em sua tabela conforme o esperado.

Execute `flask run` em seu terminal enquanto estiver no diretório `birthdays` para iniciar um servidor web que atenda sua aplicação Flask.

## Como enviar

    submit50 cs50/problems/2024/x/birthdays

