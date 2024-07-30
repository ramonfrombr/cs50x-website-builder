## Cumpleaños

![captura de pantalla de sitio web de cumpleaños](https://cs50.harvard.edu/x/2024/psets/9/birthdays/birthdays.png)

## Problema a resolver

Crea una aplicación web para llevar un registro de los cumpleaños de tus amigos.

## Empezar

Abre [VS Code](https://cs50.dev/).

Comienza haciendo clic dentro de la ventana del terminal y, a continuación, ejecutando `cd` por sí solo. Deberías encontrar que su "indicación" se asemeja a la siguiente.

    $

Haz clic dentro de esa ventana del terminal y, a continuación, ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/9/birthdays.zip

seguido de Intro para descargar un archivo ZIP llamado `birthdays.zip` en tu espacio de códigos. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, ni ningún otro carácter!

Ahora ejecuta

    unzip birthdays.zip

para crear una carpeta llamada `birthdays`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm birthdays.zip

y responder con "y" seguido de Intro en el aviso para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd birthdays

seguido de Intro para moverte a (es decir, abrir) ese directorio. Tu aviso ahora debería parecerse a lo siguiente.

    birthdays/ $

Si todo fue exitoso, deberías ejecutar

    ls

y deberías ver los siguientes archivos y carpetas:

    app.py  birthdays.db  static/  templates/

Si tienes algún problema, sigue estos mismos pasos de nuevo y observa si puedes determinar dónde te equivocaste.

## Entendimiento

En `app.py`, encontrarás el inicio de una aplicación web Flask. La aplicación tiene una ruta (`/`) que acepta tanto solicitudes `POST` (después del `if`) como solicitudes `GET` (después del `else`). Actualmente, cuando se solicita la ruta `/` a través de `GET`, se procesa la plantilla `index.html`. Cuando se solicita la ruta `/` a través de `POST`, el usuario es redirigido de vuelta a `/` a través de `GET`.

`birthdays.db` es una base de datos SQLite con una tabla, `birthdays`, que tiene cuatro columnas: `id`, `name`, `month` y `day`. Ya hay algunas filas en esta tabla, aunque en última instancia tu aplicación web admitirá la capacidad de insertar filas en esta tabla.

En el directorio `static` hay un archivo `styles.css` que contiene el código CSS para esta aplicación web. No es necesario editar este archivo, ¡aunque puedes hacerlo si lo deseas!

En el directorio `templates` hay un archivo `index.html` que se procesará cuando el usuario vea tu aplicación web.

## Detalles de la implementación

Completa la implementación de una aplicación web que permita a los usuarios almacenar y llevar un registro de los cumpleaños.

- Cuando se solicita la ruta `/` a través de `GET`, tu aplicación web debe mostrar, en una tabla, todas las personas de tu base de datos junto con sus cumpleaños.
 - Primero, en `app.py`, agrega lógica en el manejo de tu solicitud `GET` para consultar la base de datos `birthdays.db` para todos los cumpleaños. Pasa todos esos datos a tu plantilla `index.html`.
 - Luego, en `index.html`, agrega lógica para procesar cada cumpleaños como una fila en la tabla. Cada fila debe tener dos columnas: una columna para el nombre de la persona y otra columna para el cumpleaños de la persona.
- Cuando se solicita la ruta `/` a través de `POST`, tu aplicación web debe agregar un nuevo cumpleaños a tu base de datos y luego volver a procesar la página de índice.
 - Primero, en `index.html`, agrega un formulario HTML. El formulario debe permitir a los usuarios escribir un nombre, un mes de cumpleaños y un día de cumpleaños. Asegúrate de que el formulario se envíe a `/` (su "acción") con un método de `post`.
 - Luego, en `app.py`, agrega lógica en el manejo de tu solicitud `POST` para `INSERTAR` una nueva fila en la tabla `birthdays` basada en los datos proporcionados por el usuario.

Opcionalmente, también puedes:

- Agregar la capacidad de eliminar o editar entradas de cumpleaños.
- ¡Agregar cualquier función adicional que elijas!

## Pistas

### Crea un formulario a través del cual los usuarios pueden enviar cumpleaños

En `index.html`, observa la siguiente tarea pendiente:

    <!-- TODO: Crear un formulario para que los usuarios envíen un nombre, un mes y un día -->

Recuerda que, para crear un formulario, puedes utilizar el elemento HTML `form`. Puedes crear un elemento HTML `form` con las siguientes etiquetas de apertura y cierre:

    <form>
    </form>

Por supuesto, un formulario aún necesita campos de entrada (¡y un botón a través del cual el usuario puede enviar el formulario!). Recuerda que los elementos HTML `input` crean, entre otras cosas, cuadros de entrada dentro de un formulario. Puedes especificar su atributo `type` para permitirles aceptar `text` o `numbers`. También proporciona a los elementos `input` un atributo `name` para que puedas diferenciarlos.

    <form>
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
    </form>

Tu formulario podría beneficiarse de un botón en el que el usuario pudiera hacer clic para enviar sus datos. Agrega un elemento `input` de tipo `submit`, que permitirá al usuario hacer precisamente eso. Si deseas que el botón tenga un texto explicativo, intenta configurar el atributo `value`.

    <form>
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
        <input type="submit" value="Agregar cumpleaños">
    </form>

¿Dónde se enviarán los datos del usuario? ¡Actualmente, a ninguna parte! Recuerda que puedes especificar el atributo `action` de un formulario para dictar qué ruta debe solicitarse después de que se envíe el formulario. Los datos del formulario se enviarán junto con la solicitud resultante. El atributo `method` especifica qué método de solicitud HTTP utilizar al enviar el formulario.

    <form action="/" method="post">
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
        <input type="submit" value="Agregar cumpleaños">
    </form>

Con eso, tu formulario debería ser perfectamente funcional, ¡aunque aún podría mejorarse! Considera agregar valores `placeholder` para arreglar un poco las cosas:

    <form action="/" method="post">
        <input name="name" placeholder="Nombre" type="text">
        <input name="month" placeholder="Mes" type="number">
        <input name="day" placeholder="Día" type="number">
        <input type="submit" value="Agregar cumpleaños">
    </form>

Y considera agregar algo de validación del lado del cliente para garantizar que el usuario coopere con la intención de tu formulario. Por ejemplo, un campo `input` de tipo `number` también puede tener un atributo `min` y `max` especificado, que determinan el valor mínimo y máximo que un usuario puede ingresar.

    <form action="/" method="post">
        <input name="name" placeholder="Nombre" type="text">
        <input name="month" placeholder="Mes" type="number" min="1" max="12">
        <input name="day" placeholder="Día" type="number" min="1" max="31">
        <input type="submit" value="Agregar cumpleaños">
    </form>

### Agrega el envío de datos de un formulario de usuario a la base de datos

En `app.py`, nota el siguiente TODO:

    # TODO: Agrega la entrada del usuario a la base de datos

Recuerda que Flask tiene métodos prácticos para acceder a datos de formulario enviados mediante `POST`. En particular:

    # Accede a datos de formulario
    request.form.get(NAME)

donde `NAME` se refiere al atributo `name` del elemento `input` particular con los datos enviados. Si tus elementos `input` fueron nombrados `name`, `month` y `day`, podrías acceder a sus valores y almacenarlos con los siguientes:

    # Accede a datos de formulario
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

Ahora los valores enviados por el usuario en los elementos de entrada `name`, `month` y `day` están disponibles para ti como variables de Python.

¡El siguiente paso es agregar estos valores a tu base de datos! Gracias a esta línea en particular

    db = SQL("sqlite:///birthdays.db")

`app.py` ya estableció una conexión a `birthdays.db` con el nombre `db`. Ahora puedes ejecutar consultas SQL llamando a `db.execute` con una consulta SQL válida. Si quisieras agregar el cumpleaños de Carter el 1 de enero, podrías ejecutar la siguiente declaración SQL:

    INSERT INTO birthdays (name, month, day) VALUES('Carter', 1, 1);

Configura `app.py` para ejecutar esa misma consulta, pero con marcadores de posición para los valores a insertar, de la siguiente manera:

    # Accede a datos de formulario
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    # Inserta datos en la base de datos
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

¡Y eso debería ser todo! Intenta enviar el formulario, abriendo `birthdays.db` y usando una consulta `SELECT` para ver el contenido de la tabla `birthdays`. Deberías ver los datos del formulario enviado disponibles para ti.

A medida que crees aplicaciones más avanzadas, también querrás agregar _validación de lado del servidor_, es decir, una forma de verificar si los datos del usuario son válidos _antes_ de hacer cualquier otra cosa. Una de las primeras validaciones que podrías hacer es si el usuario envió algún dato. Si intentas recuperar datos de formulario con `request.form.get` cuando el usuario no envió nada, `request.form.get` devolverá una cadena vacía. Puedes verificar este valor en Python de la siguiente manera:

    # Accede a datos de formulario
    name = request.form.get("name")
    if not name:
        return redirect("/")

    month = request.form.get("month")
    if not month:
        return redirect("/")

    day = request.form.get("day")
    if not day:
        return redirect("/")

    # Inserta datos en la base de datos
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
    
Ahora no insertarás una fila hasta que estés seguro de que el usuario haya proporcionado todos los datos que necesitas.

¡Todavía podrían pasar algunas cosas más! ¿Qué pasa si el usuario no proporciona un valor numérico para `month` o `day`? Una forma de comprobarlo es `intentar` convertir el valor a un entero con `int` y, si la conversión falla, redirigir al usuario a la página de inicio.

    # Accede a datos de formulario
    name = request.form.get("name")
    if not name:
        return redirect("/")

    month = request.form.get("month")
    if not month:
        return redirect("/")
    try:
        month = int(month)
    except ValueError:
        return redirect("/")

    day = request.form.get("day")
    if not day:
        return redirect("/")
    try:
        day = int(day)
    except ValueError:
        return redirect("/")

    # Inserta datos en la base de datos
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
    
E incluso si el usuario ha ingresado un número, ¡es mejor verificar que esté en el rango correcto!

    # Accede a datos de formulario
    name = request.form.get("name")
    if not name:
        return redirect("/")

    month = request.form.get("month")
    if not month:
        return redirect("/")
    try:
        month = int(month)
    except ValueError:
        return redirect("/")
    if month < 1 or month > 12:
        return redirect("/")

    day = request.form.get("day")
    if not day:
        return redirect("/")
    try:
        day = int(day)
    except ValueError:
        return redirect("/")
    if day < 1 or day > 31:
        return redirect("/")

    # Inserta datos en la base de datos
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

### Renderizar cumpleaños en `birthdays.db`

Una vez que un usuario pueda enviar cumpleaños y almacenarlos en `birthdays.db`, tu siguiente tarea es asegurarte de que esos cumpleaños se rendericen en `index.html`.

Primero, necesitarás recuperar todos los cumpleaños de `birthdays.db`. Podrías hacerlo con la consulta SQL:

    SELECT * FROM birthdays;

Mira el siguiente TODO en `app.py`:

    # TODO: Muestra las entradas en la base de datos en index.html

Considera la posibilidad de configurar `app.py` para que ejecute esta consulta SQL cada vez que se cargue la página con una solicitud `GET`:

    # Consulta para todos los cumpleaños
    birthdays = db.execute("SELECT * FROM birthdays")

Ahora, todos los cumpleaños en la tabla `birthdays` de `birthdays.db` están disponibles para ti en una variable Python llamada `birthdays`. En particular, los resultados de la consulta SQL se almacenan como una lista de diccionarios. Cada diccionario representa una fila devuelta por la consulta, y cada clave en el diccionario corresponde a un nombre de columna de la tabla `birthdays` (es decir, "nombre", "mes" y "día").

Para renderizar estos cumpleaños en `index.html`, puedes confiar en la función `render_template` de Flask. Puedes especificar que `index.html` debe renderizarse con la variable `birthdays` especificando un argumento de palabra clave, también llamado `birthdays`, y estableciéndolo igual a la variable `birthdays` que acabas de crear.

    # Consulta para todos los cumpleaños
    birthdays = db.execute("SELECT * FROM birthdays")

    # Renderiza la página de cumpleaños
    return render_template("index.html", birthdays=birthdays)

Para ser claros, el nombre en el lado izquierdo del `=`, `birthdays`, es el nombre bajo el cual puedes acceder a los datos de cumpleaños dentro del propio `index.html`.

Ahora que se está renderizando `index.html` con acceso a los datos de los cumpleaños, puedes usar Jinja para renderizar los datos correctamente. Jinja, como Python, puede recorrer los elementos de una lista. Y Jinja, como Python, puede acceder a los elementos de un diccionario mediante sus claves. En este caso, la sintaxis de Jinja para hacerlo es el nombre del diccionario, seguido de un `.`, luego el nombre de la clave para acceder.

    {% for birthday in birthdays %}
        <tr>
            <td></td>
            <td>/</td>
        </tr>
    {% endfor %}

¡Y eso es todo! Intenta recargar la página para ver los cumpleaños renderizados.

### Tutorial

<div class="alert alert-primary" data-alert="primary" role="alert"><p>¡Este video fue grabado cuando el curso todavía usaba CS50 IDE para escribir código. Aunque la interfaz puede parecer diferente de tu espacio de códigos ¡el comportamiento de los dos entornos debería ser muy similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/HXwvj8x1Fcs"></iframe>

<details><summary> ¿No estás seguro de cómo resolverlo?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/lVwv4o8vmvI"></iframe></details>

### Pruebas

¡No hay `check50` para este conjunto de problemas! Pero asegúrate de probar tu aplicación web agregando algunos cumpleaños y asegurándote de que los datos aparezcan en tu tabla como se esperaba.

Ejecuta `flask run` en tu terminal mientras estás en tu directorio `birthdays` para iniciar un servidor web que ejecute tu aplicación Flask.

## Cómo Enviar

    submit50 cs50/problems/2024/x/birthdays

