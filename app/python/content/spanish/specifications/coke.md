

# Máquina de Coca-Cola

![Botella de Coca-Cola CS50](coke.png)

Supongamos que una máquina vende botellas de Coca-Cola (Coke) por 50 centavos y solo acepta monedas en estas denominaciones: 25 centavos, 10 centavos y 5 centavos.

En un archivo llamado `coke.py`, implementa un programa que solicite al usuario insertar una moneda, una a la vez, informando al usuario del monto adeudado cada vez. Una vez que el usuario haya ingresado al menos 50 centavos, muestra cuántos centavos de cambio se le deben al usuario. Supón que el usuario solo ingresará números enteros y ignora cualquier número entero que no sea una denominación aceptada.

## Demostración

## Antes de comenzar

Inicia sesión en [cs50.dev] (https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

A continuación, ejecuta

    mkdir coke

para crear una carpeta llamada `coke` en tu entorno de codificación.

Luego, ejecuta

    cd coke

para cambiar al directorio de esa carpeta. Ahora deberías ver tu indicador de terminal como `coke/ $`. Ahora puedes ejecutar

    code coke.py

para crear un archivo llamado `coke.py` donde escribirás tu programa.

## Cómo probar

Aquí tienes cómo probar tu código manualmente:

- Ejecuta tu programa con `python coke.py`. En tu prompt `Insert Coin:`, escribe `25` y presiona Enter. Tu programa debería mostrar:

      Monto adeudado: 25

  y continuar solicitando al usuario monedas.

- Ejecuta tu programa con `python coke.py`. En tu prompt `Insert Coin:`, escribe `10` y presiona Enter. Tu programa debería mostrar:

      Monto adeudado: 40

  y continuar solicitando al usuario monedas.

- Ejecuta tu programa con `python coke.py`. En tu prompt `Insert Coin:`, escribe `5` y presiona Enter. Tu programa debería mostrar:

      Monto adeudado: 45

  y continuar solicitando al usuario monedas.

- Ejecuta tu programa con `python coke.py`. En tu prompt `Insert Coin:`, escribe `30` y presiona Enter. ¡Tu programa debería mostrar:

      Monto adeudado: 50

  porque ¡la máquina no acepta monedas de 30 centavos! Luego, tu programa debería continuar solicitando al usuario más monedas.

- Ejecuta tu programa con `python coke.py`. En tu prompt `Insert Coin:`, escribe `25` y presiona Enter, luego escribe `25` nuevamente y presiona Enter. Tu programa debería detenerse y mostrar:

      Cambio adeudado: 0

- Ejecuta tu programa con `python coke.py`. En tu prompt `Insert Coin:`, escribe `25` y presiona Enter, luego escribe `10` y presiona Enter. Escribe `25` nuevamente y presiona Enter, después de lo cual tu programa debería detenerse y mostrar:

      Cambio adeudado: 10

Puedes ejecutar el siguiente comando para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/coke

¡Las caritas verdes significan que tu programa ha aprobado una prueba! Las caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` proporciona para ver la entrada que `check50` pasó a tu programa, qué salida esperaba y qué salida realmente proporcionó tu programa.

Pista

Ten cuidado de imprimir las indicaciones y respuestas exactamente como se muestra arriba. Si tu programa imprime algún texto adicional, es posible que no pase `check50`.

## Cómo enviar

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/coke