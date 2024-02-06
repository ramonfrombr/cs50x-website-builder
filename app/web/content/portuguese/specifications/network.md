# Rede

<div class="alert alert-warning" data-alert="warning" role="alert"><p>O CS50W não apresenta uma correspondência direta entre as palestras e os projetos. Se você está tentando realizar este projeto sem ter assistido pelo menos à Aula 7, está tentando fazer isso cedo demais!</p></div>

Projete um site de rede social semelhante ao Twitter para criar postagens e seguir usuários.

![Página da rede](https://cs50.harvard.edu/web/2020/projects/4/images/network.png)

## Começando

1. Baixe o código de distribuição em [https://cdn.cs50.net/web/2020/spring/projects/4/network.zip](https://cdn.cs50.net/web/2020/spring/projects/4/network.zip) e descompacte-o.
2. No seu terminal, entre no diretório `project4` com `cd`.
3. Execute `python manage.py makemigrations network` para criar as migrações para o aplicativo `network`.
4. Execute `python manage.py migrate` para aplicar as migrações ao seu banco de dados.

## Entendendo

No código de distribuição há um projeto Django chamado `project4` que contém um aplicativo chamado `network`, estruturado de forma semelhante ao aplicativo `leilões` do Projeto 2.

Primeiramente, abra `network/urls.py`, onde a configuração de URL para este aplicativo é definida. Observe que já escrevemos algumas URLs para você, incluindo uma rota de índice padrão, uma rota `/login`, uma rota `/logout` e uma rota `/register`.

Dê uma olhada em `network/views.py` para ver as visualizações associadas a cada uma dessas rotas. A visualização de índice por enquanto retorna um modelo `index.html` principalmente vazio. A visualização `login_view` renderiza um formulário de login quando um usuário tenta acessar a página com o método GET. Quando um usuário envia o formulário usando o método de solicitação POST, o usuário é autenticado, conectado e redirecionado para a página de índice. A visualização `logout_view` desconecta o usuário e o redireciona para a página de índice. Por fim, a rota `register` exibe um formulário de registro para o usuário e cria um novo usuário quando o formulário é enviado. Tudo isso é feito para você no código de distribuição, então você deve conseguir executar a aplicação agora para criar alguns usuários.

Execute `python manage.py runserver` para iniciar o servidor web Django e acesse o site no seu navegador. Clique em "Registrar" e registre uma conta. Você deve ver que agora está "Conectado como" sua conta de usuário, e os links no topo da página mudaram. Como o HTML mudou? Dê uma olhada em `network/templates/network/layout.html` para ver o layout HTML desta aplicação. Observe que várias partes do modelo são envoltas em uma verificação de se `user.is_authenticated`, para que diferentes conteúdos possam ser renderizados dependendo se o usuário está autenticado ou não. Fique à vontade para alterar este arquivo se quiser adicionar ou modificar algo no layout!

Por fim, examine `network/models.py`. Aqui é onde você irá definir os modelos para a sua aplicação web, onde cada modelo representa algum tipo de dado que você deseja armazenar no seu banco de dados. Nós começamos com um modelo `User` que representa cada usuário do aplicativo. Como ele herda de `AbstractUser`, ele já terá campos como nome de usuário, e-mail, senha, etc., mas você pode adicionar novos campos à classe `User` se houver informações adicionais sobre um usuário que deseja representar. Você também precisará adicionar modelos adicionais a este arquivo para representar detalhes sobre postagens, curtidas e seguidores. Lembre-se de que toda vez que você alterar algo em `network/models.py`, você precisará primeiro executar `python manage.py makemigrations` e depois `python manage.py migrate` para migrar essas alterações para o seu banco de dados.

## Especificação

Usando Python, JavaScript, HTML e CSS, complete a implementação de uma rede social que permita aos usuários criar postagens, seguir outros usuários e "curtir" postagens. Você deve cumprir os seguintes requisitos:

- **Nova Postagem**: Usuários conectados devem poder escrever uma nova postagem baseada em texto preenchendo um campo de texto e clicando em um botão para enviar a postagem.
  - A captura de tela no topo desta especificação mostra o campo "Nova Postagem" no topo da página "Todas as Postagens". Você pode optar em ter isso também, ou pode fazer a funcionalidade "Nova Postagem" em uma página separada.
- **Todas as Postagens**: O link "Todas as Postagens" na barra de navegação deve levar o usuário a uma página onde ele possa ver todas as postagens de todos os usuários, com as postagens mais recentes em primeiro lugar.
  - Cada postagem deve incluir o nome de usuário do autor, o conteúdo da postagem em si, a data e hora em que a postagem foi feita e o número de "curtidas" que a postagem tem (que será 0 para todas as postagens até você implementar a capacidade de "curtir" uma postagem posteriormente).
- **Página de Perfil**: Clicar em um nome de usuário deve carregar a página de perfil desse usuário. Esta página deve:
  - Exibir o número de seguidores que o usuário possui, bem como o número de pessoas que o usuário segue.
  - Exibir todas as postagens desse usuário, em ordem cronológica inversa.
  - Para qualquer outro usuário autenticado, esta página deve exibir um botão "Seguir" ou "Deixar de Seguir" que permitirá ao usuário atual alternar se está seguindo ou não as postagens desse usuário. Observe que isso se aplica apenas a qualquer usuário "outro": um usuário não deve poder seguir a si mesmo.
- **Seguindo**: O link "Seguindo" na barra de navegação deve levar o usuário a uma página onde ele veja todas as postagens feitas por usuários que o usuário atual segue.
  - Esta página deve se comportar da mesma forma que a página "Todas as Postagens", só que com um conjunto mais limitado de postagens.
  - Esta página deve estar disponível apenas para usuários autenticados.
- **Paginação**: Em qualquer página que exiba postagens, as postagens devem ser exibidas em grupos de 10 por página. Se houver mais de dez postagens, um botão "Próximo" deve aparecer para levar o usuário para a próxima página de postagens (que deve ser mais antiga do que a página atual de postagens). Se não estiver na primeira página, um botão "Anterior" deve aparecer para levar o usuário para a página anterior de postagens também.
  - Veja a seção **Dicas** para algumas sugestões sobre como implementar isso.
- **Editar Postagem**: Os usuários devem poder clicar em um botão ou link "Editar" em qualquer uma de suas próprias postagens para editar aquela postagem.
  - Quando um usuário clica em "Editar" em uma de suas próprias postagens, o conteúdo da postagem deve ser substituído por um `textarea` onde o usuário pode editar o conteúdo de sua postagem.
  - O usuário deve então poder "Salvar" a postagem editada. Usando JavaScript, você deve conseguir fazer isso sem exigir que a página inteira seja recarregada.
  - Por questões de segurança, garanta que sua aplicação seja projetada de forma que não seja possível para um usuário, por meio de qualquer rota, editar as postagens de outro usuário.
- **"Curtir" e "Descurtir"**: Os usuários devem poder clicar em um botão ou link em qualquer postagem para alternar se eles "curtem" ou não aquela postagem.
  - Usando JavaScript, você deve permitir de forma assíncrona que o servidor saiba para atualizar o contador de curtidas (como via uma chamada para `fetch`) e então atualizar o contador de curtidas da postagem exibida na página, sem exigir que a página inteira seja recarregada.

## Dicas

- Para exemplos de chamadas `fetch` em JavaScript, você pode achar algumas rotas no Projeto 3 úteis para referência.
- Provavelmente você precisará criar um ou mais modelos em `network/models.py` e/ou modificar o modelo `User` existente para armazenar os dados necessários para sua aplicação web.
- A classe [Paginator](https://docs.djangoproject.com/en/4.0/topics/pagination/) do Django pode ser útil para implementar a paginação no lado do backend (no seu código Python).
- Os recursos de [Paginação](https://getbootstrap.com/docs/4.4/components/pagination/) do Bootstrap podem ser úteis para exibir páginas no lado do frontend (no seu HTML).

## Como Submeter

1. Visite [este link](https://submit.cs50.io/invites/89679428401548238ceb022f141b9947), faça login com sua conta do GitHub e clique em **Authorize cs50**. Em seguida, marque a caixa indicando que deseja conceder acesso da equipe do curso às suas submissões e clique em **Join course**.
2. [Instale o Git](https://git-scm.com/downloads) e, opcionalmente, [instale o `submit50`](https://cs50.readthedocs.io/submit50/).

<div class="alert alert-success" data-alert="success" role="alert"><p>Quando você enviar seu projeto, o conteúdo do seu ramo <code class="language-plaintext highlighter-rouge">web50/projects/2020/x/network</code> deve corresponder à estrutura de arquivos do código de distribuição descompactado conforme originalmente recebido. Isso quer dizer que seus arquivos não devem estar aninhados dentro de nenhum outro diretório de sua própria criação. Seu ramo também não deve conter código de outros projetos, apenas deste. Não seguir esta estrutura de arquivos provavelmente resultará na rejeição da sua submissão.</p>

<p>Como exemplo, para este projeto, isso significa que se a equipe de avaliação visitar <code class="language-plaintext highlighter-rouge">https://github.com/me50/USERNAME/tree/web50/projects/2020/x/network</code> (onde <code class="language-plaintext highlighter-rouge">USERNAME</code> é o seu nome de usuário no GitHub fornecido no formulário) deveríamos ver os dois subdiretórios (<code class="language-plaintext highlighter-rouge">network</code>, <code class="language-plaintext highlighter-rouge">project4</code>) e o arquivo <code class="language-plaintext highlighter-rouge">manage.py</code>. Se o seu código não estiver organizado desta forma quando você checar, reorganize seu repositório conforme necessário para corresponder a esse paradigma.</p></div>

3.  Se você instalou o `submit50`, execute

        submit50 web50/projects/2020/x/network

    Caso contrário, usando o Git, envie seu trabalho para `https://github.com/me50/USERNAME.git`, onde `USERNAME` é seu nome de usuário no GitHub, em um ramo chamado `web50/projects/2020/x/network`.

4.  [Faça uma captura de tela](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) com duração máxima de 5 minutos (e não carregada há mais de um mês antes da sua submissão deste projeto), na qual você demonstra a funcionalidade do seu projeto. Certifique-se de que cada elemento da especificação acima seja demonstrado no seu vídeo. Não é necessário mostrar seu código neste vídeo, apenas sua aplicação em ação; revisaremos seu código no GitHub. [Faça o upload desse vídeo no YouTube](https://www.youtube.com/upload) (como não listado ou público, mas não privado) ou outro local. Na descrição do seu vídeo, você deve marcar o horário em que o vídeo demonstra cada um dos sete (7) elementos da especificação. **Isso não é opcional**, vídeos sem horários marcados em sua descrição serão automaticamente rejeitados.
5.  Envie [este formulário](https://forms.cs50.io/fd9d10b0-faf7-44d4-8009-410ebae3431b).

Você pode ir para [https://cs50.me/cs50w](https://cs50.me/cs50w) para ver seu progresso atual!
