# Certificado CS50 da Camisa

[![Certificado da Camisa CS50 de John Harvard](jharvard.png)](jharvard.pdf)

Suponha que você deseja implementar um "shirtificate" do CS50, um PDF com uma imagem de uma camisa [I took CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt), [shirtificate.png](shirtificate.png), personalizada com o nome do usuário.

Em um arquivo chamado `shirtificate.py`, implemente um programa que solicita ao usuário seu nome e gera, usando [fpdf2](https://pypi.org/project/fpdf2/), um certificado da camisa CS50 em um arquivo chamado `shirtificate.pdf` semelhante a [este para John Harvard](jharvard.pdf), com as seguintes especificações:

- A [orientação](https://py-pdf.github.io/fpdf2/PageFormatAndOrientation.html) do PDF deve ser retrato.
- O [formato](https://py-pdf.github.io/fpdf2/PageFormatAndOrientation.html) do PDF deve ser A4, que é 210mm de largura por 297mm de altura.
- O topo do PDF deve dizer "Certificado CS50 da Camisa" como [texto](https://py-pdf.github.io/fpdf2/Text.html), centralizado horizontalmente.
- A imagem da camisa deve estar centralizada horizontalmente.
- O nome do usuário deve estar no topo da camisa, em [texto](https://py-pdf.github.io/fpdf2/TextStyling.html) branco.

Todos os outros detalhes ficam a seu critério. Você pode adicionar bordas, cores e [linhas](https://py-pdf.github.io/fpdf2/Shapes.html#lines). Seu certificado da camisa não precisa corresponder exatamente ao de John Harvard. E não é necessário quebrar nomes longos em várias linhas.

Antes de escrever qualquer código, leia o [tutorial](https://py-pdf.github.io/fpdf2/Tutorial.html) do fpdf2 para aprender como usá-lo. Depois, analise a [API](https://py-pdf.github.io/fpdf2/fpdf/) (interface de programação de aplicativos) do fpdf2 para ver todas as suas funções e parâmetros.

Não é necessário enviar nenhum PDF com seu código. Mas, se desejar, você pode compartilhar um certificado da camisa com seu nome em uma das [comunidades da CS50](https://cs50.harvard.edu/python/communities)!

Dicas

- Observe que o fpdf2 possui uma `class` chamada `FPDF`, que possui muitos métodos, conforme [py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF](https://py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF). Você pode instalá-lo com:

      pip install fpdf2

- Observe que você pode estender `FPDF` e instanciar sua própria subclasse para adicionar um cabeçalho a cada página de um PDF, conforme [py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image](https://py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image). Ou você pode adicionar como texto manualmente.
- Observe que você pode desativar quebras de página automáticas, que de outra forma poderiam fazer com que seu PDF transbordasse de uma página para duas, com `set_auto_page_break`, conforme [py-pdf.github.io/fpdf2/Margins.html](https://py-pdf.github.io/fpdf2/Margins.html).
- Observe que a altura de uma [célula](https://py-pdf.github.io/fpdf2/Text.html#cell) pode ser negativa, para movê-la para cima.
- Você pode abrir o `shirtificate.pdf`, uma vez gerado, clicando nele no explorador de arquivos do VS Code.

## Demonstração

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique em sua janela de terminal e execute `cd` sozinho. Você deverá ver que o prompt de seu terminal se assemelha ao abaixo:

    $

Em seguida, execute

    mkdir shirtificate

para criar uma pasta chamada `shirtificate` em seu espaço de códigos.

Depois execute

    cd shirtificate

para mudar para esse diretório. Agora você deverá ver o prompt do seu terminal como `shirtificate/ $`. Agora execute

    wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png

para obter uma cópia da imagem `shirtificate.png` para o seu certificado. Finalmente, execute

    code shirtificate.py

para criar um arquivo chamado `shirtificate.py` onde você escreverá seu programa.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `shirtificate.py`. Certifique-se de que seu programa solicite um nome. Insira seu próprio nome e pressione Enter. Seu programa deve criar um arquivo, `shirtificate.pdf`, contendo o nome que você inseriu sobre uma renderização de `shirtificate.png`.
- Experimente com alguns outros nomes para garantir!

Você pode executar o abaixo para verificar seu código usando `check50`, um programa que a CS50 usará para testar seu código quando você enviar. Mas certifique-se de testá-lo por conta própria também!

    check50 cs50/problems/2022/python/shirtificate

Os sorrisos verdes significam que seu programa passou em um teste! As carinhas tristes vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que `check50` exibe para ver a entrada que `check50` forneceu ao seu programa, qual saída ele esperava e qual saída seu programa realmente deu.

## Como Enviar

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/shirtificate
