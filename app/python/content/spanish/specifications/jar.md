

# Frasco de galletas

![Cookie Monster](giphy1.gif)

Fuente: Sesame Street

Supongamos que te gustaría implementar un [frasco de galletas](https://es.wikipedia.org/wiki/Frasco_de_galletas) en el cual almacenar galletas. En un archivo llamado `jar.py`, implementa una `clase` llamada `Jar` con estos métodos:

- `__init__` debería inicializar un frasco de galletas con la capacidad dada, que representa el número máximo de galletas que pueden caber en el frasco. Sin embargo, si `capacity` no es un número entero no negativo, `__init__` debería lanzar un `ValueError`.
- `__str__` debería devolver una cadena de caracteres con \\(n\\) `🍪`, donde \\(n\\) es el número de galletas en el frasco de galletas. Por ejemplo, si hay 3 galletas en el frasco de galletas, entonces `str` debería devolver `"🍪🍪🍪"`.
- `deposit` debería agregar `n` galletas al frasco. Sin embargo, si agregar tantas galletas excedería la capacidad del frasco, `deposit` debería lanzar un `ValueError`.
- `withdraw` debería remover `n` galletas del frasco de galletas. Nom nom nom. Sin embargo, si no hay tantas galletas en el frasco, `withdraw` debería lanzar un `ValueError`.
- `capacity` debería devolver la capacidad del frasco de galletas.
- `size` debería devolver el número de galletas que se encuentran actualmente en el frasco de galletas, inicialmente `0`.

Estructura tu `clase` de la siguiente manera. No puedes cambiar los parámetros de estos métodos, pero puedes agregar tus propios métodos.

    class Jar:
        def __init__(self, capacity=12):
            ...

        def __str__(self):
            ...

        def deposit(self, n):
            ...

        def withdraw(self, n):
            ...

        @property
        def capacity(self):
            ...

        @property
        def size(self):
            ...

Ya sea antes o después de implementar `jar.py`, adicionalmente implementa, en un archivo llamado `test_jar.py`, **cuatro o más** funciones que prueben exhaustivamente tu implementación de `Jar`, cada una de las cuales debería comenzar con `test_`, para que puedas ejecutar tus pruebas con:

    pytest test_jar.py

Ten en cuenta que no es tan fácil probar los métodos de instancia como lo es probar solo las funciones, ya que los métodos de instancia a veces manipulan el mismo "estado" (es decir, variables de instancia). Para probar un método (por ejemplo, `withdraw`), podría ser necesario llamar a otro método primero (por ejemplo, `deposit`). Pero el método que llames primero puede que no sea correcto en sí mismo.

Por lo tanto, los programadores a veces simulan (es decir, falsifican) el estado al probar los métodos, como con la propia [biblioteca de objetos falsos](https://docs.python.org/3/library/unittest.mock.html) de Python, para que puedas llamar solo al método que deseas pero modificar el estado subyacente primero, sin llamar al otro método para hacerlo.

Sin embargo, por simplicidad, no es necesario falsificar ningún estado. ¡Implementa tus pruebas de la manera habitual!

Sugerencias

    from jar import Jar


    def test_init():
        ...


    def test_str():
        jar = Jar()
        assert str(jar) == ""
        jar.deposit(1)
        assert str(jar) == "🍪"
        jar.deposit(11)
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


    def test_deposit():
        ...


    def test_withdraw():
        ...

## Demo

Eres bienvenido, pero no es obligatorio, implementar una función `main`, ¡así que esto es todo lo que podemos mostrar!

![Cookie Monster](giphy2.gif)

Fuente: Sesame Street

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu terminal se parece a lo siguiente:

    $

A continuación, ejecuta

    mkdir jar

para crear una carpeta llamada `jar` en tu entorno de desarrollo.

Luego ejecuta

    cd jar

para cambiar al directorio de esa carpeta. Ahora deberías ver el indicador de tu terminal como `jar/ $`. Ahora puedes ejecutar

    code jar.py

para crear un archivo llamado `jar.py` donde escribirás tu programa. También puedes ejecutar

    code test_jar.py

para crear un archivo llamado `test_jar.py` donde puedes escribir pruebas para tu programa.

## Cómo probar

Aquí te mostramos cómo probar tu código de forma manual:

- Abre tu archivo `test_jar.py` e importa tu clase `Jar` con `from jar import Jar`. Crea una función llamada `test_init`, en la cual creas una nueva instancia de `Jar` con `jar = Jar()`. Hacer un `assert` de que este frasco tiene la capacidad que debería, luego ejecuta tus pruebas con `pytest test_jar.py`.
- Agrega otra función a tu archivo `test_jar.py` llamada `test_str`. En `test_str`, crea una nueva instancia de tu clase `Jar` y `deposita` algunas galletas. Asegúrate de que `str(jar)` imprime la cantidad correcta de galletas que se han `depositado`, luego ejecuta tus pruebas con `pytest test_jar.py`.
- Agrega otra función a tu archivo `test_jar.py` llamada `test_deposit`. En `test_deposit`, crea una nueva instancia de tu clase `Jar` y `deposita` algunas galletas. Asegúrate de que el atributo `size` del frasco sea tan grande como el número de galletas que se han `depositado`. Además, asegúrate de que si depositas más galletas de las que puede contener el frasco, `deposit` debe lanzar un `ValueError`. Ejecuta tus pruebas con `pytest test_jar.py`.
- Agrega otra función a tu archivo `test_jar.py` llamada `test_withdraw`. En `test_withdraw`, crea una nueva instancia de tu clase `Jar` y primero `deposita` algunas galletas. Asegúrate de que `withdraw` del frasco deja el número correcto de galletas en el atributo `size`. Además, asegúrate de que si retiras más galletas de las que hay en el frasco, `withdraw` debe lanzar un `ValueError`. Ejecuta tus pruebas con `pytest test_jar.py`.

Puedes ejecutar el siguiente comando para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/jar

¡Las caritas sonrientes en verde significan que tu programa ha pasado una prueba! Las caritas tristes en rojo indicarán que tu programa generó algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le pasó a tu programa, la salida esperada y la salida real de tu programa.

## Cómo enviar

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/jar