

# Trabajando de 9 a 5

Mientras que [la mayoría de los países](https://en.wikipedia.org/wiki/Date_and_time_representation_by_country#Time) utilizan un [reloj de 24 horas](https://en.wikipedia.org/wiki/24-hour_clock), Estados Unidos tiende a utilizar un [reloj de 12 horas](https://en.wikipedia.org/wiki/12-hour_clock). En consecuencia, en lugar de "09:00 a 17:00", muchos estadounidenses dirían que trabajan de "9:00 AM a 5:00 PM" (o "9 AM a 5 PM"), donde "AM" es una abreviatura de "ante meridiem" y "PM" es una abreviatura de "post meridiem", donde "meridiem" significa mediodía (es decir, el mediodía).

<details><summary>Tabla de conversión</summary><p>Al igual que "12:00 AM" en formato de 12 horas sería "00:00" en formato de 24 horas, "12:01 AM" a través de "12:59 AM" también serían "00:01" a través de "00:59", respectivamente.</p>
| 12 horas | 24 horas |
| -------- | ------- |
| 12:00 AM | 00:00   |
| 1:00 AM  | 01:00   |
| 2:00 AM  | 02:00   |
| 3:00 AM  | 03:00   |
| 4:00 AM  | 04:00   |
| 5:00 AM  | 05:00   |
| 6:00 AM  | 06:00   |
| 7:00 AM  | 07:00   |
| 8:00 AM  | 08:00   |
| 9:00 AM  | 09:00   |
| 10:00 AM | 10:00   |
| 11:00 AM | 11:00   |
| 12:00 PM | 12:00   |
| 1:00 PM  | 13:00   |
| 2:00 PM  | 14:00   |
| 3:00 PM  | 15:00   |
| 4:00 PM  | 16:00   |
| 5:00 PM  | 17:00   |
| 6:00 PM  | 18:00   |
| 7:00 PM  | 19:00   |
| 8:00 PM  | 20:00   |
| 9:00 PM  | 21:00   |
| 10:00 PM | 22:00   |
| 11:00 PM | 23:00   |
| 12:00 AM | 00:00   |
</details>

En un archivo llamado `working.py`, implementa una función llamada `convert` que espera una cadena (`str`) en cualquiera de los formatos de 12 horas a continuación y devuelve la cadena correspondiente en formato de 24 horas (es decir, `9:00 a 17:00`). Se espera que `AM` y `PM` estén en mayúscula (sin puntos) y que haya un espacio antes de cada uno. Supón que estas horas representan horas reales, no necesariamente las 9:00 AM y 5:00 PM específicamente.

- `9:00 AM a 5:00 PM`
- `9 AM a 5 PM`

Genera un `ValueError` en su lugar si la entrada en `convert` no está en ninguno de esos formatos o si alguna de las horas es inválida (por ejemplo, `12:60 AM`, `13:00 PM`, etc.). Pero no asumas que las horas de trabajo de alguien comenzarán antes del mediodía y terminarán después del mediodía; alguien podría trabajar hasta tarde e incluso horas largas (por ejemplo, `5:00 PM a 9:00 AM`).

Estructura `working.py` de la siguiente manera, y modifica `main` y/o implementa otras funciones según sea necesario, pero no puedes importar ninguna otra biblioteca. Puedes usar `re` y/o `sys` si lo deseas.

```python
import re
import sys

def main():
    print(convert(input("Horas: ")))

def convert(s):
    ...

...

if __name__ == "__main__":
    main()
```

Ya sea antes o después de implementar `convert` en `working.py`, también implementa, en un archivo llamado `test_working.py`, **tres o más** funciones que prueben exhaustivamente tu implementación de `convert`, cada una de las cuales debe comenzar con `test_` para que puedas ejecutar tus pruebas con:

```bash
pytest test_working.py
```

<details><summary>Consejos</summary><ul>
  <li data-marker="*">Recuerda que el módulo <code class="language-plaintext highlighter-rouge">re</code> viene con varias funciones, según <a href="https://docs.python.org/3/library/re.html">docs.python.org/3/library/re.html</a>, incluida <code class="language-plaintext highlighter-rouge">search</code>.</li>
  <li data-marker="*">Recuerda que las expresiones regulares admiten varios caracteres especiales, según <a href="https://docs.python.org/3/library/re.html#regular-expression-syntax">docs.python.org/3/library/re.html#regular-expression-syntax</a>.</li>
  <li data-marker="*">Debido a que las barras invertidas en las expresiones regulares podrían confundirse con secuencias de escape (como <code class="language-plaintext highlighter-rouge">\n</code>), es mejor usar la <a href="https://docs.python.org/3/library/re.html#module-re">notación de cadena cruda para patrones de expresiones regulares de Python</a>, de lo contrario, `pytest` mostrará una advertencia de <code class="language-plaintext highlighter-rouge">DeprecationWarning: invalid escape sequence</code>. Al igual que las cadenas de formato se prefijan con `f`, las cadenas crudas se prefijan con `r`. Por ejemplo, en lugar de <code class="language-plaintext highlighter-rouge">"harvard\.edu"</code>, usa <code class="language-plaintext highlighter-rouge">r"harvard\.edu"</code>.</li>
  <li data-marker="*">Ten en cuenta que `re.search`, si se le pasa un patrón con "grupos de captura" (es decir, paréntesis), devuelve un "objeto de coincidencia", según <a href="https://docs.python.org/3/library/re.html#match-objects">docs.python.org/3/library/re.html#match-objects</a>, donde las coincidencias se numeran desde 1 y se pueden acceder individualmente con <code class="language-plaintext highlighter-rouge">group</code>, según <a href="https://docs.python.org/3/library/re.html#re.Match.group">docs.python.org/3/library/re.html#re.Match.group</a>, o colectivamente con <code class="language-plaintext highlighter-rouge">groups</code>, según <a href="https://docs.python.org/3/library/re.html#re.Match.groups">docs.python.org/3/library/re.html#re.Match.groups</a>.</li>
  <li data-marker="*">Ten en cuenta que puedes formatear un número entero con ceros iniciales con el código siguiente:
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="si">{{n:02}}</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>donde, si `n` es un solo dígito, se le agregará un `0` delante, según <a href="https://docs.python.org/3/library/string.html#format-string-syntax">docs.python.org/3/library/string.html#format-string-syntax</a>.</p>
  </li>
</ul></details>
## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta el comando `cd` por sí solo. Deberías ver que el prompt de tu terminal se parezca al siguiente:

    $

Luego, ejecuta el siguiente comando:

    mkdir working

para crear una carpeta llamada `working` en tu espacio de trabajo.

Después, ejecuta el comando:

    cd working

para cambiar al directorio `working`. Ahora deberías ver que el prompt de tu terminal se muestra como `working/ $`. Ahora puedes ejecutar el comando:

    code working.py

para crear un archivo llamado `working.py` donde escribirás tu programa. Asegúrate de ejecutar también el comando:

    code test_working.py

para crear un archivo llamado `test_working.py` donde escribirás las pruebas para tu programa.

## Cómo realizar las pruebas

### Cómo probar `working.py`

Aquí te explicamos cómo probar `working.py` manualmente:

- Ejecuta tu programa con `python working.py`. Asegúrate de que tu programa te solicite un horario ingresando `9 AM to 5 PM` y luego presionando Enter. Tu programa debería imprimir `09:00 to 17:00`.
- Ejecuta tu programa con `python working.py`. Ingresa `9:00 AM to 5:00 PM` y presiona Enter. Una vez más, tu programa debería imprimir `09:00 to 17:00`.
- Ejecuta tu programa con `python working.py`. Asegúrate de que tu programa te solicite un horario. Ingresa `10 PM to 8 AM` y presiona Enter. Tu programa debería imprimir `22:00 to 08:00`.
- Ejecuta tu programa con `python working.py`. Asegúrate de que tu programa te solicite un horario. Ingresa `10:30 PM to 8:50 AM` y presiona Enter. Una vez más, tu programa debería imprimir `22:30 to 08:50`.
- Ejecuta tu programa con `python working.py`. Asegúrate de que tu programa te solicite un horario. Intenta provocar intencionalmente un `ValueError` ingresando `9:60 AM to 5:60 PM` y presionando Enter. Tu programa debería mostrar un error `ValueError`.
- Ejecuta tu programa con `python working.py`. Asegúrate de que tu programa te solicite un horario. Intenta provocar intencionalmente un `ValueError` ingresando `9 AM - 5 PM` y presionando Enter. Tu programa debería mostrar un error `ValueError`.
- Ejecuta tu programa con `python working.py`. Asegúrate de que tu programa te solicite un horario. Intenta provocar intencionalmente un `ValueError` ingresando `09:00 AM - 17:00 PM` y presionando Enter. Tu programa debería mostrar un error `ValueError`.

### Cómo probar `test_working.py`

Para probar tus pruebas, ejecuta `pytest test_working.py`. Intenta utilizar versiones correctas e incorrectas de `working.py` para determinar qué tan bien tus pruebas detectan errores:

- Asegúrate de tener una versión correcta de `working.py`. Ejecuta tus pruebas ejecutando el comando `pytest test_working.py`. `pytest` debería mostrar que todas tus pruebas pasaron.
- Modifica la versión correcta de `working.py`, en particular la función `convert`. Tu programa podría, por ejemplo, no generar un `ValueError` cuando debería hacerlo. Ejecuta tus pruebas ejecutando el comando `pytest test_working.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.
- De manera similar, modifica la versión correcta de `working.py`, cambiando los valores de retorno de `convert`. Por ejemplo, tu programa podría omitir erróneamente los minutos. Ejecuta tus pruebas ejecutando el comando `pytest test_working.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.

Puedes ejecutar el siguiente comando para comprobar tu código utilizando `check50`, un programa que CS50 utiliza para probar tu código cuando haces tu entrega. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/working

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indican que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le ha dado a tu programa, la salida que esperaba y la salida que tu programa ha dado.

## Cómo hacer la entrega

En tu terminal, ejecuta el siguiente comando para hacer la entrega de tu trabajo.

    submit50 cs50/problems/2022/python/working