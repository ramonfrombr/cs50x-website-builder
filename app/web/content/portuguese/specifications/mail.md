# Correio

<div class="alert alert-warning" data-alert="warning" role="alert"><p>O CS50W não possui uma correspondência direta entre aulas e projetos. Se você está tentando fazer este projeto sem ter assistido pelo menos a Aula 5, você está tentando fazer isso cedo demais!</p></div>

Desenhe um front-end para um cliente de e-mail que faz chamadas de API para enviar e receber e-mails.

![Página de Caixa de Entrada](https://cs50.harvard.edu/web/2020/projects/3/images/inbox.png)

![Página de E-mail](https://cs50.harvard.edu/web/2020/projects/3/images/email.png)

## Começando

1.  Baixe o código de distribuição em [https://cdn.cs50.net/web/2020/spring/projects/3/mail.zip](https://cdn.cs50.net/web/2020/spring/projects/3/mail.zip) e descompacte-o.
2.  No seu terminal, use o comando `cd` para entrar no diretório `mail`.
3.  Execute `python manage.py makemigrations mail` para gerar as migrações para o aplicativo `mail`.
4.  Execute `python manage.py migrate` para aplicar as migrações ao seu banco de dados.

## Entendendo

No código de distribuição há um projeto Django chamado `project3` que contém um único aplicativo chamado `mail`.

Primeiro, após fazer e aplicar as migrações para o projeto, execute `python manage.py runserver` para iniciar o servidor web. Abra o servidor web no seu navegador e use o link "Register" para se registrar para uma nova conta. Os e-mails que você enviar e receber neste projeto serão armazenados inteiramente em seu banco de dados (eles não serão realmente enviados para servidores de e-mail reais), então você pode escolher qualquer endereço de e-mail (por exemplo, `foo@example.com`) e senha que desejar para este projeto, as credenciais não precisam ser válidas para endereços de e-mail reais.

Depois de se inscrever, você deverá ser redirecionado para a página da Caixa de Entrada do cliente de e-mail, embora esta página esteja principalmente em branco (por enquanto). Clique nos botões para navegar para suas Caixas de Saída e Arquivadas e note como também estão vazias no momento. Clique no botão "Compor" e você será levado a um formulário que permitirá compor um novo e-mail. Cada vez que você clicar em um botão, porém, você não será levado a uma nova rota ou a fazer uma nova solicitação web: na verdade, toda essa aplicação é apenas uma única página, com JavaScript usado para controlar a interface do usuário. Vamos dar uma olhada mais de perto no código de distribuição para ver como isso funciona.

Dê uma olhada em `mail/urls.py` e observe que a rota padrão carrega uma função `index` em `views.py`. Então vamos abrir `views.py` e olhar para a função `index`. Observe que, enquanto o usuário estiver logado, esta função renderiza o modelo `mail/inbox.html`. Vamos olhar para esse modelo, armazenado em `mail/templates/mail/inbox.html`. Você notará que no corpo da página, o endereço de e-mail do usuário é exibido primeiro em um elemento `h2`. Depois disso, a página tem uma sequência de botões para navegar entre várias páginas do aplicativo. Abaixo disso, note que esta página tem duas seções principais, cada uma definida por um elemento `div`. O primeiro (com um `id` de `emails-view`) contém o conteúdo de uma caixa de e-mail (inicialmente vazio). O segundo (com um `id` de `compose-view`) contém um formulário onde o usuário pode compor um novo e-mail. Os botões ao longo do topo, então, precisam mostrar e esconder seletivamente essas visualizações: o botão de composição, por exemplo, deve esconder o `emails-view` e mostrar o `compose-view`; enquanto o botão de Caixa de Entrada, por sua vez, deve esconder o `compose-view` e mostrar o `emails-view`.

Como eles fazem isso? Observe que no final de `inbox.html`, o arquivo JavaScript `mail/inbox.js` está incluído. Abra esse arquivo, armazenado em `mail/static/mail/inbox.js`, e dê uma olhada. Observe que, quando o conteúdo do DOM da página é carregado, anexamos ouvintes de eventos a cada um dos botões. Quando o botão `inbox`, por exemplo, é clicado, chamamos a função `load_mailbox` com o argumento `'inbox'; quando o botão `compose`é clicado, por outro lado, chamamos a função`compose_email`. O que essas funções fazem? A função `compose_email`primeiro esconde o`emails-view`(definindo sua propriedade`style.display`para`none`) e mostra o `compose-view`(definindo sua propriedade`style.display`para`block`). Depois disso, a função pega todos os campos de entrada do formulário (onde o usuário pode digitar um endereço de e-mail do destinatário, assunto e corpo do e-mail) e define seus valores para a string vazia `''` para limpá-los. Isso significa que toda vez que clicar no botão "Compor", você deverá ser apresentado com um formulário de e-mail em branco: você pode testar isso digitando valores no formulário, mudando a visualização para a Caixa de Entrada e depois voltar à visualização de Compor.

Enquanto isso, a função `load_mailbox` primeiro mostra o `emails-view` e esconde o `compose-view`. A função `load_mailbox` também recebe um argumento, que será o nome da caixa de correio que o usuário está tentando visualizar. Para este projeto, você projetará um cliente de e-mail com três caixas de correio: uma caixa de entrada, uma caixa de saída com todos os e-mails enviados e um arquivo de e-mails que estavam uma vez na caixa de entrada mas foram arquivados desde então. O argumento para `load_mailbox`, então, será um desses três valores, e a função `load_mailbox` exibe o nome da caixa de correio selecionada atualizando o `innerHTML` do `emails-view` (após a capitalização do primeiro caracter). É por isso que, quando você escolhe um nome de caixa de correio no navegador, vê o nome dessa caixa de correio (capitalizado) aparecer no DOM: a função `load_mailbox` está atualizando o `emails-view` para incluir o texto apropriado.

É claro que essa aplicação está incompleta. Todas as caixas de correio mostram apenas o nome da caixa de correio (Caixa de Entrada, Enviados, Arquivados) mas na verdade não mostram nenhum e-mail ainda. Ainda não há uma visualização para visualizar o conteúdo de nenhum e-mail. E o formulário de composição permitirá que você digite o conteúdo de um e-mail, mas o botão para enviar o e-mail na verdade não faz nada. É aí que você entra!

### API

Você recebe, envia e atualiza e-mails usando a API desta aplicação. Nós escrevemos a API inteira para você (e documentamos abaixo), para que você possa usá-la em seu código JavaScript. (De fato, observe que escrevemos **todo** o código Python para você neste projeto. Você deve ser capaz de completar este projeto apenas escrevendo HTML e JavaScript).

Esta aplicação suporta as seguintes rotas de API:

#### `GET /emails/<str:mailbox>`

Enviando uma solicitação `GET` para `/emails/<caixa-de-entrada>` onde `<caixa-de-entrada>` é `inbox`, `sent` ou `archive` retornará para você (em forma JSON) uma lista de todos os e-mails nessa caixa, em ordem cronológica reversa. Por exemplo, se você enviar uma solicitação `GET` para `/emails/inbox`, você pode obter uma resposta JSON como abaixo (representando dois e-mails):

    [
        {
            "id": 100,
            "sender": "foo@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Olá!",
            "body": "Olá, mundo!",
            "timestamp": "2 Jan 2020, 00:00",
            "read": false,
            "archived": false
        },
        {
            "id": 95,
            "sender": "baz@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Reunião Amanhã",
            "body": "A que horas nos encontramos?",
            "timestamp": "2 Jan 2020, 00:00",
            "read": true,
            "archived": false
        }
    ]

Observe que cada e-mail inclui seu `id` (um identificador único), um endereço de e-mail do `remetente`, um array de `destinatários`, uma string para `assunto`, `corpo` e `timestamp`, bem como dois valores booleanos indicando se o e-mail foi “lido” e se o e-mail foi “arquivado”.

Como obter acesso a esses valores em JavaScript? Lembre-se que em JavaScript você pode usar `fetch` para fazer uma solicitação web. Portanto, o código JavaScript a seguir:

    fetch('/emails/inbox')
    .then(response => response.json())
    .then(emails => {
        // Exibir e-mails
        console.log(emails);

        // ... faça algo mais com os e-mails ...
    });

fará uma solicitação `GET` para `/emails/inbox`, converterá a resposta resultante em JSON e então fornecerá a você o array de e-mails dentro da variável `emails`. Você pode imprimir esse valor no console do navegador usando `console.log` (se você não tiver nenhum e-mail em sua caixa de entrada, isso será um array vazio), ou fazer algo mais com esse array.

Note também que se você solicitar uma caixa de correio inválida (qualquer coisa que não seja `inbox`, `sent` ou `archive`), você receberá a resposta JSON `{"error": "Caixa de correio inválida."}`.

#### `GET /emails/<int:id_do_email>`

Enviando uma solicitação `GET` para `/emails/id_do_email` onde `id_do_email` é um ID inteiro para um e-mail, retornará uma representação JSON do e-mail, como abaixo:

    {
            "id": 100,
            "sender": "foo@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Olá!",
            "body": "Olá, mundo!",
            "timestamp": "2 Jan 2020, 00:00",
            "read": false,
            "archived": false
    }

Observe que se o e-mail não existe, ou se o usuário não tem acesso ao e-mail, a rota em vez disso retornará um erro 404 Not Found com uma resposta JSON `{"error": "E-mail não encontrado."}`.

Para obter o e-mail de número 100, por exemplo, você pode escrever código JavaScript como:

    fetch('/emails/100')
    .then(response => response.json())
    .then(email => {
        // Exibir e-mail
        console.log(email);

        // ... faça algo mais com o e-mail ...
    });

#### `POST /emails`

Até agora, vimos como obter e-mails: todos os e-mails em uma caixa de correio, ou apenas um único e-mail. Para enviar um e-mail, você pode enviar uma solicitação `POST` para a rota `/emails`. A rota requer que três dados sejam enviados: um valor `destinatários` (uma string separada por vírgula de todos os usuários para enviar um e-mail), uma string `assunto` e uma string de `corpo`. Por exemplo, você poderia escrever código JavaScript como:

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: 'baz@example.com',
          subject: 'Hora da Reunião',
          body: 'Que tal nos encontrarmos amanhã às 15h?'
      })
    })
    .then(response => response.json())
    .then(result => {
        // Exibir resultado
        console.log(result);
    });

Se o e-mail for enviado com sucesso, a rota responderá com um código de status 201 e uma resposta JSON de `{"message": "E-mail enviado com sucesso."}`.

Observe que deve haver pelo menos um destinatário de e-mail: se um não for fornecido, a rota responderá com um código de status 400 e uma resposta JSON de `{"error": "Pelo menos um destinatário é necessário."}`. Todos os destinatários também devem ser usuários válidos que se registraram neste aplicativo web específico: se você tentar enviar um e-mail para `baz@example.com` mas não houver nenhum usuário com esse endereço de e-mail, você receberá uma resposta JSON de `{"error": "Usuário com o e-mail baz@example.com não existe."}`.

#### `PUT /emails/<int:id_do_email>`

A rota final que você precisará é a capacidade de marcar um e-mail como lido/não lido ou como arquivado/não arquivado. Para fazer isso, envie uma solicitação `PUT` (em vez de uma solicitação `GET`) para `/emails/id_do_email` onde `id_do_email` é o ID do e-mail que você está tentando modificar. Por exemplo, o código JavaScript a seguir:

    fetch('/emails/100', {
      method: 'PUT',
      body: JSON.stringify({
          archived: true
      })
    })

marcaria o e-mail número 100 como arquivado. O corpo da solicitação `PUT` também pode ser `{archived: false}` para desarquivar a mensagem, e também poderia ser `{read: true}` ou `{read: false}` para marcar o e-mail como lido ou não lido, respectivamente.

Usando essas quatro rotas de API (obtendo todos os e-mails em uma caixa de correio, obtendo um único e-mail, enviando um e-mail e atualizando um e-mail existente), você deve ter todas as ferramentas que você precisa agora para completar este projeto!

## Especificação

Usando JavaScript, HTML e CSS, complete a implementação do seu cliente de e-mail de página única dentro do arquivo `inbox.js` (e não em arquivos adicionais ou outros; para fins de avaliação, só iremos considerar o `inbox.js`!). Você deve cumprir os seguintes requisitos:

-   **Enviar E-mail**: Quando um usuário envia o formulário de composição de e-mail, adicione código JavaScript para realmente enviar o e-mail.
    -   Provavelmente você vai querer fazer uma requisição `POST` para `/emails`, passando valores para `recipients`, `subject` e `body`.
    -   Após o envio do e-mail, carregue a caixa de saída do usuário.
-   **Caixa de Correio**: Quando um usuário visita sua Caixa de Entrada, Caixa de Saída ou Arquivo, carregue a caixa apropriada.
    -   Provavelmente você vai querer fazer uma requisição `GET` para `/emails/<caixa>` para solicitar os e-mails de uma caixa específica.
    -   Quando uma caixa de e-mail é visitada, a aplicação deve consultar a API para os e-mails mais recentes naquela caixa.
    -   Quando uma caixa de e-mail é visitada, o nome da caixa de e-mail deve aparecer no topo da página (esta parte já está feita para você).
    -   Cada e-mail deve então ser renderizado em sua própria caixa (por exemplo, como um `<div>` com uma borda) que exibe de quem é o e-mail, qual é o assunto e o timestamp do e-mail.
    -   Se o e-mail estiver não lido, ele deve aparecer com fundo branco. Se o e-mail foi lido, ele deve aparecer com fundo cinza.
-   **Visualizar E-mail**: Quando um usuário clica em um e-mail, o usuário deve ser levado para uma visualização onde ele vê o conteúdo desse e-mail.
    -   Provavelmente você vai querer fazer uma requisição `GET` para `/emails/<id_do_email>` para solicitar o e-mail.
    -   Sua aplicação deve mostrar o remetente do e-mail, destinatários, assunto, timestamp e corpo do e-mail.
    -   Você provavelmente vai querer adicionar um novo `div` ao `inbox.html` (além de `emails-view` e `compose-view`) para exibir o e-mail. Certifique-se de atualizar seu código para ocultar e exibir as visualizações corretas quando as opções de navegação são clicadas.
    -   Veja a dica na seção Dicas sobre como adicionar um ouvinte de eventos a um elemento HTML que você adicionou ao DOM.
    -   Uma vez que o e-mail tenha sido clicado, você deve marcá-lo como lido. Lembre-se de que você pode enviar uma requisição `PUT` para `/emails/<id_do_email>` para atualizar se um e-mail foi lido ou não.
-   **Arquivar e Desarquivar**: Permitir que os usuários arquivem e desarquivem e-mails que eles receberam.
    -   Ao visualizar um e-mail na Caixa de Entrada, o usuário deve ser apresentado com um botão que permite arquivar o e-mail. Ao visualizar um e-mail no Arquivo, o usuário deve ser apresentado com um botão que permite desarquivar o e-mail. Este requisito não se aplica aos e-mails na Caixa de Saída.
    -   Lembre-se de que você pode enviar uma requisição `PUT` para `/emails/<id_do_email>` para marcar um e-mail como arquivado ou desarquivado.
    -   Depois que um e-mail for arquivado ou desarquivado, carregue a caixa de entrada do usuário.
-   **Responder**: Permitir que os usuários respondam a um e-mail.
    -   Ao visualizar um e-mail, o usuário deve ser apresentado com um botão "Responder" que permite responder ao e-mail.
    -   Quando o usuário clica no botão "Responder", ele deve ser levado para o formulário de composição do e-mail.
    -   Preencha o formulário de composição com o campo `destinatário` definido como quem enviou o e-mail original.
    -   Preencha a linha do `assunto`. Se o e-mail original tiver um assunto de `foo`, a nova linha de assunto deve ser `Re: foo`. (Se a linha de assunto já começar com `Re:`, não é necessário adicionar novamente.)
    -   Preencha o `corpo` do e-mail com uma linha como `"Em 1 de janeiro de 2020, 12:00 AM foo@example.com escreveu:"` seguido pelo texto original do e-mail.

## Dicas

-   Para criar um elemento HTML e adicionar um manipulador de eventos a ele, você pode usar código JavaScript como o abaixo:

```
const element = document.createElement('div');
element.innerHTML = 'Este é o conteúdo do div.';
element.addEventListener('click', function() {
    console.log('Este elemento foi clicado!')
});
document.querySelector('#container').append(element);
```

Este código cria um novo elemento `div`, define seu `innerHTML`, adiciona um manipulador de eventos para executar uma função específica quando esse `div` é clicado, e então o adiciona a um elemento HTML cujo `id` é `container` (este código assume que existe um elemento HTML cujo `id` é `container`: provavelmente você vai querer mudar o argumento do `querySelector` para ser o elemento ao qual deseja adicionar um elemento).

-   Pode ser útil editar o arquivo `mail/static/mail/styles.css` para adicionar qualquer CSS necessário para a aplicação.
-   Lembre-se de que se você tiver um array em JavaScript, você pode percorrer cada elemento desse array utilizando [`forEach`](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach).
-   Lembre-se que normalmente, para requisições `POST` e `PUT`, o Django requer um token CSRF para se proteger contra possíveis ataques de falsificação de solicitação entre sites. Para este projeto, intencionalmente tornamos as rotas da API isentas de CSRF, portanto você não precisará de um token. Entretanto, em um projeto do mundo real, é sempre melhor se prevenir contra essas possíveis vulnerabilidades!

## Como Enviar

1. Acesse [este link](https://submit.cs50.io/invites/89679428401548238ceb022f141b9947), faça login com sua conta do GitHub e clique em **Authorize cs50**. Em seguida, marque a caixa indicando que você deseja conceder acesso da equipe do curso às suas submissões e clique em **Join course**.
2. [Instale o Git](https://git-scm.com/downloads) e, opcionalmente, [instale o `submit50`](https://cs50.readthedocs.io/submit50/).

<div class="alert alert-success" data-alert="success" role="alert"><p>Ao enviar seu projeto, o conteúdo do seu branch <code class="language-plaintext highlighter-rouge">web50/projects/2020/x/mail</code> deve corresponder à estrutura de arquivos do código distribuído descompactado como originalmente recebido. Ou seja, seus arquivos não devem estar aninhados dentro de nenhum outro diretório de sua própria criação. Seu branch também não deve conter código de outros projetos, apenas deste. O não cumprimento dessa estrutura de arquivos provavelmente resultará na rejeição da sua submissão.</p>

<p>A título de exemplo, para este projeto significa que se a equipe de avaliação visitar <code class="language-plaintext highlighter-rouge">https://github.com/me50/USERNAME/tree/web50/projects/2020/x/mail</code> (onde <code class="language-plaintext highlighter-rouge">USERNAME</code> é seu nome de usuário do GitHub conforme fornecido no formulário abaixo), deveríamos ver os dois subdiretórios (<code class="language-plaintext highlighter-rouge">mail</code>, <code class="language-plaintext highlighter-rouge">project3</code>) e o arquivo <code class="language-plaintext highlighter-rouge">manage.py</code>. Se o seu código não estiver organizado assim quando você verificar, reorganize seu repositório conforme necessário para combinar com esse paradigma.</p></div>

3.  Se você instalou o `submit50`, execute

        submit50 web50/projects/2020/x/mail

    Caso contrário, usando o Git, envie seu trabalho para `https://github.com/me50/USERNAME.git`, onde `USERNAME` é seu nome de usuário do GitHub, em um branch chamado `web50/projects/2020/x/mail`.

4.  [Grave um screencast](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) com no máximo 5 minutos de duração (não pode ser carregado mais de um mês antes da submissão deste projeto), no qual você demonstra a funcionalidade do seu projeto. Certifique-se de que cada elemento da especificação, acima, seja demonstrado em seu vídeo. Não é necessário mostrar seu código neste vídeo, apenas sua aplicação em ação; revisaremos seu código no GitHub. [Faça o upload desse vídeo para o YouTube](https://www.youtube.com/upload) (como não listado ou público, mas não privado) ou em outro lugar. Na descrição do seu vídeo, você deve marcar o momento em que ele demonstra cada um dos cinco (5) elementos da especificação. **Isso não é opcional**, vídeos sem marcações na descrição serão automaticamente rejeitados.
5.  Envie [este formulário](https://forms.cs50.io/8f569b7d-bd6d-4446-82ac-d65b86d95bbb).

Depois, você pode ir para [https://cs50.me/cs50w](https://cs50.me/cs50w) para ver seu progresso atual!
