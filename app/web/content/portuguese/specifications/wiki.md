# Wiki

<div class="alert alert-warning" data-alert="warning" role="alert">
<p>O CS50W não apresenta correspondência direta entre as aulas e os projetos. Se você está tentando fazer este projeto sem ter assistido pelo menos aula 3, está tentando cedo demais!</p>
</div>

Projete um enciclopédia online semelhante à Wikipedia.

## Antecedentes

A [Wikipedia](https://www.wikipedia.org/) é uma enciclopédia online gratuita que consiste em uma série de entradas de enciclopédia sobre diversos tópicos.

Cada entrada de enciclopédia pode ser visualizada visitando a página dessa entrada. Ao visitar [https://en.wikipedia.org/wiki/HTML](https://en.wikipedia.org/wiki/HTML), por exemplo, você visualiza a entrada da Wikipedia para HTML. Observe que o nome da página solicitada (HTML) é especificado na rota `/wiki/HTML`. Reconheça também que o conteúdo da página deve ser apenas HTML que seu navegador renderiza.

Na prática, seria tedioso se cada página na Wikipedia tivesse que ser escrita em HTML. Em vez disso, pode ser útil armazenar as entradas da enciclopédia usando uma linguagem de marcação mais leve e amigável para humanos. A Wikipedia utiliza uma linguagem de marcação chamada [Wikitext](https://en.wikipedia.org/wiki/Help:Wikitext), mas para este projeto, vamos armazenar as entradas da enciclopédia usando uma linguagem de marcação chamada Markdown.

Leia o guia do Markdown do GitHub em [GitHub’s Markdown guide](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) para entender como funciona a sintaxe do Markdown. Preste atenção, em particular, em como a sintaxe do Markdown se parece para títulos, texto em negrito, links e listas.

Ao ter um arquivo Markdown representando cada entrada da enciclopédia, podemos tornar nossas entradas mais amigáveis para escrita e edição. Quando um usuário visualiza nossa entrada da enciclopédia, no entanto, precisaremos converter esse Markdown em HTML antes de exibi-lo para o usuário.

## Começando

- Baixe o código de distribuição em [https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip](https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip) e descompacte-o.

## Entendendo

No código de distribuição, há um projeto Django chamado `wiki` que contém um único aplicativo chamado `encyclopedia`.

Primeiramente, abra `encyclopedia/urls.py`, onde a configuração de URL para este aplicativo é definida. Observe que iniciamos com uma única rota padrão associada à função `views.index`.

Em seguida, olhe para `encyclopedia/util.py`. Você não precisará modificar nada neste arquivo, mas observe que existem três funções que podem ser úteis para interagir com as entradas da enciclopédia. `list_entries` retorna uma lista com os nomes de todas as entradas de enciclopédia salvas atualmente. `save_entry` salvará uma nova entrada de enciclopédia, dado seu título e algum conteúdo em Markdown. `get_entry` recuperará uma entrada da enciclopédia pelo seu título, retornando seu conteúdo em Markdown se a entrada existir ou `None` se a entrada não existir. Qualquer uma das views que você escrever pode usar essas funções para interagir com as entradas da enciclopédia.

Cada entrada da enciclopédia será salva como um arquivo Markdown dentro do diretório `entries/`. Se você verificar lá agora, verá que pré-criamos algumas entradas de exemplo. Você pode adicionar mais!

Agora, vamos olhar para `encyclopedia/views.py`. Há apenas uma view aqui agora, a view `index`. Esta view retorna um template `encyclopedia/index.html`, fornecendo ao template uma lista de todas as entradas da enciclopédia (obtidas chamando `util.list_entries`, que vimos definido em `util.py`).

Você pode encontrar o template olhando para `encyclopedia/templates/encyclopedia/index.html`. Este template herda de um arquivo base `layout.html` e especifica qual deve ser o título da página e o que deve estar no corpo da página: neste caso, uma lista não ordenada de todas as entradas da enciclopédia. `layout.html`, por sua vez, define a estrutura mais ampla da página: cada página tem uma barra lateral com um campo de pesquisa (que por enquanto não faz nada), um link para ir para casa e links (que ainda não funcionam) para criar uma nova página ou visitar uma página aleatória.

## Especificação

Complete a implementação da sua enciclopédia Wiki. Você deve cumprir os seguintes requisitos:

- **Página da Entrada**: Ao visitar `/wiki/TÍTULO`, onde `TÍTULO` é o título de uma entrada da enciclopédia, deve renderizar uma página que exiba o conteúdo dessa entrada da enciclopédia.
  - A view deve obter o conteúdo da entrada da enciclopédia chamando a função `util` apropriada.
  - Se for solicitada uma entrada que não existe, o usuário deve ser apresentado com uma página de erro indicando que a página solicitada não foi encontrada.
  - Se a entrada existe, o usuário deve ser apresentado com uma página que exibe o conteúdo da entrada. O título da página deve incluir o nome da entrada.
- **Página de Índice**: Atualize `index.html` de forma que, em vez de listar apenas os nomes de todas as páginas na enciclopédia, o usuário possa clicar em qualquer nome de entrada para ser levado diretamente para aquela página de entrada.
- **Busca**: Permita ao usuário digitar uma consulta na caixa de pesquisa na barra lateral para pesquisar uma entrada da enciclopédia.
  - Se a consulta corresponder ao nome de uma entrada da enciclopédia, o usuário deve ser redirecionado para a página daquela entrada.
  - Se a consulta não corresponder ao nome de uma entrada da enciclopédia, o usuário deve ser levado a uma página de resultados de pesquisa que exibe uma lista de todas as entradas da enciclopédia que têm a consulta como uma substring. Por exemplo, se a consulta de pesquisa for `ytho`, então `Python` deve aparecer nos resultados da pesquisa.
  - Clicar em qualquer um dos nomes das entradas na página de resultados da pesquisa deve levar o usuário para a página daquela entrada.
- **Nova Página**: Clicar em "Criar Nova Página" na barra lateral deve levar o usuário a uma página onde ele pode criar uma nova entrada da enciclopédia.
  - Os usuários devem poder inserir um título para a página e, em um [`textarea`](https://www.w3schools.com/tags/tag_textarea.asp), devem poder inserir o conteúdo em Markdown para a página.
  - Os usuários devem poder clicar em um botão para salvar sua nova página.
  - Quando a página é salva, se uma entrada de enciclopédia já existir com o título fornecido, o usuário deve ser apresentado com uma mensagem de erro.
  - Caso contrário, a entrada da enciclopédia deve ser salva no disco, e o usuário deve ser levado à página da nova entrada.
- **Editar Página**: Em cada página de entrada, o usuário deve poder clicar em um link para ser levado a uma página onde o usuário pode editar o conteúdo em Markdown daquela entrada em um `textarea`.
  - O `textarea` deve ser preenchido com o conteúdo em Markdown existente da página. (ou seja, o conteúdo existente deve ser o `value` inicial do `textarea`).
  - O usuário deve poder clicar em um botão para salvar as alterações feitas na entrada.
  - Uma vez que a entrada é salva, o usuário deve ser redirecionado de volta para a página daquela entrada.
- **Página Aleatória**: Clicar em "Página Aleatória" na barra lateral deve levar o usuário a uma entrada aleatória da enciclopédia.
- **Conversão de Markdown para HTML**: Em cada página de entrada, qualquer conteúdo em Markdown no arquivo da entrada deve ser convertido para HTML antes de ser exibido ao usuário. Você pode usar o pacote [`python-markdown2`](https://github.com/trentm/python-markdown2) para realizar esta conversão, instalável via `pip3 install markdown2`.
  - Desafio para aqueles mais confortáveis: Se estiver se sentindo mais confortável, tente implementar a conversão de Markdown para HTML sem usar bibliotecas externas, suportando títulos, texto em negrito, listas não ordenadas, links e parágrafos. Você pode achar útil [usar expressões regulares em Python](https://docs.python.org/3/howto/regex.html).

## Dicas

- Por padrão, ao substituir um valor em um template Django, o Django escapa o HTML do valor para evitar a exibição de HTML indesejado. Se deseja permitir que uma sequência HTML seja exibida, você pode fazer isso com o filtro [`safe`](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#safe) (adicionando `|safe` após o nome da variável que você está substituindo).

<details><summary>Usando o CS50 Codespace?</summary><p>Se estiver usando o CS50 Codespace e encontrar a mensagem de erro de verificação de origem de CSRF 403 ao tentar enviar um formulário, você precisará atualizar o arquivo de configurações do seu projeto <code class="language-plaintext highlighter-rouge">settings.py</code> para adicionar a seguinte linha:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>CSRF_TRUSTED_ORIGINS = ['https://CODESPACE-URL-8000.preview.app.github.dev']
</code></pre></div></div>
<p>substituindo <code class="language-plaintext highlighter-rouge">CODESPACE-URL</code> pela URL real que você vê na barra do seu navegador ao executar o Codespace.</p></details>

## Como Enviar

1.  Visite [este link](https://submit.cs50.io/invites/89679428401548238ceb022f141b9947), faça login com sua conta do GitHub e clique em **Autorizar cs50**. Em seguida, marque a caixa indicando que você gostaria de conceder acesso dos funcionários do curso às suas submissões e clique em **Participar do curso**.
2.  [Instale o Git](https://git-scm.com/downloads) e, opcionalmente, [instale o `submit50`](https://cs50.readthedocs.io/submit50/).

<div class="alert alert-success" data-alert="success" role="alert"><p>Ao enviar seu projeto, o conteúdo do seu ramo <code class="language-plaintext highlighter-rouge">web50/projects/2020/x/wiki</code> deve corresponder à estrutura de arquivos do código de distribuição descompactado conforme originalmente recebido. Ou seja, seus arquivos não devem estar aninhados dentro de nenhum outro diretório de sua própria criação. Seu ramo também não deve conter qualquer código de outros projetos, apenas deste. Não seguir essa estrutura de arquivos provavelmente resultará na rejeição de sua submissão.</p>

<p>Por exemplo, para este projeto, isso significa que se a equipe de avaliação visitar <code class="language-plaintext highlighter-rouge">https://github.com/me50/USERNAME/tree/web50/projects/2020/x/wiki</code> (onde <code class="language-plaintext highlighter-rouge">USERNAME</code> é seu nome de usuário do GitHub conforme fornecido no formulário abaixo), deveríamos ver os três subdiretórios (<code class="language-plaintext highlighter-rouge">encyclopedia</code>, <code class="language-plaintext highlighter-rouge">entries</code>, <code class="language-plaintext highlighter-rouge">wiki</code>) e o arquivo <code class="language-plaintext highlighter-rouge">manage.py</code>. Se o seu código não estiver organizado desta forma quando você verificar, reorganize seu repositório conforme necessário para corresponder a esse paradigma.</p></div>

3.  Se você instalou o `submit50`, execute

        submit50 web50/projects/2020/x/wiki

    Caso contrário, usando o Git, envie seu trabalho para `https://github.com/me50/USERNAME.git`, onde `USERNAME` é seu nome de usuário do GitHub, em um ramo chamado `web50/projects/2020/x/wiki`.

4.  [Grave um screencast](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) com duração máxima de 5 minutos (e não carregado há mais de um mês antes da sua submissão deste projeto), no qual você demonstra a funcionalidade do seu projeto. Certifique-se de que cada elemento da especificação acima esteja demonstrado em seu vídeo. Não é necessário mostrar seu código neste vídeo, apenas sua aplicação em ação; revisaremos seu código no GitHub. [Faça o upload desse vídeo para o YouTube](https://www.youtube.com/upload) (como não listado ou público, mas não privado) ou em outro lugar. Na descrição do seu vídeo, você deve colocar os timestamps onde seu vídeo demonstra cada um dos sete (7) elementos principais da especificação. **Isso não é opcional**, os vídeos sem timestamps em sua descrição serão automaticamente rejeitados.
5.  Envie [este formulário](https://forms.cs50.io/776c132a-0aac-43c5-9826-b958f245a7b6).

A seguir, acesse [https://cs50.me/cs50w](https://cs50.me/cs50w) para visualizar o seu progresso atual!
