*   No sétimo `TODO`, você deve implementar a função `get_block_size`. `get_block_size`, assim como `check_format`, recebe um único argumento: isso é um `WAVHEADER` chamado `header`, que representa a estrutura contendo o cabeçalho do arquivo de entrada. `get_block_size` deve retornar um número inteiro representando o tamanho do **bloco** do arquivo WAV fornecido, em bytes. Podemos pensar em um _bloco_ como uma unidade de dados auditivos. Para áudio, calculamos o tamanho de cada bloco com o seguinte cálculo: **número de canais** multiplicado por **bytes por amostra**. Felizmente, o cabeçalho contém todas as informações de que precisamos para calcular esses valores. Certifique-se de consultar a seção [Background](#background) para uma explicação mais detalhada sobre o que esses valores significam e como eles são armazenados. Consulte também `wav.h`, para determinar quais membros de `WAVHEADER` podem ser úteis.
<ul>
<li data-marker="+">Dicas
  <ul>
    <li data-marker="*">Observe que um dos membros de `WAVHEADER` é `bitsPerSample`. Mas, para calcular o tamanho do bloco, você precisará de **bytes** por amostra!</li>
  </ul>
</li>
</ul>

*   O oitavo e último `TODO` é onde ocorre a inversão real do áudio. Para fazer isso, precisamos ler cada bloco de dados auditivos começando do final do arquivo de entrada e retrocedendo, escrevendo simultaneamente cada bloco no arquivo de saída para que sejam escritos em ordem inversa. Primeiro, devemos declarar um array para armazenar cada bloco lido. Em seguida, cabe a você iterar pelos dados de áudio do arquivo de entrada. Certifique-se de ler todo o áudio, mas não copie erroneamente nenhum dos dados do cabeçalho! Além disso, para fins de teste, gostaríamos de manter a ordem dos canais para cada bloco de áudio. Por exemplo, em um arquivo WAV com dois canais (som estereofônico), queremos garantir que o primeiro canal do último bloco de áudio na entrada se torne o primeiro canal do primeiro bloco de áudio na saída.
<ul>
<li data-marker="+">Dicas
    <ul>
      <li data-marker="*">Algumas funções (e uma compreensão minuciosa de seu uso) podem ser especialmente úteis ao concluir esta seção - as páginas do manual do CS50 podem ser especialmente úteis aqui:
        <ul>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fread"><code class="language-plaintext highlighter-rouge">fread</code></a>: lê de um arquivo para um buffer. A saída da função auxiliar <code class="language-plaintext highlighter-rouge">get_block_size</code> pode ser útil aqui ao decidir quais valores usar para o tamanho e o número de dados a serem lidos de uma vez.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fwrite"><code class="language-plaintext highlighter-rouge">fwrite</code></a>: escreve de um buffer para um arquivo.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fseek"><code class="language-plaintext highlighter-rouge">fseek</code></a>: define um ponteiro de arquivo para um deslocamento específico. Pode ser útil experimentar com valores de deslocamento negativos para mover um ponteiro de arquivo para trás.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/ftell"><code class="language-plaintext highlighter-rouge">ftell</code></a>: retorna a posição atual de um ponteiro de arquivo. Pode ser útil inspecionar qual valor <code class="language-plaintext highlighter-rouge">ftell</code> retorna depois que o cabeçalho de entrada é lido no terceiro `TODO`, além do que ele retorna durante a leitura dos dados de áudio.</li>
        </ul>
      </li>
      <li data-marker="*">Lembre-se de que depois de usar `fread` para carregar um bloco de dados, o ponteiro `input` estará apontando para a posição em que a leitura foi concluída. Em outras palavras, o ponteiro `input` pode precisar ser movido de volta **dois** tamanhos de bloco após cada `fread`, um para voltar à posição em que o `fread` começou e o segundo para mover para o bloco não lido anterior.</li>
    </ul>
</li>
</ul>

*   Por fim, certifique-se de fechar todos os arquivos que você abriu!