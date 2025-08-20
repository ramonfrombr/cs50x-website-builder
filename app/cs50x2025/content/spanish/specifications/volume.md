## Volumen

![Forma de onda del archivo WAV](https://cs50.harvard.edu/x/2024/psets/4/volume/wav_file.png)

## Problema a resolver

Los [archivos WAV](https://docs.fileformat.com/audio/wav/) son un formato de archivo común para representar audio. Los archivos WAV almacenan audio como una secuencia de "muestras": números que representan el valor de alguna señal de audio en un momento determinado. Los archivos WAV comienzan con un "encabezado" de 44 bytes que contiene información sobre el archivo en sí, incluyendo el tamaño del archivo, el número de muestras por segundo y el tamaño de cada muestra. Después del encabezado, el archivo WAV contiene una secuencia de muestras, cada una de las cuales es un entero de 2 bytes (16 bits) que representa la señal de audio en un momento determinado.

Escalar cada valor de muestra por un factor determinado tiene el efecto de cambiar el volumen del audio. Multiplicar cada valor de muestra por 2.0, por ejemplo, tendrá el efecto de duplicar el volumen del audio original. Multiplicar cada muestra por 0.5, por otro lado, tendrá el efecto de reducir el volumen a la mitad.

En un archivo llamado `volume.c` en una carpeta llamada `volume`, escribe un programa para modificar el volumen de un archivo de audio.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-mc2hPhYDt1spoMjlqNMuqC4Uc" src="https://asciinema.org/a/mc2hPhYDt1spoMjlqNMuqC4Uc.js"></script>

## Código de Distribución

Para este problema, ampliarás la funcionalidad del código que te proporciona el personal de CS50.

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí mismo. Deberías encontrar que la solicitud de la ventana de tu terminal se asemeja a la siguiente:

    $

A continuación, ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/4/volume.zip

para descargar un ZIP llamado `volume.zip` en tu espacio de códigos.

Luego ejecuta

    unzip volume.zip

para crear una carpeta llamada `volume`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm volume.zip

y responder con "y" seguido de Enter en el mensaje para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd volume

seguido de Enter para moverte (es decir, abrir) a ese directorio. Tu solicitud ahora debe parecerse a la siguiente.

    volume/ $

Si todo tuvo éxito, debes ejecutar

    ls

y ver un archivo llamado `volume.c`. La ejecución de `code volume.c` debe abrir el archivo donde escribirás tu código para este conjunto de problemas. Si no es así, ¡revisa tus pasos y mira si puedes determinar dónde te equivocaste!

## Detalles de la implementación

Completa la implementación de `volume.c`, de tal manera que cambie el volumen de un archivo de sonido por un factor determinado.

- El programa debe aceptar tres argumentos de línea de comandos. El primero es `input`, que representa el nombre del archivo de audio original. El segundo es `output`, que representa el nombre del nuevo archivo de audio que se debe generar. El tercero es `factor`, que es la cantidad por la cual se debe escalar el volumen del archivo de audio original.
  - Por ejemplo, si `factor` es `2.0`, entonces tu programa debe duplicar el volumen del archivo de audio en `input` y guardar el archivo de audio recién generado en `output`.
- Tu programa primero debe leer el encabezado del archivo de entrada y escribir el encabezado en el archivo de salida.
- Tu programa debe leer el resto de los datos del archivo WAV, una muestra de 16 bits (2 bytes) a la vez. Tu programa debe multiplicar cada muestra por el `factor` y escribir la nueva muestra en el archivo de salida.
  - Puedes asumir que el archivo WAV usará valores de 16 bits con signo como muestras. En la práctica, los archivos WAV pueden tener un número variable de bits por muestra, pero asumiremos muestras de 16 bits para este problema.
- Tu programa, si utiliza `malloc`, no debe perder ninguna memoria.

## Consejos

### Entender el código en `volume.c`

En primer lugar, observa que `volume.c` ya está configurado para tomar tres argumentos de línea de comandos, `input`, `output` y `factor`.

- `main` toma un `int`, `argc` y una matriz de `char *`s (¡cadenas!), `argv`.
- Si `argc`, el número de argumentos en la línea de comandos, incluido el programa en sí, no es igual a 4, el programa imprimirá su uso correcto y saldrá con el código de estado 1.

        int main(int argc, char \*argv[])
        {
            // Verificar argumentos de línea de comandos
            if (argc != 4)
            {
                printf("Uso: ./volume input.wav output.wav factor\n");
                return 1;
            }

            // ...
        }

A continuación, `volume.c` utiliza [`fopen`](https://manual.cs50.io/3/fopen) para abrir los dos archivos proporcionados como argumentos de línea de comandos.

- Es una buena práctica verificar si el resultado de llamar a `fopen` es `NULL`. Si lo es, el archivo no se encontró o no se pudo abrir.

        // Abrir archivos y determinar factor de escalado
        FILE *input = fopen(argv[1], "r");
        if (input == NULL)
        {
            printf("No se pudo abrir el archivo.\n");
            return 1;
        }

        FILE *output = fopen(argv[2], "w");
        if (output == NULL)
        {
            printf("No se pudo abrir el archivo.\n");
            return 1;
        }

Más tarde, estos archivos se cierran con `fclose`. ¡Siempre que llames a `fopen`, debes llamar posteriormente a `fclose`!

        // Cerrar archivos
        fclose(input);
        fclose(output);

Sin embargo, antes de cerrar los archivos, observa que tenemos algunas tareas pendientes.

        // TODO: Copiar encabezado del archivo de entrada al archivo de salida

        // TODO: Leer muestras del archivo de entrada y escribir datos actualizados en el archivo de salida

Es probable que necesites saber el factor por el cual escalar el volumen, por lo que `volume.c` ya convierte el tercer argumento de línea de comandos en un `float` para ti.

        float factor = atof(argv[3]);

### Copiar encabezado WAV desde el archivo de entrada al archivo de salida

Tu primera tarea es copiar el encabezado del archivo WAV desde `entrada` y escribirlo en `salida`. Sin embargo, primero deberás aprender sobre algunos tipos de datos especiales.

Hasta ahora, hemos visto diferentes tipos en C, incluyendo `int`, `bool`, `char`, `double`, `float` y `long`. Sin embargo, dentro de un archivo de encabezado llamado `stdint.h` están las declaraciones de otros tipos que nos permiten definir con mucha precisión el tamaño (en bits) y el signo (con signo o sin signo) de un entero. Dos tipos en particular serán útiles cuando trabajemos con archivos WAV:

- `uint8_t` es un tipo que almacena un entero sin signo (es decir, no negativo) de 8 bits (¡por eso 8!) (¡por eso `uint`!). Podemos tratar cada byte del encabezado de un archivo WAV como un valor `uint8_t`.
- `int16_t` es un tipo que almacena un entero con signo (es decir, positivo o negativo) de 16 bits. Podemos tratar cada muestra de audio en un archivo WAV como un valor `int16_t`.

Probablemente desearás crear un arreglo de bytes para almacenar los datos del encabezado del archivo WAV que leerás desde el archivo de entrada. Usando el tipo `uint8_t` para representar un byte, puedes crear un arreglo de `n` bytes para tu encabezado con la sintaxis como

    uint8_t header[n];

reemplazando `n` con el número de bytes. Luego puedes usar `header` como argumento para [`fread`](https://manual.cs50.io/3/fread) o [`fwrite`](https://manual.cs50.io/3/fwrite) para leer o escribir desde el encabezado.

Recuerda que el encabezado de un archivo WAV siempre tiene exactamente 44 bytes de longitud. Ten en cuenta que `volume.c` ya define una variable para ti llamada `HEADER_SIZE`, igual al número de bytes en el encabezado.

La siguiente es una pista bastante grande, ¡pero así es como podrías lograr esta tarea!

    // Copiar encabezado desde el archivo de entrada al archivo de salida
    uint8_t header[HEADER_SIZE];
    fread(header, HEADER_SIZE, 1, input);
    fwrite(header, HEADER_SIZE, 1, output);

### Escribir datos actualizados en el archivo de salida

Tu siguiente tarea es leer muestras desde `entrada`, actualizar esas muestras y escribir las muestras actualizadas en `salida`. Al leer archivos, es común crear un "buffer" en el cual almacenar datos temporalmente. Ahí puedes modificar los datos y, una vez que estén listos, escribir los datos del buffer en un nuevo archivo.

Recuerda que podemos usar el tipo `int16_t` para representar una muestra de un archivo WAV. Para almacenar una muestra de audio, entonces, puedes crear una variable de buffer con una sintaxis como:

    // Crear un buffer para una sola muestra
    int16_t buffer;

Con un buffer para muestras en su lugar, ahora puedes leer datos en él, una muestra a la vez. ¡Intenta usar `fread` para esta tarea! Puedes usar `&buffer`, la dirección de `buffer`, como argumento para `fread` o `fwrite` para leer o escribir desde el buffer. (Recuerda que el operador `&` se usa para obtener la dirección de la variable).

    // Crear un buffer para una sola muestra
    int16_t buffer;

    // Leer muestra individual en el buffer
    fread(&buffer, sizeof(int16_t), 1, input)

Ahora, para aumentar (o disminuir) el volumen de una muestra, solo necesitas multiplicarla por algún factor.

    // Crear un buffer para una sola muestra
    int16_t buffer;

    // Leer muestra individual en el buffer
    fread(&buffer, sizeof(int16_t), 1, input)

    // Actualizar volumen de la muestra
    buffer *= factor;

Y finalmente, puedes escribir esa muestra actualizada en `salida`:

    // Crear un buffer para una sola muestra
    int16_t buffer;

    // Leer muestra individual desde entrada en el buffer
    fread(&buffer, sizeof(int16_t), 1, input)

    // Actualizar volumen de la muestra
    buffer *= factor;

    // Escribir muestra actualizada en un nuevo archivo
    fwrite(&buffer, sizeof(int16_t), 1, output);

Solo hay un problema: necesitarás seguir leyendo una muestra en tu buffer, actualizando su volumen y escribiendo la muestra actualizada en el archivo de salida mientras queden muestras para leer.

- Afortunadamente, por su documentación, `fread` devolverá el número de elementos de datos leídos exitosamente. ¡Puedes encontrar esto útil para verificar cuándo has llegado al final del archivo!
- Ten en cuenta que no hay ninguna razón por la que no puedas llamar a `fread` dentro de un condicional de un lazo `while`. Podrías, por ejemplo, hacer un llamado a `fread` como el siguiente:

        while (fread(...))
        {

        }

Es una gran pista, pero mira a continuación una forma eficiente de resolver este problema:

    // Crear un buffer para una sola muestra
    int16_t buffer;

    // Leer muestra individual desde entrada en el buffer mientras queden muestras para leer
    while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
    {
        // Actualizar volumen de la muestra
        buffer *= factor;

        // Escribir muestra actualizada en un nuevo archivo
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

Como la versión de C que estás usando trata a los valores distintos de cero como `true` y a los valores cero como `false`, podrías simplificar la sintaxis anterior a la siguiente:

    // Crear un buffer para una sola muestra
    int16_t buffer;

    // Leer muestra individual desde entrada en el buffer mientras queden muestras para leer
    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        // Actualizar volumen de la muestra
        buffer *= factor;

        // Escribir muestra actualizada en un nuevo archivo
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/LiGhjz9ColQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

<details><summary>¿No estás seguro de cómo resolverlo?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-rtZkTAK2gg?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

## Cómo probar

Tu programa debe comportarse según los ejemplos siguientes.

    $ ./volumen entrada.wav salida.wav 2.0

Cuando escuches `salida.wav` (por ejemplo, haciendo clic con control en `salida.wav` en el explorador de archivos, seleccionando **Descargar** y luego abriendo el archivo en un reproductor de audio en tu computadora), ¡debe ser el doble de fuerte que `entrada.wav`!

    $ ./volumen entrada.wav salida.wav 0.5

Cuando escuches `salida.wav`, ¡debe ser la mitad de fuerte que `entrada.wav`!

### Precisión

    check50 cs50/problems/2024/x/volumen

### Estilo

    style50 volumen.c

## Cómo enviar

    submit50 cs50/problems/2024/x/volumen

