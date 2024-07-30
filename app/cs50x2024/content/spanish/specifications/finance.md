# C$50 Finanzas

Implementa un sitio web a través del cual los usuarios pueden "comprar" y "vender" acciones, como el siguiente.

![C$50 Finanzas](https://cs50.harvard.edu/x/2024/psets/9/finance/finance_2024.png)

## Antecedentes

Si no estás seguro de lo que significa comprar y vender acciones (es decir, acciones de una empresa), dirígete [aquí](https://www.investopedia.com/articles/basics/06/invest1000.asp) para un tutorial.

Estás a punto de implementar C$50 Finance, una aplicación web a través de la cual puedes administrar carteras de acciones. Esta herramienta no solo te permitirá consultar los precios reales de las acciones reales y los valores de las carteras, sino que también te permitirá comprar (bien, "comprar") y vender (bien, "vender") acciones consultando los precios de las acciones.

De hecho, existen herramientas (una se conoce como IEX) que te permiten descargar cotizaciones de acciones a través de su API (interfaz de programación de aplicaciones) utilizando URL como `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Observa cómo el símbolo de Netflix (NFLX) está incrustado en esta URL; así es como IEX sabe cuyos datos devolver. Ese enlace en realidad no devolverá ningún dato porque IEX requiere que utilices una clave API, pero si lo hiciera, verías una respuesta en formato JSON (JavaScript Object Notation) como esta:

    {
      "avgTotalVolume":6787785,
      "calculationPrice":"tops",
      "change":1.46,
      "changePercent":0.00336,
      "close":null,
      "closeSource":"official",
      "closeTime":null,
      "companyName":"Netflix Inc.",
      "currency":"USD",
      "delayedPrice":null,
      "delayedPriceTime":null,
      "extendedChange":null,
      "extendedChangePercent":null,
      "extendedPrice":null,
      "extendedPriceTime":null,
      "high":null,
      "highSource":"IEX real time price",
      "highTime":1699626600947,
      "iexAskPrice":460.87,
      "iexAskSize":123,
      "iexBidPrice":435,
      "iexBidSize":100,
      "iexClose":436.61,
      "iexCloseTime":1699626704609,
      "iexLastUpdated":1699626704609,
      "iexMarketPercent":0.00864679844447232,
      "iexOpen":437.37,
      "iexOpenTime":1699626600859,
      "iexRealtimePrice":436.61,
      "iexRealtimeSize":5,
      "iexVolume":965,
      "lastTradeTime":1699626704609,
      "latestPrice":436.61,
      "latestSource":"IEX real time price",
      "latestTime":"9:31:44 AM",
      "latestUpdate":1699626704609,
      "latestVolume":null,
      "low":null,
      "lowSource":"IEX real time price",
      "lowTime":1699626634509,
      "marketCap":192892118443,
      "oddLotDelayedPrice":null,
      "oddLotDelayedPriceTime":null,
      "open":null,
      "openTime":null,
      "openSource":"official",
      "peRatio":43.57,
      "previousClose":435.15,
      "previousVolume":2735507,
      "primaryExchange":"NASDAQ",
      "symbol":"NFLX",
      "volume":null,
      "week52High":485,
      "week52Low":271.56,
      "ytdChange":0.4790450244167119,
      "isUSMarketOpen":true
    }

Observa cómo, entre las llaves, hay una lista separada por comas de pares clave-valor, con dos puntos que separan cada clave de su valor. Vamos a hacer algo muy similar con Yahoo Finance.

¡Ahora dirijamos nuestra atención a obtener el código de distribución de este problema!

## Cómo empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí mismo. Deberías encontrar que el indicador de la ventana de comandos se asemeja a lo siguiente:

    $

A continuación, ejecuta

    wget https://cdn.cs50.net/2024/x/psets/9/finance.zip

para descargar un ZIP llamado `finance.zip` en tu espacio de códigos.

Luego ejecuta

    unzip finance.zip

para crear una carpeta llamada `finance`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm finance.zip

y responder con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd finance

seguido de Enter para colocarte en (es decir, abrir) ese directorio. Tu indicador ahora debería parecerse al siguiente.

    finance/ $

Ejecuta `ls` por sí mismo, y deberías ver algunos archivos y carpetas:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

¡Si te encuentras con algún problema, sigue estos mismos pasos nuevamente y ve si puedes determinar dónde te equivocaste!

### Ejecución

Inicia el servidor web incorporado de Flask (dentro de `finance/`):

    $ flask run

Visita la URL generada por `flask` para ver el código de distribución en acción. Sin embargo, ¡no podrás iniciar sesión ni registrarte, todavía!

Dentro de `finance/`, ejecuta `sqlite3 finance.db` para abrir `finance.db` con `sqlite3`. Si ejecutas `.schema` en el aviso de SQLite, observa cómo `finance.db` viene con una tabla llamada `users`. Echa un vistazo a su estructura (es decir, esquema). Observa cómo, de forma predeterminada, los nuevos usuarios recibirán $10,000 en efectivo. Pero si ejecutas `SELECT * FROM users;`, no hay (¡todavía!) usuarios (es decir, filas) en los que navegar.

Otra forma de ver `finance.db` es con un programa llamado phpLiteAdmin. Haz clic en `finance.db` en el explorador de archivos de tu espacio de códigos, luego haz clic en el enlace que se muestra debajo del texto "Por favor, visita el siguiente enlace para autorizar la vista previa de GitHub". Deberías ver información sobre la base de datos en sí, así como una tabla, `users`, tal como la viste en el aviso de `sqlite3` con `.schema`.

### Entendiendo

#### `app.py`

Abre `app.py`. Al principio del archivo hay una serie de importaciones, entre ellas el módulo SQL de CS50 y algunas funciones auxiliares. Ya hablaremos de ellas más adelante.

Después de configurar [Flask](https://flask.pocoo.org/), observa cómo este archivo desactiva el almacenamiento en caché de las respuestas (siempre que estés en modo de depuración, que es el predeterminado en tu espacio de códigos de code50), para que no hagas un cambio en algún archivo pero tu navegador no lo detecte. Observa a continuación cómo configura [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) con un "filtro" personalizado, `usd`, una función (definida en `helpers.py`) que facilitará el formateo de valores como dólares estadounidenses (USD). A continuación, configura Flask para que almacene las [sesiones](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) en el sistema de archivos local (es decir, el disco) en lugar de almacenarlas dentro de cookies (firmadas digitalmente), que es el valor predeterminado de Flask. A continuación, el archivo configura el módulo SQL de CS50 para que utilice `finance.db`.

A continuación, hay un montón de rutas, de las cuales solo dos están completamente implementadas: `login` y `logout`. Lee primero la implementación de `login`. Observa cómo utiliza `db.execute` (de la biblioteca de CS50) para consultar `finance.db`. Y observa cómo utiliza `check_password_hash` para comparar hashes de contraseñas de usuarios. Observa también cómo `login` "recuerda" que un usuario ha iniciado sesión almacenando su `user_id`, un ENTERO, en `session`. De esa manera, cualquiera de las rutas de este archivo puede comprobar qué usuario, si es que hay alguno, ha iniciado sesión. Por último, observa cómo una vez que el usuario ha iniciado sesión correctamente, `login` redireccionará a `"/"`, llevando al usuario a su página de inicio. Mientras tanto, observa cómo `logout` simplemente borra `session`, cerrando efectivamente la sesión de un usuario.

Observa cómo la mayoría de las rutas están "decoradas" con `@login_required` (una función también definida en `helpers.py`). Ese decorador asegura que, si un usuario intenta visitar cualquiera de esas rutas, será redirigido primero a `login` para iniciar sesión.

Observa también cómo la mayoría de las rutas admiten GET y POST. Aun así, la mayoría de ellas (¡por ahora!) simplemente devuelven una "disculpa", ya que aún no se han implementado.

#### `helpers.py`

A continuación, echa un vistazo a `helpers.py`. Ahí está la implementación de `apology`. Observa cómo finalmente renderiza una plantilla, `apology.html`. También sucede que define dentro de sí misma otra función, `escape`, que simplemente usa para reemplazar caracteres especiales en disculpas. Al definir `escape` dentro de `apology`, hemos limitado este primero al segundo; ninguna otra función podrá (o necesitará) llamarlo.

Lo siguiente en el archivo es `login_required`. No te preocupes si esto es un poco críptico, pero si alguna vez te has preguntado cómo una función puede devolver otra función, ¡aquí tienes un ejemplo!

A continuación está `lookup`, una función que, dado un `symbol` (por ejemplo, NFLX), devuelve una cotización de acciones para una empresa en forma de `dict` con dos claves: `price`, cuyo valor es un `float`; y `symbol`, cuyo valor es una `str`, una versión canónica (en mayúsculas) del símbolo de una acción, independientemente de cómo se haya escrito en mayúsculas o minúsculas cuando se pasó a `lookup`.

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Ten en cuenta. Si empezaste este problema en 2023, ten en cuenta que <code class="language-plaintext highlighter-rouge">lookup</code> ya no devuelve una clave de <code class="language-plaintext highlighter-rouge">name</code>, así que asegúrate de eliminarla de cualquier consulta que la espere. No es necesario mostrar ningún nombre en ninguna página.</p></div>

Lo último en el archivo es `usd`, una función corta que simplemente formatea un `float` como USD (por ejemplo, `1234.56` se formatea como `$1,234.56`).

#### `requirements.txt`

A continuación, echa un vistazo rápido a `requirements.txt`. Ese archivo simplemente prescribe los paquetes de los que dependerá esta aplicación.

#### `static/`

Echa un vistazo también a `static/`, dentro del cual está `styles.css`. Ahí es donde vive algún CSS inicial. Puedes modificarlo como mejor te parezca.

#### `templates/`

Ahora mira en `templates/`. En `login.html` hay, esencialmente, solo un formulario HTML, estilizado con [Bootstrap](https://getbootstrap.com/). En `apology.html`, mientras tanto, hay una plantilla para una disculpa. Recuerda que `apology` en `helpers.py` tomó dos argumentos: `message`, que se pasó a `render_template` como el valor de `bottom`, y, opcionalmente, `code`, que se pasó a `render_template` como el valor de `top`. ¡Observa en `apology.html` cómo se utilizan esos valores finalmente! Y [aquí tienes por qué](https://github.com/jacebrowning/memegen) 0:-)

Lo último es `layout.html`. Es un poco más grande de lo habitual, pero eso es principalmente porque viene con una "barra de navegación" elegante y optimizada para móviles, también basada en Bootstrap. Observa cómo define un bloque, `main`, dentro del cual irán las plantillas (incluyendo `apology.html` y `login.html`). También incluye soporte para el [message flashing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing) de Flask para que puedas transmitir mensajes de una ruta a otra para que el usuario los vea.

## Especificaciones

### `register`

Completa la implementación de `register` de tal manera que permita a un usuario registrarse para obtener una cuenta a través de un formulario.

- Requiere que un usuario ingrese un nombre de usuario, implementado como un campo de texto cuyo `name` es `username`. Muestra una disculpa si la entrada del usuario está en blanco o si el nombre de usuario ya existe.
  - Ten en cuenta que [`cs50.SQL.execute`](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL) lanzará una excepción `ValueError` si intentas `INSERT` un nombre de usuario duplicado porque hemos creado un `UNIQUE INDEX` en `users.username`. Asegúrate, entonces, de usar `try` y `except` para determinar si el nombre de usuario ya existe.
- Requiere que un usuario ingrese una contraseña, implementada como un campo de texto cuyo `name` es `password`, y luego esa misma contraseña nuevamente, implementada como un campo de texto cuyo `name` es `confirmation`. Muestra una disculpa si alguna de las entradas está en blanco o si las contraseñas no coinciden.
- Envía la entrada del usuario a través de `POST` a `/register`.
- `INSERT` el nuevo usuario en `users`, almacenando un hash de la contraseña del usuario, no la contraseña en sí. Hash la contraseña del usuario con [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.security.generate_password_hash) Es probable que quieras crear una nueva plantilla (por ejemplo, `register.html`) que sea muy similar a `login.html`.

Una vez que hayas implementado correctamente `register`, ¡deberías poder registrarte para obtener una cuenta e iniciar sesión (ya que `login` y `logout` ya funcionan)! Y deberías poder ver tus filas a través de phpLiteAdmin o `sqlite3`.

### `quote`

Completa la implementación de `quote` de tal manera que permita a un usuario consultar el precio actual de una acción.

- Requiere que un usuario ingrese un símbolo de una acción, implementado como un campo de texto cuyo `name` es `symbol`.
- Envía la entrada del usuario a través de `POST` a `/quote`.
- Es probable que quieras crear dos nuevas plantillas (por ejemplo, `quote.html` y `quoted.html`). Cuando un usuario visita `/quote` a través de GET, renderiza una de esas plantillas, dentro de la cual debe haber un formulario HTML que se envíe a `/quote` a través de POST. En respuesta a un POST, `quote` puede renderizar esa segunda plantilla, incrustando dentro de ella uno o más valores de `lookup`.

### `buy`

Completa la implementación de `buy` para que permita a un usuario comprar acciones.

- Solicita que un usuario proporcione el símbolo de una acción, implementado como un campo de texto cuyo `name` es `symbol`. Muestra un mensaje de disculpa si la entrada está en blanco o si el símbolo no existe (según el valor de retorno de `lookup`).
- Solicita que un usuario proporcione el número de acciones, implementado como un campo de texto cuyo `name` es `shares`. Muestra un mensaje de disculpa si la entrada no es un entero positivo.
- Envía la entrada del usuario mediante `POST` a `/buy`.
- Una vez completado, redirige al usuario a la página de inicio.
- Lo más probable es que quieras llamar a `lookup` para obtener el precio actual de una acción.
- Lo más probable es que quieras `SELECT` la cantidad de dinero en efectivo que el usuario tiene actualmente en `users`.
- Agrega una o más nuevas tablas a `finance.db` mediante las cuales hacer un seguimiento de la compra. Almacena suficiente información para saber quién compró qué, a qué precio y cuándo.
  - Utiliza los tipos de SQLite adecuados.
  - Define índices `UNIQUE` en cualquier campo que deba ser único.
  - Define índices (no `UNIQUE`) para cualquier campo a través del cual realizarás búsquedas (como mediante `SELECT` con `WHERE`).
- Muestra un mensaje de disculpa, sin completar una compra, si el usuario no puede pagar el número de acciones al precio actual.
- No tienes que preocuparte por las condiciones de carrera (o usar transacciones).

Una vez que hayas implementado `buy` correctamente, deberías poder ver las compras de los usuarios en tus nuevas tablas mediante phpLiteAdmin o `sqlite3`.

### `index`

Completa la implementación de `index` para que muestre una tabla HTML que resuma, para el usuario actualmente conectado, qué acciones posee, el número de acciones poseídas, el precio actual de cada acción y el valor total de cada participación (es decir, acciones multiplicado por precio). También muestra el saldo de efectivo actual del usuario junto con un gran total (es decir, el valor total de las acciones más el efectivo).

- Lo más probable es que quieras ejecutar varios `SELECT`. Dependiendo de cómo implementes tus tablas, es posible que encuentres [GROUP BY](https://www.google.com/search?q=SQLite+GROUP+BY,) [HAVING](https://www.google.com/search?q=SQLite+HAVING,) [SUM](https://www.google.com/search?q=SQLite+SUM,) y/o [WHERE](https://www.google.com/search?q=SQLite+WHERE) de interés.
- Lo más probable es que quieras llamar a `lookup` para cada acción.

### `sell`

Completa la implementación de `sell` para que permita a un usuario vender acciones de una acción (que posea).

- Solicita que un usuario proporcione el símbolo de una acción, implementado como un menú `select` cuyo `name` es `symbol`. Muestra un mensaje de disculpa si el usuario no selecciona una acción o si (de alguna manera, una vez enviado) el usuario no posee ninguna acción de esa acción.
- Solicita que un usuario proporcione el número de acciones, implementado como un campo de texto cuyo `name` es `shares`. Muestra un mensaje de disculpa si la entrada no es un entero positivo o si el usuario no posee tantas acciones de la acción.
- Envía la entrada del usuario mediante `POST` a `/sell`.
- Una vez completado, redirige al usuario a la página de inicio.
- No tienes que preocuparte por las condiciones de carrera (o usar transacciones).

### `history`

Completa la implementación de `history` para que muestre una tabla HTML que resuma todas las transacciones de un usuario, enumerando fila por fila cada compra y cada venta.

- Para cada fila, deja en claro si una acción se compró o vendió e incluye el símbolo de la acción, el precio (de compra o venta), el número de acciones compradas o vendidas y la fecha y hora en que ocurrió la transacción.
- Es posible que debas alterar la tabla que creaste para `buy` o complementarla con una tabla adicional. Intenta minimizar las redundancias.

### Toque personal

Implementa al menos un toque personal de tu elección:

- Permite a los usuarios cambiar sus contraseñas.
- Permite a los usuarios agregar dinero en efectivo adicional a su cuenta.
- Permite a los usuarios comprar más acciones o vender acciones de las acciones que ya poseen mediante el propio `index`, sin tener que escribir los símbolos de las acciones manualmente.
- Implementa alguna otra función de alcance comparable.

## Guía paso a paso

<div class="alert alert-info" data-alert="info" role="alert"><p>Ten en cuenta que Brian menciona que <code class="language-plaintext highlighter-rouge">lookup</code> devolverá el nombre de la acción. Según lo anterior, ahora solo devuelve el precio y el símbolo.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Pruebas

Asegúrate de probar tu aplicación web manualmente, como

- registrando un nuevo usuario y verificando que su página de portafolio se carga con la información correcta,
- solicitando una cotización utilizando un símbolo de acción válido,
- comprando una acción varias veces, verificando que el portafolio muestre los totales correctos,
- vendiendo todas o algunas de una acción, verificando nuevamente el portafolio y
- verificando que tu página de historial muestre todas las transacciones para tu usuario registrado.

También prueba un uso inesperado, como

- ingresando cadenas alfabéticas en formularios cuando solo se esperan números,
- ingresando cero o números negativos en formularios cuando solo se esperan números positivos,
- ingresando valores de punto flotante en formularios cuando solo se esperan enteros,
- tratando de gastar más dinero del que tiene un usuario,
- tratando de vender más acciones de las que posee un usuario,
- ingresando un símbolo de acción no válido y
- incluyendo caracteres potencialmente peligrosos como `'` y `;` en las consultas SQL.

También puedes verificar la validez de tu HTML haciendo clic en el botón **I ♥ VALIDATOR** en el pie de página de cada una de tus páginas, que PUBLICARÁ tu HTML en [validator.w3.org](https://validator.w3.org/).

Una vez satisfecho, para probar tu código con `check50`, ejecuta lo siguiente.

    check50 cs50/problems/2024/x/finance

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Ten en cuenta que <code class="language-plaintext highlighter-rouge">check50</code> probará todo tu programa en su conjunto. Si lo ejecutas <strong>antes</strong> de completar todas las funciones requeridas, puede reportar errores en las funciones que en realidad son correctas pero dependen de otras funciones.</p></div>

## Estilo

    style50 app.py

## Solución de los asesores

Puedes personalizar el estilo de tu aplicación como quieras, ¡pero así es como se ve la solución de los asesores!

[https://finance.cs50.net/](https://finance.cs50.net/)

No dudes en registrarte para crear una cuenta y probarla. **No** uses una contraseña que uses en otros sitios.

Es **razonable** revisar los archivos HTML y CSS de los asesores.

## Sugerencias

- Para dar formato al valor como valor en dólares estadounidenses (con centavos listados con dos decimales), puedes usar el filtro `usd` en tus plantillas Jinja (imprime valores como `{{ valor | usd }}` en lugar de `{{ valor }}`.
- Dentro de `cs50.SQL` hay un método `execute` cuyo primer argumento debe ser una `str` de SQL. Si esa `str` contiene parámetros de interrogación a los que se les deben enlazar valores, esos valores se pueden proporcionar como parámetros con nombre adicionales a `execute`. Mira la implementación de `login` para ver un ejemplo de eso. El valor de retorno de `execute` es el siguiente:
  - Si `str` es `SELECT`, entonces `execute` devuelve una `list` de cero o más objetos `dict`, dentro de los cuales hay claves y valores que representan los campos y celdas de una tabla, respectivamente.
  - Si `str` es un `INSERT` y la tabla en la que se insertaron los datos contiene una `PRIMARY KEY` de autoincremento, entonces `execute` devuelve el valor de la clave principal de la fila insertada recientemente.
  - Si `str` es un `DELETE` o un `UPDATE`, entonces `execute` devuelve el número de filas eliminadas o actualizadas por `str`.
- Recuerda que `cs50.SQL` registrará en tu terminal cualquier consulta que ejecutes a través de `execute` (para que puedas confirmar si son como las esperabas).
- Asegúrate de utilizar parámetros enlazados a signos de interrogación (es decir, un [paramstyle](https://www.python.org/dev/peps/pep-0249/#paramstyle) de `named`) al llamar al método `execute` de CS50, como `WHERE ?`. **No** uses cadenas f, [`format`](https://docs.python.org/3.6/library/functions.html#format,) o `+` (es decir, concatenación), para evitar el riesgo de un ataque de inyección SQL.
- Si (y solo si) ya te sientes cómodo con SQL, puedes utilizar [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) o [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org/) (es decir, [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/index.html)) en lugar de `cs50.SQL`.
- Puedes agregar archivos estáticos adicionales a `static/`.
- Lo más probable es que desees consultar la [documentación de Jinja](https://jinja.palletsprojects.com/en/3.1.x/) al implementar tus plantillas.
- Es **razonable** pedir a otros que prueben (e intenten activar errores) tu sitio.
- Puedes modificar lo estético de los sitios, como a través de:
  - [bootswatch.com](https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/), y/o
  - [memegen.link](https://memegen.link/).
- ¡Te puede resultar útil la [documentación Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) y la [documentación de Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) !

## Preguntas frecuentes

### ImportError: No module named ‘application’

Por defecto, `flask` busca un archivo llamado `app.py` en tu directorio de trabajo actual (porque hemos configurado el valor de `FLASK_APP`, una variable de entorno, como `app.py`). ¡Si aparece este error, lo más probable es que hayas ejecutado `flask` en el directorio incorrecto!

### OSError: \[Errno 98\] Address already in use

Si, al ejecutar `flask`, ves este error, lo más probable es que (todavía) tengas `flask` ejecutándose en otra pestaña. Asegúrate de eliminar ese otro proceso, como con ctrl-c, antes de iniciar `flask` nuevamente. Si no tienes ninguna otra pestaña de este tipo, ejecuta `fuser -k 8080/tcp` para eliminar cualquier proceso que (todavía) esté escuchando en el puerto TCP 8080.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2024/x/finance

<div class="alert alert-danger" data-alert="danger" role="alert"><h3 id="why-does-my-submission-pass-check50-but-shows-no-results-in-my-gradebook-after-running-submit50">¿Por qué mi envío pasa check50, pero muestra “No hay resultados” en mi libreta de calificaciones después de ejecutar submit50?</h3>

<p>En algunos casos, es posible que <code class="language-plaintext highlighter-rouge">submit50</code> no califique la tarea debido a (1) formato inconsistente en tu archivo <code class="language-plaintext highlighter-rouge">app.py</code> y/o (2) archivos adicionales innecesarios que se envían con el conjunto de problemas. Para solucionar estos problemas, ejecuta <code class="language-plaintext highlighter-rouge">black app.py</code> en la carpeta <code class="language-plaintext highlighter-rouge">finance</code>. Resuelve cualquier problema que se revele. Luego, examina el contenido de tu carpeta <code class="language-plaintext highlighter-rouge">finance</code>. Elimina archivos extraños, como sesiones flask u otros archivos que no formen parte de tu implementación del conjunto de problemas. Además, ejecuta <code class="language-plaintext highlighter-rouge">check50</code> nuevamente para asegurarte de que tu envío aún funciona. Finalmente, vuelve a ejecutar el comando <code class="language-plaintext highlighter-rouge">submit50</code> anterior. Tu resultado aparecerá en tu <a href="https://cs50.me/cs50x">Libreta de calificaciones</a> en unos minutos.</p>

<p>Ten en cuenta que si hay una puntuación numérica junto a tu envío financiero en el área de <code class="language-plaintext highlighter-rouge">envíos</code> de tu <a href="https://cs50.me/cs50x"> Libreta de calificaciones</a>, el procedimiento descrito anteriormente no se aplica a ti. Probablemente, no has cumplido completamente con los requisitos del conjunto de problemas y debes confiar en <code class="language-plaintext highlighter-rouge">check50</code> para obtener pistas sobre el trabajo pendiente.</p></div>

