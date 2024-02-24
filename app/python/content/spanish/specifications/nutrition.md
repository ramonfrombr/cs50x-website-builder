

# Información Nutricional

La Administración de Alimentos y Medicamentos de los Estados Unidos (FDA, por sus siglas en inglés) ofrece carteles descargables/imprimibles que "muestran información nutricional de las 20 frutas crudas más consumidas en los Estados Unidos. Las tiendas minoristas pueden descargar los carteles, imprimirlos, mostrarlos o distribuirlos a los consumidores en las cercanías de los alimentos relevantes en las tiendas".

En un archivo llamado `nutrition.py`, implementa un programa que solicite a los usuarios que ingresen una fruta (sin importar las mayúsculas o minúsculas) y luego muestre el número de calorías en una porción de esa fruta, según el póster de frutas de la FDA, que también está disponible en forma de texto. Ignora cualquier entrada que no sea una fruta.

Pistas:

- En lugar de usar una condición con 20 expresiones booleanas, una para cada fruta, es mejor usar un `dict` para asociar una fruta con sus calorías.
- Si `k` es una `str` y `d` es un `dict`, puedes verificar si `k` es una clave en `d` con código como este:

      si k en d:
          ...

- ¡Asegúrate de mostrar las calorías de la fruta, no las calorías provenientes de la grasa!

## Demo

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de la terminal y ejecuta `cd` por sí solo. Debería aparecer el siguiente indicador de la terminal:

    $

A continuación, ejecuta

    mkdir nutrition

para crear una carpeta llamada `nutrition` en tu espacio de trabajo de código.

Luego ejecuta

    cd nutrition

para cambiar al directorio de esa carpeta. Ahora deberías ver el indicador de la terminal como `nutrition/ $`. Ahora puedes ejecutar

    code nutrition.py

para crear un archivo llamado `nutrition.py`, donde escribirás tu programa.

## Cómo Probar

Así es cómo puedes probar tu código manualmente:

- Ejecuta tu programa con `python nutrition.py`. Escribe `Manzana` y presiona Enter. Tu programa debería mostrar:

      Calorías: 130

- Ejecuta tu programa con `python nutrition.py`. Escribe `Aguacate` y presiona Enter. Tu programa debería mostrar:

      Calorías: 50

- Ejecuta tu programa con `python nutrition.py`. Escribe `Cerezas Dulces` y presiona Enter. Tu programa debería mostrar:

      Calorías: 100

- Ejecuta tu programa con `python nutrition.py`. Escribe `Tomate` y presiona Enter. Tu programa no debería mostrar nada.

Asegúrate de probar con otras frutas y variar el formato de mayúsculas y minúsculas de tu entrada. Tu programa debería comportarse como se espera, sin importar las mayúsculas o minúsculas.

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 usará para probar tu código cuando lo envíes. Pero también asegúrate de probarlo tú mismo.

    check50 cs50/problems/2022/python/nutrition

¡Los emojis verdes significan que tu programa ha pasado una prueba! Los emojis rojos indicarán que tu programa ha producido una salida inesperada. Visita la URL que `check50` muestra para ver la entrada que `check50` proporcionó a tu programa, la salida esperada y la salida real de tu programa.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/nutrition