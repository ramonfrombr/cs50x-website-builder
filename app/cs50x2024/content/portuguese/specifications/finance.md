<div class="alert alert-warning" data-alert="warning" role="alert"><p>Se você usou <code class="language-plaintext highlighter-rouge">wget</code> para baixar <code class="language-plaintext highlighter-rouge">finance.zip</code> antes das <a data-local="2024-04-10T08:30:00-04:00" href="https://time.cs50.io/20240410T083000-0400">2024-04-10T08:30:00-04:00</a>, certifique-se de copiar, colar e executar este comando <em>dentro do seu diretório <code>finance</code></em> para baixar uma versão mais recente de <code class="language-plaintext highlighter-rouge">helpers.py</code>:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>[ -f helpers.py ] &amp;&amp; curl -O https://cdn.cs50.net/2024/x/psets/9/finance/helpers.py
</code></pre></div></div></div>

# C$50 Finanças

Implemente um site no qual usuários podem "comprar" e "vender" ações, como abaixo.

![C$50 Finanças](https://cs50.harvard.edu/x/2024/psets/9/finance/finance_2024.png)

## Histórico

Se você não tem certeza sobre o que significa comprar e vender ações (por ex., as porcentagens de uma empresa), vá [aqui](https://www.investopedia.com/articles/basics/06/invest1000.asp) para um tutorial.

Você está prestes a implementar o C$50 Finanças, um aplicativo web no qual você pode gerenciar portfólios de ações. Essa ferramenta não só permitirá que você confira os preços reais das ações e os valores dos portfólios, como também permitirá que você compre (ok, "compre") e venda (ok, "venda") ações consultando os preços das ações.

De fato, existem ferramentas (uma é conhecida como IEX) que permitem que você baixe cotações de ações pela API (interface de programação de aplicativos) usando URLs como `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Observe como o símbolo da Netflix (NFLX) está embutido neste URL; é assim que o IEX sabe de quem deve retornar os dados. Esse link não retornará nenhum dado porque o IEX exige que você use uma chave de API, mas se retornasse, você veria uma resposta no formato JSON (JavaScript Object Notation) como este:

    {
      "avgTotalVolume":6787785,
      "calculationPrice":"tops",
      "change":1.46,
      "changePercent":0.00336,
      "close":null,
      "closeSource":"official",
      "closeTime":null,
      "companyName":"Netflix Inc.",
      "currency":"USD",
      "delayedPrice":null,
      "delayedPriceTime":null,
      "extendedChange":null,
      "extendedChangePercent":null,
      "extendedPrice":null,
      "extendedPriceTime":null,
      "high":null,
      "highSource":"IEX real time price",
      "highTime":1699626600947,
      "iexAskPrice":460.87,
      "iexAskSize":123,
      "iexBidPrice":435,
      "iexBidSize":100,
      "iexClose":436.61,
      "iexCloseTime":1699626704609,
      "iexLastUpdated":1699626704609,
      "iexMarketPercent":0.00864679844447232,
      "iexOpen":437.37,
      "iexOpenTime":1699626600859,
      "iexRealtimePrice":436.61,
      "iexRealtimeSize":5,
      "iexVolume":965,
      "lastTradeTime":1699626704609,
      "latestPrice":436.61,
      "latestSource":"IEX real time price",
      "latestTime":"9:31:44 AM",
      "latestUpdate":1699626704609,
      "latestVolume":null,
      "low":null,
      "lowSource":"IEX real time price",
      "lowTime":1699626634509,
      "marketCap":192892118443,
      "oddLotDelayedPrice":null,
      "oddLotDelayedPriceTime":null,
      "open":null,
      "openTime":null,
      "openSource":"official",
      "peRatio":43.57,
      "previousClose":435.15,
      "previousVolume":2735507,
      "primaryExchange":"NASDAQ",
      "symbol":"NFLX",
      "volume":null,
      "week52High":485,
      "week52Low":271.56,
      "ytdChange":0.4790450244167119,
      "isUSMarketOpen":true
    }

Observe como, entre as chaves, há uma lista separada por vírgulas de pares chave-valor, com dois pontos separando cada chave do seu valor. Faremos algo muito parecido, com o Yahoo Finance.

Vamos nos concentrar agora em obter o código de distribuição deste problema!

## Começando

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` por si só. Você deve descobrir que o prompt da janela de terminal se parece com o abaixo:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2024/x/psets/9/finance.zip

para baixar um ZIP chamado `finance.zip` no seu espaço de código.

Então execute

    unzip finance.zip

para criar uma pasta chamada `finance`. Você não precisará mais do arquivo ZIP, então você pode executar

    rm finance.zip

e responder com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd finance

seguido de Enter para ir para (por ex., abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    finance/ $

Execute `ls` por si só e você verá alguns arquivos e pastas:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

Se você tiver algum problema, siga estes mesmos passos novamente e veja se consegue determinar onde errou!

### Execução

Inicie o servidor web integrado ao Flask (dentro de `finance/`):

    $ flask run

Visite a URL exibida por `flask` para ver o código de distribuição em ação. Você não conseguirá fazer login ou se registrar por enquanto!

Dentro de `finance/`, execute `sqlite3 finance.db` para abrir `finance.db` com o `sqlite3`. Se você executar `.schema` no prompt do SQLite, observe como `finance.db` vem com uma tabela chamada `users` (usuários). Dê uma olhada em sua estrutura (por ex., esquema). Observe como, por padrão, os novos usuários receberão US$ 10.000 em dinheiro. Mas se você executar `SELECT * FROM users;`, não haverá (ainda!) usuários (por ex., linhas) lá para navegar.

Outra forma de visualizar `finance.db` é com um programa chamado phpLiteAdmin. Clique em `finance.db` no navegador de arquivos do seu espaço de código e, em seguida, clique no link mostrado abaixo do texto "Please visit the following link to authorize GitHub Preview". Você deverá ver informações sobre o próprio banco de dados, bem como uma tabela, `users`, assim como viu no prompt `sqlite3` com `.schema`.

### Entendimento

#### `app.py`

Abra `app.py`. No início do arquivo há várias importações, entre elas o módulo SQL da CS50 e algumas funções auxiliares. Mais sobre elas em breve.

Depois de configurar o [Flask](https://flask.pocoo.org/), observe como esse arquivo desabilita o cache das respostas (desde que você esteja no modo de depuração, o que é ativado por padrão no seu código no Code50), para que você não faça uma alteração em algum arquivo e o seu navegador não perceba. Observe em seguida como ele configura o [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) com um "filtro" personalizado, `usd`, uma função (definida em `helpers.py`) que facilitará a formatação dos valores como dólares americanos (USD). Ele configura ainda o Flask para armazenar [sessões](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) no sistema de arquivos local (ou seja, disco) em vez de armazená-las dentro de cookies (assinalados digitalmente), que é o padrão do Flask. O arquivo então configura o módulo SQL da CS50 para usar o `finance.db`.

Depois disso, há várias rotas, das quais somente duas estão totalmente implementadas: `login` e `logout`. Leia a implementação de `login` primeiro. Observe como ele usa `db.execute` (da biblioteca da CS50) para consultar `finance.db`. E observe como ele usa `check_password_hash` para comparar hashes das senhas dos usuários. Observe também como `login` "lembra" que um usuário está conectado armazenando seu `user_id`, um INTEIRO, em `session`. Dessa forma, qualquer uma das rotas desse arquivo pode verificar qual usuário, se houver, está conectado. Finalmente, observe como, depois que o usuário tiver conectado com sucesso, `login` redirecionará para `"/", levando o usuário para sua página inicial. Enquanto isso, observe como `logout` simplesmente limpa `session`, efetivamente desconectando o usuário.

Observe como a maioria das rotas são "decoradas" com `@login_required` (uma função também definida em `helpers.py`). Esse decorador garante que, se um usuário tentar visitar qualquer uma dessas rotas, ele será primeiro redirecionado para `login` para se conectar.

Observe também como a maioria das rotas suporta GET e POST. No entanto, a maioria delas (por enquanto!) simplesmente retorna um "pedido de desculpas", já que ainda não foram implementadas.

#### `helpers.py`

Em seguida, dê uma olhada em `helpers.py`. Ah, aí está a implementação de `apology`. Observe como ela acaba renderizando um template, `apology.html`. Por acaso ela também define internamente outra função, `escape`, que ela simplesmente usa para substituir caracteres especiais em pedidos de desculpas. Ao definir `escape` dentro de `apology`, nós escopaamos a primeira apenas para a segunda; nenhuma outra função conseguirá (ou precisará) chamá-la.

O próximo no arquivo é `login_required`. Não se preocupe se ela for um pouco críptica, mas se você já se perguntou como uma função pode retornar outra função, aqui está um exemplo!

Depois dela vem `lookup`, uma função que, dado um `símbolo` (ex.: NFLX), retorna uma cotação de ações para uma empresa na forma de um `dict` com duas chaves: `price`, cujo valor é um `float`; e `symbol`, cujo valor é uma `str`, uma versão padronizada (em caixa alta) do símbolo de uma ação, independentemente de como aquele símbolo foi escrito em caixa alta ou baixa quando passado para `lookup`.

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Observação.  Se você começou esse problema em 2023, observe que <code class="language-plaintext highlighter-rouge">lookup</code> não retorna mais uma chave de <code class="language-plaintext highlighter-rouge">name</code>, portanto, remova-a de qualquer consulta que a espere. Nenhum nome precisa ser exibido em nenhuma página.</p></div>

O último no arquivo é `usd`, uma função curta que simplesmente formata um `float` como USD (ex.: `1234.56` é formatado como `$1,234.56`).

#### `requirements.txt`

Agora dê uma olhada rápida em `requirements.txt`. Esse arquivo simplesmente prescreve os pacotes dos quais esse aplicativo dependerá.

#### `static/`

Dê uma olhada também em `static/`, dentro do qual está `styles.css`. É lá que fica parte do CSS inicial. Fique à vontade para alterá-lo como quiser.

#### `templates/`

Agora olhe em `templates/`. Em `login.html` há, essencialmente, um formulário HTML, estilizado com [Bootstrap](https://getbootstrap.com/). Enquanto isso, em `apology.html`, há um template para um pedido de desculpas. Lembre-se de que `apology` em `helpers.py` recebeu dois argumentos: `message`, que foi passado para `render_template` como o valor de `bottom`, e, opcionalmente, `code`, que foi passado para `render_template` como o valor de `top`. Observe em `apology.html` como esses valores são usados no final! E [aqui está o motivo](https://github.com/jacebrowning/memegen) 0:-)

Por último, vem `layout.html`. Ele é um pouco maior do que o normal, mas isso ocorre principalmente porque ele vem com uma "navbar" (barra de navegação) sofisticada e otimizada para dispositivos móveis, também baseada no Bootstrap. Observe como ele define um bloco, `main`, dentro do qual os templates (incluindo `apology.html` e `login.html`) devem ir. Ele também inclui suporte para o [message flashing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing) do Flask, para que você possa transmitir mensagens de uma rota para outra para que o usuário as veja.

## Especificação

### `register`

Conclua a implementação de `register` de forma que permita que um usuário se cadastre para uma conta por meio de um formulário.

- Exija que o usuário insira um nome de usuário, implementado como um campo de texto cujo `name` é `username`. Renderize um pedido de desculpas se a entrada do usuário estiver em branco ou se o nome de usuário já existir.
  - Observe que [`cs50.SQL.execute`](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL) lançará uma exceção `ValueError` se você tentar `INSERT` um nome de usuário duplicado porque criamos um `UNIQUE INDEX` em `users.username`. Portanto, certifique-se de usar `try` e `except` para determinar se o nome de usuário já existe.
- Exija que o usuário insira uma senha, implementada como um campo de texto cujo `name` é `password`, e em seguida a mesma senha novamente, implementada como um campo de texto cujo `name` é `confirmation`. Renderize um pedido de desculpas se uma das entradas estiver em branco ou se as senhas não corresponderem.
- Envie a entrada do usuário via `POST` para `/register`.
- `INSERT` o novo usuário em `users`, armazenando um hash da senha do usuário, não a senha em si. Criptografe a senha do usuário com [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.security.generate_password_hash) Provavelmente você vai querer criar um novo template (ex.: `register.html`) que seja bem semelhante a `login.html`.

Depois de implementar `register` corretamente, você deve conseguir se cadastrar para obter uma conta e conectar-se (já que `login` e `logout` já funcionam)! E você deve conseguir ver suas linhas pelo phpLiteAdmin ou `sqlite3`.

### `quote`

Conclua a implementação de `quote` de forma que permita que um usuário procure o preço atual de uma ação.

- Exija que o usuário insira o símbolo de uma ação, implementado como um campo de texto cujo `name` é `symbol`.
- Envie a entrada do usuário via `POST` para `/quote`.
- Provavelmente você vai querer criar dois novos templates (ex.: `quote.html` e `quoted.html`). Quando um usuário visita `/quote` via GET, renderize um desses templates, dentro do qual deve haver um formulário HTML que envia para `/quote` via POST. Em resposta a um POST, `quote` pode renderizar esse segundo template, incorporando a ele um ou mais valores de `lookup`.

### `buy`

Complete a implementação de `buy` de forma que permita que o usuário compre ações.

- Exija que o usuário informe um símbolo de ação, implementado como um campo de texto cujo `name` seja `symbol`. Renderize um pedido de desculpas se a entrada estiver em branco ou o símbolo não existir (de acordo com o valor de retorno de `lookup`).
- Exija que o usuário insira um número de ações, implementado como um campo de texto cujo `name` seja `shares`. Renderize um pedido de desculpas se a entrada não for um número inteiro positivo.
- Envie a entrada do usuário via `POST` para `/buy`.
- Após a conclusão, redirecione o usuário para a página inicial.
- Provavelmente, você desejará chamar `lookup` para consultar o preço atual de uma ação.
- Provavelmente, você desejará `SELECIONAR` quanto dinheiro o usuário tem atualmente em `users`.
- Adicione uma ou mais tabelas novas ao `finance.db` para manter o controle da compra. Armazene informações suficientes para saber quem comprou o quê, a que preço e quando.
  - Use tipos SQLite apropriados.
  - Defina índices `UNIQUE` em quaisquer campos que devem ser exclusivos.
  - Defina índices (não `UNIQUE`) em quaisquer campos pelos quais você pesquisará (como por meio de `SELECT` com `WHERE`).
- Renderize um pedido de desculpas, sem concluir a compra, se o usuário não puder comprar o número de ações ao preço atual.
- Você não precisa se preocupar com condições de corrida (ou usar transações).

Depois de implementar `buy` corretamente, você poderá ver as compras dos usuários em suas novas tabelas no phpLiteAdmin ou `sqlite3`.

### `index`

Complete a implementação de `index` de forma que exiba uma tabela HTML resumindo, para o usuário atualmente conectado, quais ações o usuário possui, o número de ações possuídas, o preço atual de cada ação e o valor total de cada participação (ou seja, ações vezes preço). Exiba também o saldo atual de caixa do usuário e o total geral (ou seja, valor total das ações mais o dinheiro).

- Provavelmente, você desejará executar vários `SELECT`s. Dependendo de como você implementar sua(s) tabela(s), você poderá encontrar [GROUP BY](https://www.google.com/search?q=SQLite+GROUP+BY,) [HAVING](https://www.google.com/search?q=SQLite+HAVING,) [SUM](https://www.google.com/search?q=SQLite+SUM,) e/ou [WHERE](https://www.google.com/search?q=SQLite+WHERE) de seu interesse.
- Provavelmente, você desejará chamar `lookup` para cada ação.

### `sell`

Complete a implementação de `sell` para que permita que o usuário venda ações de uma ação (que ele possui).

- Requeira que o usuário insira um símbolo de ação, implementado como um menu `select` cujo `name` seja `symbol`. Renderize um pedido de desculpas se o usuário não selecionar uma ação ou se (de alguma forma, depois de enviar) o usuário não possuir nenhuma ação daquela ação.
- Exija que o usuário insira um número de ações, implementado como um campo de texto cujo `name` seja `shares`. Renderize um pedido de desculpas se a entrada não for um número inteiro positivo ou se o usuário não possuir tantas ações da ação.
- Envie a entrada do usuário via `POST` para `/sell`.
- Após a conclusão, redirecione o usuário para a página inicial.
- Você não precisa se preocupar com condições de corrida (ou usar transações).

### `history`

Complete a implementação de `history` de forma que exiba uma tabela HTML resumindo todas as transações de um usuário, listando linha por linha cada compra e venda.

- Para cada linha, deixe claro se uma ação foi comprada ou vendida e inclua o símbolo da ação, o preço (de compra ou venda), o número de ações compradas ou vendidas e a data e hora em que a transação ocorreu.
- Talvez seja necessário alterar a tabela criada para `buy` ou complementá-la com uma tabela adicional. Tente minimizar redundâncias.

### Toque pessoal

Implemente pelo menos um toque pessoal de sua escolha:

- Permita que os usuários alterem suas senhas.
- Permita que os usuários adicionem dinheiro extra à sua conta.
- Permita que os usuários comprem mais ações ou vendam ações que já possuem no próprio `index`, sem precisar digitar os símbolos das ações manualmente.
- Implemente algum outro recurso de escopo comparável.

## Passo a passo

<div class="alert alert-info" data-alert="info" role="alert"><p>Observe que Brian menciona que <code class="language-plaintext highlighter-rouge">lookup</code> retornará o nome da ação. Conforme acima, agora ele retorna apenas o preço e o símbolo.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Testes

Certifique-se de testar seu aplicativo da web manualmente, como

- registrando um novo usuário e verificando se a página do portfólio é carregada com as informações corretas,
- solicitando uma cotação usando um símbolo de ação válido,
- comprando uma ação várias vezes, verificando se o portfólio exibe totais corretos,
- vendendo todas ou algumas ações, verificando o portfólio novamente e
- verificando se a página do histórico mostra todas as transações do usuário conectado.

Também teste alguns usos inesperados, como

- inserindo strings alfabéticas em formulários quando apenas números são esperados,
- inserindo zero ou números negativos em formulários quando apenas números positivos são esperados,
- inserindo valores de pontos flutuantes em formulários quando apenas inteiros são esperados,
- tentando gastar mais dinheiro do que o usuário tem,
- tentando vender mais ações do que o usuário tem,
- inserindo um símbolo de ação inválido e
- incluindo caracteres potencialmente perigosos, como `'` e `;` em consultas SQL.

Você também pode verificar a validade do HTML clicando no botão **I ♥ VALIDATOR** no rodapé de cada uma das suas páginas, que enviará seu HTML para [validator.w3.org](https://validator.w3.org/).

Após a satisfação, para testar seu código com `check50`, execute o abaixo.

    check50 cs50/problems/2024/x/finance

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Esteja ciente de que <code class="language-plaintext highlighter-rouge">check50</code> testará todo o seu programa como um todo. Se você o executar <strong>antes</strong> de concluir todas as funções necessárias, ele poderá relatar erros em funções que são realmente corretas, mas dependem de outras funções.</p></div>

## Estilo

    style50 app.py

## Solução do corpo docente

Você é bem-vindo para estilizar seu próprio aplicativo de forma diferente, mas é assim que a solução do corpo docente se parece!

[https://finance.cs50.net/](https://finance.cs50.net/)

Sinta-se à vontade para se registrar para obter uma conta e brincar com o app. **Não** use uma senha que você usa em outros sites.

É **razoável** olhar para o HTML e CSS do corpo docente.

## Dicas

- Para formatar um valor como um valor em dólar dos EUA (com centavos listados em duas casas decimais), você pode usar o filtro `usd` em seus modelos Jinja (imprimindo valores como `{{ value | usd }}` em vez de `{{ value }}`.
- Dentro de `cs50.SQL` há um método `execute` cujo primeiro argumento deve ser uma `str` de SQL. Se essa `str` contiver parâmetros de ponto de interrogação aos quais valores devem ser vinculados, esses valores podem ser fornecidos como parâmetros nomeados adicionais para `execute`. Veja a implementação de `login` para um exemplo. O valor de retorno de `execute` é o seguinte:
  - Se `str` for um `SELECT`, então `execute` retornará uma `list` de zero ou mais objetos `dict`, dentro dos quais estão chaves e valores representando campos de uma tabela e células, respectivamente.
  - Se `str` for um `INSERT`, e a tabela na qual os dados foram inseridos contiver uma `PRIMARY KEY` de autoincremento, então `execute` retornará o valor da chave primária da linha recém-inserida.
  - Se `str` for um `DELETE` ou um `UPDATE`, então `execute` retornará o número de linhas excluídas ou atualizadas por `str`.
- Lembre-se que `cs50.SQL` registrará em sua janela de terminal todas as consultas que você executar via `execute` (para que você possa confirmar se elas estão conforme o esperado).
- Certifique-se de usar parâmetros vinculados a ponto de interrogação (ou seja, um [paramstyle](https://www.python.org/dev/peps/pep-0249/#paramstyle) de `named`) ao chamar o método `execute` do CS50, à la `WHERE ?`. **Não** use f-strings, [`format`](https://docs.python.org/3.6/library/functions.html#format,) ou `+` (ou seja, concatenação), para que você não corra o risco de um ataque de injeção de SQL.
- Se (e somente se) já estiver confortável com SQL, você pode usar [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) ou [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org/) (ou seja, [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/index.html)) em vez de `cs50.SQL`.
- Você pode adicionar arquivos estáticos adicionais em `static/`.
- Provavelmente você desejará consultar a [documentação do Jinja](https://jinja.palletsprojects.com/en/3.1.x/) ao implementar seus modelos.
- É **razoável** pedir a outras pessoas para testar (e tentar acionar erros em) seu site.
- Você pode alterar a estética dos sites, como via
  - [bootswatch.com](https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/), e/ou
  - [memegen.link](https://memegen.link/).
- Você pode achar a [documentação do Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) e a [documentação do Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) úteis!

## FAQs

### ImportError: No module named ‘application’

Por padrão, `flask` procura um arquivo chamado `app.py` em seu diretório de trabalho atual (porque configuramos o valor de `FLASK_APP`, uma variável de ambiente, para ser `app.py`). Se ver este erro, provavelmente você executou `flask` no diretório errado!

### OSError: \[Errno 98\] Address already in use

Se, ao executar `flask`, você vir este erro, provavelmente (ainda) tem `flask` sendo executado em outra aba. Certifique-se de encerrar aquele outro processo, como com ctrl-c, antes de iniciar `flask` novamente. Se você não tiver nenhuma outra aba, execute `fuser -k 8080/tcp` para encerrar quaisquer processos que (ainda) estejam escutando na porta TCP 8080.

## Como enviar

Em seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2024/x/finance

<div class="alert alert-danger" data-alert="danger" role="alert"><h3 id="why-does-my-submission-pass-check50-but-shows-no-results-in-my-gradebook-after-running-submit50">Por que minha submissão passa pelo check50, mas mostra "Sem resultados" em meu Gradebook após executar submit50?</h3>

<p>Em alguns casos, <code class="language-plaintext highlighter-rouge">submit50</code> pode não avaliar a atribuição devido a (1) formatação inconsistente em seu arquivo <code class="language-plaintext highlighter-rouge">app.py</code> e/ou (2) arquivos adicionais desnecessários sendo enviados com o conjunto de problemas. Para corrigir esses problemas, execute <code class="language-plaintext highlighter-rouge">black app.py</code> na pasta <code class="language-plaintext highlighter-rouge">finance</code>. Resolva quaisquer problemas que sejam revelados. Em seguida, examine o conteúdo de sua pasta <code class="language-plaintext highlighter-rouge">finance</code>. Exclua arquivos estranhos, como sessões do flask ou outros arquivos que não fazem parte de sua implementação do conjunto de problemas. Além disso, execute <code class="language-plaintext highlighter-rouge">check50</code> novamente para garantir que sua submissão ainda funcione. Por fim, execute o comando <code class="language-plaintext highlighter-rouge">submit50</code> acima novamente. Seu resultado aparecerá em seu <a href="https://cs50.me/cs50x">Gradebook</a> em alguns minutos.</p>

<p>Observe que se houver uma pontuação numérica ao lado de sua submissão de finanças na área <code class="language-plaintext highlighter-rouge">submissions</code> do seu <a href="https://cs50.me/cs50x">Gradebook</a>, o procedimento discutido acima não se aplica a você. Provavelmente, você não atendeu totalmente aos requisitos do conjunto de problemas e deve confiar no <code class="language-plaintext highlighter-rouge">check50</code> para obter pistas sobre que trabalho resta.</p></div>

