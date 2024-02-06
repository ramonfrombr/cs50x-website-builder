# Pesquisa

<div class="alert" data-alert="warning" role="alert"><p>As Aulas 1 e 2 não são necessárias para concluir este projeto, mas podem ser úteis se estiver com dificuldades para <em>enviá-lo</em>, pois ensinam Git, entre outros tópicos!</p></div>

Desenvolva um front-end para Pesquisa do Google, Pesquisa de Imagens do Google e Pesquisa Avançada do Google.

## Contexto

Lembre-se da aula que podemos criar um formulário HTML usando uma tag `<form>` e adicionar tags `<input>` para criar campos de entrada para esse formulário. Mais tarde no curso, veremos como escrever aplicações web que podem aceitar dados do formulário como entrada. Para este projeto, escreveremos formulários que enviam dados para um servidor web existente: neste caso, o Google.

Quando você faz uma pesquisa no Google, como digitando uma consulta na página inicial do Google e clicando no botão "Pesquisa Google", como essa consulta funciona? Vamos tentar descobrir.

Vá para [google.com](https://www.google.com/), digite uma consulta como “Harvard” no campo de pesquisa e clique no botão “Pesquisa Google”.

Como provavelmente esperava, você deve ver os resultados da pesquisa do Google para “Harvard”. Mas agora, dê uma olhada na URL. Deve começar com `https://www.google.com/search`, a rota no site do Google que permite a pesquisa. Mas após a rota há um `?`, seguido de algumas informações adicionais.

Esses elementos adicionais na URL são conhecidos como uma string de consulta. A string de consulta consiste em uma sequência de parâmetros GET, em que cada parâmetro tem um nome e um valor. As strings de consulta geralmente são formatadas como

    campo1=valor1&campo2=valor2&campo3=valor3...

onde um `=` separa o nome do parâmetro de seu valor, e o símbolo `&` separa os parâmetros uns dos outros. Esses parâmetros são uma maneira para os formulários enviarem informações para um servidor web, codificando os dados do formulário na URL.

Dê uma olhada na URL da página de resultados da sua pesquisa no Google. Parece que o Google está utilizando muitos parâmetros. Dê uma olhada na URL (pode ser útil copiar/colar em um editor de texto) e veja se consegue encontrar alguma menção a “Harvard”, nossa consulta.

Se você olhar a URL, deve ver que um dos parâmetros GET na URL é `q=Harvard`. Isso sugere que o nome do parâmetro correspondente a uma pesquisa no Google é `q` (provavelmente uma abreviação de “query”).

Acontece que, enquanto os outros parâmetros fornecem dados úteis ao Google, somente o parâmetro `q` é necessário para realizar uma pesquisa. Você pode testar isso visitando `https://www.google.com/search?q=Harvard`, excluindo todos os outros parâmetros. Você deverá ver os mesmos resultados do Google!

Usando essa informação, na verdade podemos recriar um front end para a página inicial do Google. Cole o código abaixo em um arquivo HTML chamado `index.html` e abra no navegador. Você também pode baixar o arquivo `index.html` diretamente na seção “Primeiros Passos” abaixo.

    <!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <title>Pesquisa</title>
        </head>
        <body>
            <form action="https://www.google.com/search">
                <input type="text" name="q">
                <input type="submit" value="Pesquisa Google">
            </form>
        </body>
    </html>

Quando você abrir essa página no navegador, deverá ver um formulário HTML (bem simples). Digite uma consulta de pesquisa como “Harvard” e clique em “Pesquisa Google” e você será levado para a página de resultados da pesquisa do Google!

Como isso funcionou? Neste caso, o atributo `action` no `form` informou ao navegador que quando o formulário for enviado, os dados devem ser enviados para `https://www.google.com/search`. E adicionando um campo `input` ao formulário cujo atributo `name` era `q`, o que quer que o usuário digite naquele campo de entrada é incluído como um parâmetro GET na URL.

Sua tarefa neste projeto é expandir este site, criando seu próprio front-end para Pesquisa Google, explorando a interface do Google para identificar quais parâmetros GET ela espera e adicionando o HTML e CSS necessários ao seu site.

## Primeiros Passos

- Baixe o código de distribuição em [https://cdn.cs50.net/web/2020/spring/projects/0/search.zip](https://cdn.cs50.net/web/2020/spring/projects/0/search.zip) e descompacte-o. Você pode pular este passo se criou manualmente o arquivo `index.html` seguindo as instruções da seção "Contexto" acima.

## Especificação

Seu site deve atender aos seguintes requisitos:

- Seu site deve ter pelo menos três páginas: uma para a Pesquisa regular do Google (que deve ser chamada `index.html`), uma para a Pesquisa de Imagens do Google e uma para a Pesquisa Avançada do Google.
  - Na página de Pesquisa Google, deve haver links no canto superior direito da página para ir para a Pesquisa de Imagens ou Pesquisa Avançada. Em cada uma das outras duas páginas, deve haver um link no canto superior direito para voltar para a Pesquisa Google.
- Na página de Pesquisa Google, o usuário deve ser capaz de digitar uma consulta, clicar em "Pesquisa Google" e ser levado para os resultados da pesquisa do Google para essa consulta.
  - Assim como no Google, sua barra de pesquisa deve estar centralizada com cantos arredondados. O botão de pesquisa também deve estar centralizado e abaixo da barra de pesquisa.
- Na página de Pesquisa de Imagens do Google, o usuário deve ser capaz de digitar uma consulta, clicar em um botão de pesquisa e ser levado para os resultados da pesquisa de imagens do Google para essa consulta.
- Na página de Pesquisa Avançada do Google, o usuário deve ser capaz de fornecer entrada para os seguintes quatro campos (extraídos das opções da própria [pesquisa avançada do Google](https://www.google.com/advanced_search)):
  - Encontrar páginas com… “todas essas palavras:”
  - Encontrar páginas com… “esta palavra ou frase exata:”
  - Encontrar páginas com… “alguma(s) das palavras:”
  - Encontrar páginas com… “nenhuma(s) das palavras:”
- Assim como na própria página de Pesquisa Avançada do Google, as quatro opções devem ser empilhadas verticalmente, e todos os campos de texto devem estar alinhados à esquerda.
  - Conforme o CSS do próprio Google, o botão “Pesquisa Avançada” deve ser azul com texto branco.
  - Quando o botão “Pesquisa Avançada” é clicado, o usuário deve ser levado para a página de resultados da pesquisa para a consulta fornecida.
- Adicione um botão “Estou com sorte” à página principal de Pesquisa do Google. Conforme o comportamento do próprio Google, ao clicar neste link, os usuários devem ser levados diretamente para o primeiro resultado da pesquisa do Google para a consulta, ignorando a página de resultados normais.
  - Você pode encontrar um aviso de redirecionamento ao usar o botão “Estou com sorte”. Não se preocupe! Isso é uma consequência esperada de uma funcionalidade de segurança implementada pelo Google.
- O CSS que você escrever deve se assemelhar à estética do próprio Google.

## Dicas

- Para determinar quais devem ser os nomes dos parâmetros, você pode experimentar fazendo pesquisas no Google e olhando a URL resultante. Também pode ser útil abrir o inspetor de "Rede" (acessível no Google Chrome escolhendo Visualizar -> Desenvolvedor -> Ferramentas de Desenvolvedor) para visualizar detalhes sobre as solicitações que o seu navegador faz ao Google.
  - Qualquer elemento `<input>` (seja do tipo `text`, `submit`, `number` ou outro tipo) pode ter atributos `name` e `value` que se tornarão parâmetros GET quando um formulário for enviado.
  - Também pode ser útil olhar o HTML do próprio Google para responder essas perguntas. Na maioria dos navegadores, você pode clicar com o botão direito em uma página e escolher “Visualizar Código-fonte da Página” para ver o HTML subjacente da página.
- Para incluir um campo de entrada em um formulário que os usuários não podem ver ou modificar, você pode usar um campo de entrada [“hidden”](https://www.w3schools.com/tags/att_input_type_hidden.asp).

## Como Enviar

1.  Acesse [este link](https://submit.cs50.io/invites/89679428401548238ceb022f141b9947), faça login com sua conta do GitHub e clique em **Autorizar cs50**. Em seguida, marque a caixa indicando que deseja conceder acesso da equipe do curso às suas submissões e clique em **Participar do curso**.
2.  [Instale o Git](https://git-scm.com/downloads) e, opcionalmente, [instale o `submit50`](https://cs50.readthedocs.io/submit50/).

<div class="alert" data-alert="success" role="alert"><p>Ao enviar seu projeto, o conteúdo do seu branch <code class="language-plaintext highlighter-rouge">web50/projects/2020/x/search</code> deve corresponder à estrutura de arquivos do código de distribuição descompactado originalmente recebido. Ou seja, seus arquivos não devem estar aninhados dentro de quaisquer outros diretórios de sua própria criação (<code class="language-plaintext highlighter-rouge">search</code> ou <code class="language-plaintext highlighter-rouge">project0</code>, por exemplo). Seu branch também não deve conter código de quaisquer outros projetos, apenas deste. O não cumprimento desta estrutura de arquivos provavelmente resultará na rejeição da sua submissão.</p>
<p>Por exemplo, para este projeto, isso significa que se a equipe de avaliação acessar <code class="language-plaintext highlighter-rouge">https://github.com/me50/USERNAME/blob/web50/projects/2020/x/search/index.html</code> (onde <code class="language-plaintext highlighter-rouge">USERNAME</code> é seu nome de usuário do GitHub fornecido no formulário abaixo), sua submissão para o <code class="language-plaintext highlighter-rouge">index.html</code> deste projeto deve ser o que aparece. Se não for, reorganize seu repositório conforme necessário para corresponder a esse paradigma.</p></div>

3.  Se você instalou o `submit50`, execute

        submit50 web50/projects/2020/x/search

    Caso contrário, usando o Git, envie seu trabalho para `https://github.com/me50/USERNAME.git`, onde `USERNAME` é seu nome de usuário do GitHub, em um branch chamado `web50/projects/2020/x/search`.

4.  [Registre um screencast](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) com duração máxima de 5 minutos (e não carregado há mais de um mês antes da submissão deste projeto), no qual você demonstra a funcionalidade do seu projeto. **A barra de URL deve permanecer visível durante toda a demonstração do projeto.** Certifique-se de que cada elemento da especificação acima seja demonstrado em seu vídeo. Não é necessário mostrar seu código neste vídeo, apenas sua aplicação em ação; revisaremos seu código no GitHub. [Carregue este vídeo no YouTube](https://www.youtube.com/upload) (como não listado ou público, mas não privado) ou em outro local. Na descrição do seu vídeo, você deve adicionar timestamps para indicar onde seu vídeo demonstra cada um dos sete (7) elementos da especificação. **Isso não é opcional**, vídeos sem timestamps na descrição serão automaticamente rejeitados.
5.  Envie [este formulário](https://forms.cs50.io/e066493e-47d7-4586-b818-4d44a87553e5).

Você pode então acessar [https://cs50.me/cs50w](https://cs50.me/cs50w) para ver o andamento atual!
