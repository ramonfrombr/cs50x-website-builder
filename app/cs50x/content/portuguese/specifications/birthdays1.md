# Laboratório 9: Aniversários

<div class="alert" data-alert="warning" role="alert">
<p>Você pode colaborar com um ou dois colegas neste laboratório, embora seja esperado que todos os estudantes, em qualquer grupo, contribuam igualmente para o laboratório.</p>
</div>

Crie um aplicativo da web para acompanhar os aniversários de amigos.

![captura de tela do site de aniversários](https://cs50.harvard.edu/x/2023/labs/9/birthdays.png)

## Começando

<div class="alert" data-alert="primary" role="alert">
<p>Começou o CS50x em 2021 ou antes e precisa migrar seu trabalho do CS50 IDE para o novo codespace do VS Code? Certifique-se de conferir nossas instruções sobre como <a href="../../new/">migrar</a> seus arquivos!</p>
</div>

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e execute `cd` sozinho. Você verá que seu "prompt" se parece com o exemplo abaixo.

    $

Clique dentro da janela do terminal e em seguida execute

    wget https://cdn.cs50.net/2022/fall/labs/9/birthdays.zip

seguido de Enter para baixar um arquivo ZIP chamado `birthdays.zip` em seu codespace. Certifique-se de não esquecer o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere!

Agora execute

    unzip birthdays.zip

para criar uma pasta chamada `birthdays`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm birthdays.zip

e responder com "y" seguido de Enter na solicitação para remover o arquivo ZIP que você baixou.

Agora digite

    cd birthdays

seguido de Enter para mover-se para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o exemplo abaixo.

    birthdays/ $

Se tudo correu bem, você deve executar

    ls

e você verá os seguintes arquivos e pastas:

    app.py  birthdays.db  static/  templates/

Se você encontrar algum problema, siga essas mesmas etapas novamente e veja se consegue identificar onde errou!

## Entendendo

No `app.py`, você encontrará o início de um aplicativo da web Flask. O aplicativo possui uma rota (`/`) que aceita tanto os pedidos `POST` (após o `if`) quanto os pedidos `GET` (após o `else`). Atualmente, quando a rota `/` é solicitada via `GET`, o modelo `index.html` é renderizado. Quando a rota `/` é solicitada via `POST`, o usuário é redirecionado de volta para `/` via `GET`.

`birthdays.db` é um banco de dados SQLite com uma tabela chamada `birthdays`, que possui quatro colunas: `id`, `name`, `month` e `day`. Já existem algumas linhas nesta tabela, embora, no final, seu aplicativo da web suportará a capacidade de inserir linhas nesta tabela!

No diretório `static`, há um arquivo chamado `styles.css` contendo o código CSS para este aplicativo da web. Não é necessário editar este arquivo, embora você possa fazê-lo se desejar!

No diretório `templates`, há um arquivo chamado `index.html` que será renderizado quando o usuário visualizar seu aplicativo da web.