

## Especificação

Usando JavaScript, HTML e CSS, complete a implementação do seu cliente de e-mail de página única dentro do arquivo `inbox.js` (e não em arquivos adicionais ou outros; para fins de avaliação, só iremos considerar o `inbox.js`!). Você deve cumprir os seguintes requisitos:

- **Enviar E-mail**: Quando um usuário envia o formulário de composição de e-mail, adicione código JavaScript para realmente enviar o e-mail.
  - Provavelmente você vai querer fazer uma requisição `POST` para `/emails`, passando valores para `recipients`, `subject` e `body`.
  - Após o envio do e-mail, carregue a caixa de saída do usuário.
- **Caixa de Correio**: Quando um usuário visita sua Caixa de Entrada, Caixa de Saída ou Arquivo, carregue a caixa apropriada.
  - Provavelmente você vai querer fazer uma requisição `GET` para `/emails/<caixa>` para solicitar os e-mails de uma caixa específica.
  - Quando uma caixa de e-mail é visitada, a aplicação deve consultar a API para os e-mails mais recentes naquela caixa.
  - Quando uma caixa de e-mail é visitada, o nome da caixa de e-mail deve aparecer no topo da página (esta parte já está feita para você).
  - Cada e-mail deve então ser renderizado em sua própria caixa (por exemplo, como um `<div>` com uma borda) que exibe de quem é o e-mail, qual é o assunto e o timestamp do e-mail.
  - Se o e-mail estiver não lido, ele deve aparecer com fundo branco. Se o e-mail foi lido, ele deve aparecer com fundo cinza.
- **Visualizar E-mail**: Quando um usuário clica em um e-mail, o usuário deve ser levado para uma visualização onde ele vê o conteúdo desse e-mail.
  - Provavelmente você vai querer fazer uma requisição `GET` para `/emails/<id_do_email>` para solicitar o e-mail.
  - Sua aplicação deve mostrar o remetente do e-mail, destinatários, assunto, timestamp e corpo do e-mail.
  - Você provavelmente vai querer adicionar um novo `div` ao `inbox.html` (além de `emails-view` e `compose-view`) para exibir o e-mail. Certifique-se de atualizar seu código para ocultar e exibir as visualizações corretas quando as opções de navegação são clicadas.
  - Veja a dica na seção Dicas sobre como adicionar um ouvinte de eventos a um elemento HTML que você adicionou ao DOM.
  - Uma vez que o e-mail tenha sido clicado, você deve marcá-lo como lido. Lembre-se de que você pode enviar uma requisição `PUT` para `/emails/<id_do_email>` para atualizar se um e-mail foi lido ou não.
- **Arquivar e Desarquivar**: Permitir que os usuários arquivem e desarquivem e-mails que eles receberam.
  - Ao visualizar um e-mail na Caixa de Entrada, o usuário deve ser apresentado com um botão que permite arquivar o e-mail. Ao visualizar um e-mail no Arquivo, o usuário deve ser apresentado com um botão que permite desarquivar o e-mail. Este requisito não se aplica aos e-mails na Caixa de Saída.
  - Lembre-se de que você pode enviar uma requisição `PUT` para `/emails/<id_do_email>` para marcar um e-mail como arquivado ou desarquivado.
  - Depois que um e-mail for arquivado ou desarquivado, carregue a caixa de entrada do usuário.
- **Responder**: Permitir que os usuários respondam a um e-mail.
  - Ao visualizar um e-mail, o usuário deve ser apresentado com um botão "Responder" que permite responder ao e-mail.
  - Quando o usuário clica no botão "Responder", ele deve ser levado para o formulário de composição do e-mail.
  - Preencha o formulário de composição com o campo `destinatário` definido como quem enviou o e-mail original.
  - Preencha a linha do `assunto`. Se o e-mail original tiver um assunto de `foo`, a nova linha de assunto deve ser `Re: foo`. (Se a linha de assunto já começar com `Re:`, não é necessário adicionar novamente.)
  - Preencha o `corpo` do e-mail com uma linha como `"Em 1 de janeiro de 2020, 12:00 AM foo@example.com escreveu:"` seguido pelo texto original do e-mail.

## Dicas

- Para criar um elemento HTML e adicionar um manipulador de eventos a ele, você pode usar código JavaScript como o abaixo:

