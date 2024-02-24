

# Índice del Precio de Bitcoin

![Logo de Bitcoin](Bitcoin.svg.png)

[Bitcoin](https://es.wikipedia.org/wiki/Bitcoin) es una forma de moneda digital, también conocida como [criptomoneda](https://es.wikipedia.org/wiki/Criptomoneda). En lugar de depender de una autoridad central como un banco, Bitcoin depende de una red distribuida, también conocida como [blockchain](https://es.wikipedia.org/wiki/Blockchain), para registrar transacciones.

Debido a la demanda de Bitcoin (es decir, los usuarios lo desean), los usuarios están dispuestos a comprarlo, es decir, intercambiar una moneda (por ejemplo, USD) por Bitcoin.

En un archivo llamado `bitcoin.py`, implementa un programa que:

- Espera que el usuario especifique como argumento de línea de comandos el número de Bitcoins, \\(n\\), que les gustaría comprar. Si ese argumento no se puede convertir a `float`, el programa debe salir a través de `sys.exit` con un mensaje de error.
- Consulta la API del Índice de Precio de Bitcoin de CoinDesk en [https://api.coindesk.com/v1/bpi/currentprice.json](https://api.coindesk.com/v1/bpi/currentprice.json), que devuelve un objeto [JSON](https://es.wikipedia.org/wiki/JSON), entre cuyas claves anidadas se encuentra el precio actual de Bitcoin como un `float`. Asegúrate de capturar cualquier [excepción](https://requests.readthedocs.io/en/latest/api/#exceptions), por ejemplo, con el siguiente código:

      import requests

      try:
          ...
      except requests.RequestException:
          ...

- Muestra el costo actual de \\(n\\) Bitcoins en USD con cuatro decimales, usando `,` como separador de miles.

Sugerencias

- Recuerda que el módulo `sys` incluye `argv`, según [docs.python.org/3/library/sys.html#sys.argv](https://docs.python.org/3/library/sys.html#sys.argv).
- Ten en cuenta que el módulo `requests` tiene varios métodos, según [requests.readthedocs.io/en/latest](https://requests.readthedocs.io/en/latest/), entre ellos `get`, según [requests.readthedocs.io/en/latest/user/quickstart.html#make-a-request](https://requests.readthedocs.io/en/latest/user/quickstart.html#make-a-request), y `json`, según [requests.readthedocs.io/en/latest/user/quickstart.html#json-response-content](https://requests.readthedocs.io/en/latest/user/quickstart.html#json-response-content). Puedes instalarlo con:

      pip install requests

- Ten en cuenta que la API de CoinDesk devuelve una respuesta JSON como esta:

      {
         "time":{
            "updated":"Mayo 2, 2022 15:27:00 UTC",
            "updatedISO":"2022-05-02T15:27:00+00:00",
            "updateduk":"Mayo 2, 2022 a las 16:27 BST"
         },
         "disclaimer":"Estos datos se obtuvieron del Índice de Precio de Bitcoin de CoinDesk (USD). Los datos de moneda no USD se convirtieron utilizando la tasa de conversión por hora de openexchangerates.org",
         "chartName":"Bitcoin",
         "bpi":{
            "USD":{
               "code":"USD",
               "symbol":"&#36;",
               "rate":"38,761.0833",
               "description":"Dólar Estadounidense",
               "rate_float":38761.0833
            },
            "GBP":{
               "code":"GBP",
               "symbol":"&pound;",
               "rate":"30,827.6198",
               "description":"Libra Esterlina Británica",
               "rate_float":30827.6198
            },
            "EUR":{
               "code":"EUR",
               "symbol":"&euro;",
               "rate":"36,800.2764",
               "description":"Euro",
               "rate_float":36800.2764
            }
         }
      }

- Recuerda que puedes formatear USD a cuatro decimales con un [separador de miles](https://docs.python.org/3/library/string.html#formatspec) con código como este:

      print(f"${amount:,.4f}")

## Demostración

Esta demostración se grabó cuando el precio de Bitcoin era de $38,761.0833. Tus propias salidas pueden variar.

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

A continuación, ejecuta

    mkdir bitcoin

para crear una carpeta llamada `bitcoin` en tu entorno de programación.

Luego ejecuta

    cd bitcoin

para cambiar al directorio de esa carpeta. Ahora deberías ver el indicador de tu terminal como `bitcoin/ $`. Ahora puedes ejecutar

    code bitcoin.py

para crear un archivo llamado `bitcoin.py` en el que escribirás tu programa.

## Cómo probar

Así es como puedes probar tu código manualmente:

- Ejecuta tu programa con `python bitcoin.py`. Tu programa debería utilizar `sys.exit` para salir con un mensaje de error:

      Falta el argumento de línea de comandos

- Ejecuta tu programa con `python bitcoin.py gato`. Tu programa debería utilizar `sys.exit` para salir con un mensaje de error:

      El argumento de línea de comandos no es un número

- Ejecuta tu programa con `python bitcoin.py 1`. Tu programa debería mostrar el precio de un solo Bitcoin con cuatro decimales, usando `,` como [separador de miles](https://docs.python.org/3/library/string.html#formatspec).
- Ejecuta tu programa con `python bitcoin.py 2`. Tu programa debería mostrar el precio de dos Bitcoins con cuatro decimales, usando `,` como [separador de miles](https://docs.python.org/3/library/string.html#formatspec).
- Ejecuta tu programa con `python bitcoin.py 2.5`. Tu programa debería mostrar el precio de 2.5 Bitcoins con cuatro decimales, usando `,` como [separador de miles](https://docs.python.org/3/library/string.html#formatspec).

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 usará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/bitcoin

¡Las caritas verdes significan que tu programa ha superado una prueba! Las caritas rojas indicarán que tu programa ha producido un resultado inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le dio a tu programa, qué salida esperaba y qué salida dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/bitcoin