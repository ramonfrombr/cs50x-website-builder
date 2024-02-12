

# Validación de respuesta

Al crear un [Formulario de Google](https://www.google.com/forms/about/) que solicita a los usuarios una respuesta breve (o párrafo), es posible habilitar la [validación de respuesta](https://support.google.com/docs/answer/3378864) y requerir que la entrada del usuario coincida con una [expresión regular](https://support.google.com/a/answer/1371415). Por ejemplo, se puede requerir que el usuario ingrese una dirección de correo electrónico utilizando una expresión regular como [esta](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address):

.html pre { white-space: pre-wrap; }

    ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

O también se puede usar más fácilmente el soporte incorporado de Google para validar una dirección de correo electrónico, como se muestra a continuación, de la misma manera que se podría usar una biblioteca en su propio código:

![Formulario de Google](form.png)

En un archivo llamado `response.py`, utilizando ya sea [validator-collection](https://pypi.org/project/validator-collection/) o [validators](https://github.com/kvesteri/validators) de PyPI, implemente un programa que solicite al usuario una dirección de correo electrónico a través de `input` y luego imprima `Válido` o `Inválido`, respectivamente, si la entrada es una dirección de correo electrónico válida sintácticamente. No se permite utilizar `re`. Y no se debe validar si el nombre de dominio de la dirección de correo electrónico realmente existe.

Indicaciones

- Tenga en cuenta que puede instalar validator-collection con el siguiente comando:

      pip install validator-collection

  Haga clic en **Homepage** para acceder a la documentación de la biblioteca.

- Tenga en cuenta que puede instalar validators con el siguiente comando:

      pip install validators

  Haga clic en **Homepage** para acceder a la documentación de la biblioteca.

## Demo

## Antes de comenzar

Inicie sesión en [cs50.dev](https://cs50.dev/), haga clic en su ventana de terminal y ejecute `cd` por sí solo. Debería ver que el indicador de su ventana de terminal se parece al siguiente:

    $

A continuación, ejecute

    mkdir response

para crear una carpeta llamada `response` en su espacio de código.

Luego, ejecute

    cd response

para cambiar al directorio de esa carpeta. Ahora debería ver el indicador de su terminal como `response/ $`. Ahora puede ejecutar

    code response.py

para crear un archivo llamado `response.py` donde escribirá su programa.

## Cómo probar

Aquí se explica cómo probar su código manualmente:

- Ejecute su programa con `python response.py`. Asegúrese de que su programa le solicite un correo electrónico, luego escriba `malan@harvard.edu` y presione Enter. Su programa debería imprimir `Válido`.
- Ejecute su programa con `python response.py`. Escriba su propio correo electrónico y presione Enter. Su programa debería imprimir `Válido`.
- Ejecute su programa con `python response.py`. Escriba `malan@@@harvard.edu` y presione Enter. Su programa debería imprimir `Inválido`.
- Ejecute su programa con `python response.py`. Escriba incorrectamente su propio correo electrónico, incluyendo un `.` adicional antes de `.com`, por ejemplo. Presione enter y su programa debería imprimir `Inválido`.

Puede ejecutar lo siguiente para verificar su código utilizando `check50`, un programa que CS50 utilizará para probar su código cuando lo envíe. ¡Pero asegúrese de probarlo usted mismo también!

    check50 cs50/problems/2022/python/response

¡Las caritas verdes indican que su programa ha aprobado una prueba! Las caritas rojas indicarán que su programa ha generado un resultado inesperado. Visite la URL que `check50` proporciona para ver la entrada que `check50` le proporcionó a su programa, la salida esperada y la salida real de su programa.

## Cómo enviar

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2022/python/response