```
const element = document.createElement('div');
element.innerHTML = 'Este é o conteúdo do div.';
element.addEventListener('click', function() {
    console.log('Este elemento foi clicado!')
});
document.querySelector('#container').append(element);
```

Este código cria um novo elemento `div`, define seu `innerHTML`, adiciona um manipulador de eventos para executar uma função específica quando esse `div` é clicado, e então o adiciona a um elemento HTML cujo `id` é `container` (este código assume que existe um elemento HTML cujo `id` é `container`: provavelmente você vai querer mudar o argumento do `querySelector` para ser o elemento ao qual deseja adicionar um elemento).

- Pode ser útil editar o arquivo `mail/static/mail/styles.css` para adicionar qualquer CSS necessário para a aplicação.
- Lembre-se de que se você tiver um array em JavaScript, você pode percorrer cada elemento desse array utilizando [`forEach`](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach).
- Lembre-se que normalmente, para requisições `POST` e `PUT`, o Django requer um token CSRF para se proteger contra possíveis ataques de falsificação de solicitação entre sites. Para este projeto, intencionalmente tornamos as rotas da API isentas de CSRF, portanto você não precisará de um token. Entretanto, em um projeto do mundo real, é sempre melhor se prevenir contra essas possíveis vulnerabilidades!

## Como Enviar

1. Acesse [este link](https://submit.cs50.io/invites/89679428401548238ceb022f141b9947), faça login com sua conta do GitHub e clique em **Authorize cs50**. Em seguida, marque a caixa indicando que você deseja conceder acesso da equipe do curso às suas submissões e clique em **Join course**.
2. [Instale o Git](https://git-scm.com/downloads) e, opcionalmente, [instale o `submit50`](https://cs50.readthedocs.io/submit50/).

<div class="alert alert-success" data-alert="success" role="alert"><p>Ao enviar seu projeto, o conteúdo do seu branch <code class="language-plaintext highlighter-rouge">web50/projects/2020/x/mail</code> deve corresponder à estrutura de arquivos do código distribuído descompactado como originalmente recebido. Ou seja, seus arquivos não devem estar aninhados dentro de nenhum outro diretório de sua própria criação. Seu branch também não deve conter código de outros projetos, apenas deste. O não cumprimento dessa estrutura de arquivos provavelmente resultará na rejeição da sua submissão.</p>

<p>A título de exemplo, para este projeto significa que se a equipe de avaliação visitar <code class="language-plaintext highlighter-rouge">https://github.com/me50/USERNAME/tree/web50/projects/2020/x/mail</code> (onde <code class="language-plaintext highlighter-rouge">USERNAME</code> é seu nome de usuário do GitHub conforme fornecido no formulário abaixo), deveríamos ver os dois subdiretórios (<code class="language-plaintext highlighter-rouge">mail</code>, <code class="language-plaintext highlighter-rouge">project3</code>) e o arquivo <code class="language-plaintext highlighter-rouge">manage.py</code>. Se o seu código não estiver organizado assim quando você verificar, reorganize seu repositório conforme necessário para combinar com esse paradigma.</p></div>

3. Se você instalou o `submit50`, execute

        submit50 web50/projects/2020/x/mail

    Caso contrário, usando o Git, envie seu trabalho para `https://github.com/me50/USERNAME.git`, onde `USERNAME` é seu nome de usuário do GitHub, em um branch chamado `web50/projects/2020/x/mail`.

4. [Grave um screencast](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) com no máximo 5 minutos de duração (não pode ser carregado mais de um mês antes da submissão deste projeto), no qual você demonstra a funcionalidade do seu projeto. Certifique-se de que cada elemento da especificação, acima, seja demonstrado em seu vídeo. Não é necessário mostrar seu código neste vídeo, apenas sua aplicação em ação; revisaremos seu código no GitHub. [Faça o upload desse vídeo para o YouTube](https://www.youtube.com/upload) (como não listado ou público, mas não privado) ou em outro lugar. Na descrição do seu vídeo, você deve marcar o momento em que ele demonstra cada um dos cinco (5) elementos da especificação. **Isso não é opcional**, vídeos sem marcações na descrição serão automaticamente rejeitados.
5. Envie [este formulário](https://forms.cs50.io/8f569b7d-bd6d-4446-82ac-d65b86d95bbb).

Depois, você pode ir para [https://cs50.me/cs50w](https://cs50.me/cs50w) para ver seu progresso atual!