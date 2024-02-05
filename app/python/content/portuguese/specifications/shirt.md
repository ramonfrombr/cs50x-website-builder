# CS50 Camiseta

![CS50 camiseta](took.png)

Após terminar o CS50 em si, os estudantes no campus de Harvard tradicionalmente recebem sua própria [Eu fiz CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt) camiseta. Não há necessidade de comprar uma online, mas gostaria de experimentar uma virtualmente?

Em um arquivo chamado `shirt.py`, implemente um programa que espera exatamente dois argumentos da linha de comando:

- em `sys.argv[1]`, o nome (ou caminho) de um arquivo JPEG ou PNG para ler (ou seja, abrir) como entrada
- em `sys.argv[2]`, o nome (ou caminho) de um arquivo JPEG ou PNG para escrever (ou seja, salvar) como saída

O programa deve então sobrepor [shirt.png](shirt.png) (que possui um fundo transparente) na entrada após redimensionar e recortar a entrada para ter o mesmo tamanho, salvando o resultado como saída.

Abra a entrada com `Image.open`, conforme [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open), redimensione e recorte a entrada com `ImageOps.fit`, conforme [pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit](https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit), usando os valores padrão para `method`, `bleed` e `centering`, sobreponha a camiseta com `Image.paste`, conforme [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste), e salve o resultado com `Image.save`, conforme [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save).

O programa deve sair através de `sys.exit` se:

- o usuário não especificar exatamente dois argumentos da linha de comando,
- os nomes da entrada e saída não terminarem em `.jpg`, `.jpeg` ou `.png`, insensivelmente a maiúsculas e minúsculas,
- o nome da entrada não tiver a mesma extensão que o nome da saída, ou
- a entrada especificada não existir.

Assuma que a entrada será uma foto de alguém posando de maneira adequada, como [esses exemplos](#demos), de modo que, quando redimensionadas e recortadas, a camiseta pareça se ajustar perfeitamente.

Se desejar executar seu programa em uma foto sua, primeiro arraste a foto para o explorador de arquivos do VS Code, para a mesma pasta que `shirt.py`. Não é necessário enviar fotos com seu código. Mas se quiser, fique à vontade (mas não é obrigatório) para compartilhar uma foto sua usando sua camiseta virtual em alguma das [comunidades CS50](https://cs50.harvard.edu/python/communities)!

Dicas

- Observe que você pode determinar a extensão de um arquivo com `os.path.splitext`, conforme [docs.python.org/3/library/os.path.html#os.path.splitext](https://docs.python.org/3/library/os.path.html#os.path.splitext).
- Observe que `open` pode `levantar` um `FileNotFoundError`, conforme [docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).
- Observe que o pacote `Pillow` vem com várias classes e métodos, conforme [pypi.org/project/Pillow](https://pypi.org/project/Pillow/). Você pode achar seu [manual](https://pillow.readthedocs.io/en/stable/handbook/) e [referência](https://pillow.readthedocs.io/en/stable/reference/) úteis para consultar. Você pode instalar o pacote com:

      pip install Pillow

  Você pode abrir uma imagem (por exemplo, `shirt.png`) com um código como:

      shirt = Image.open("shirt.png")

  Você pode obter a largura e altura, respectivamente, dessa imagem como uma `tupla` com um código como:

      size = shirt.size

  E você pode sobrepor essa imagem em cima de outra (por exemplo, `foto`) com um código como:

      photo.paste(shirt, shirt)

  onde o primeiro `shirt` representa a imagem a ser sobreposta e o segundo `shirt` representa uma "máscara" indicando quais pixels em `photo` devem ser atualizados.

- Observe que você pode abrir uma imagem (por exemplo, `shirt.png`) no VS Code executando

      code shirt.png

  ou clicando duas vezes no ícone no explorador de arquivos do VS Code.

## Demonstração

### Antes

[![antes](before1.jpg)](before1.jpg) [![antes](before2.jpg)](before2.jpg) [![antes](before3.jpg)](before3.jpg)

### Depois

![depois](after1.jpg) ![depois](after2.jpg) ![depois](after3.jpg)

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Deve aparecer algo semelhante à imagem abaixo no seu terminal:

    $

Em seguida, execute

    mkdir shirt

para criar uma pasta chamada `shirt` em seu espaço de códigos.

Depois execute

    cd shirt

para mudar de diretório para essa pasta. Você deve ver agora o prompt do terminal como `shirt/ $`. Agora você pode executar

    code shirt.py

para criar um arquivo chamado `shirt.py`, onde você escreverá seu programa. Certifique-se de executar

    wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png

para baixar [shirt.png](shirt.png). Certifique-se também de executar

    wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip

para baixar [muppets.zip](muppets.zip) para sua pasta. Você pode então executar

    unzip muppets.zip

para extrair uma coleção de fotos dos Muppets!

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python shirt.py`. Seu programa deve sair usando `sys.exit` e fornecer uma mensagem de erro:

      Poucos argumentos da linha de comando

- Certifique-se de baixar [muppets.zip](muppets.zip) e extrair uma coleção de fotos dos Muppets usando `unzip muppets.zip`. Execute seu programa com `python shirt.py before1.jpg before2.jpg before3.jpg`. Seu programa deve retornar:

      Muitos argumentos da linha de comando

- Execute seu programa com `python shirt.py before1.jpg formato_invalido.bmp`. Seu programa deve sair usando `sys.exit` e fornecer uma mensagem de erro:

      Saída inválida

- Execute seu programa com `python shirt.py before1.jpg after1.png`. Seu programa deve sair usando `sys.exit` e fornecer uma mensagem de erro:

      A entrada e a saída têm extensões diferentes

- Execute seu programa com `python shirt.py imagem_inexistente.jpg after1.jpg`. Seu programa deve sair usando `sys.exit` e fornecer uma mensagem de erro:

      A entrada não existe

- Execute seu programa com `python shirt.py before1.jpg after1.jpg`. Supondo que você tenha baixado e descompactado [muppets.zip](muppets.zip), seu programa deve criar uma imagem como a abaixo:  
  ![depois](after1.jpg)

Você pode executar o código abaixo para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código quando você o enviar. Mas certifique-se de testá-lo você mesmo também!

    check50 cs50/problems/2022/python/shirt

Smiles verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` retorna para ver a entrada que o `check50` enviou para seu programa, qual saída esperava e qual saída seu programa realmente forneceu.

## Como Enviar

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/shirt
