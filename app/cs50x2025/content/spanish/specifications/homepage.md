## Página de inicio

Crea una página de inicio sencilla usando HTML, CSS y JavaScript.

## Antecedentes

Internet ha permitido cosas increíbles: podemos usar un motor de búsqueda para investigar cualquier cosa imaginable, comunicarnos con amigos y familiares en todo el mundo, jugar juegos, tomar cursos y mucho más. Pero resulta que casi todas las páginas que podemos visitar están construidas sobre tres lenguajes principales, cada uno de los cuales tiene un propósito ligeramente diferente:

1. HTML, o _HyperText Markup Language_, que se utiliza para describir el contenido de los sitios web;
2. CSS, _Cascading Style Sheets_, que se utiliza para describir la estética de los sitios web; y
3. JavaScript, que se utiliza para hacer que los sitios web sean interactivos y dinámicos.

Crea una página de inicio sencilla que te presente, tu pasatiempo favorito o actividad extracurricular, o cualquier otra cosa que te interese.

## Primeros pasos

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías encontrar que el indicador de la ventana de tu terminal se asemeja al siguiente:

    $

A continuación, ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/8/homepage.zip

para descargar un ZIP llamado `homepage.zip` en tu espacio de códigos.

A continuación, ejecuta

    unzip homepage.zip

para crear una carpeta llamada `homepage`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm homepage.zip

y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd homepage

seguido de Enter para moverte (es decir, abrir) ese directorio. Tu indicador ahora debería parecerse al siguiente.

    homepage/ $

Ejecuta `ls` por sí solo, y deberías ver algunos archivos:

    index.html  styles.css

Si tienes algún problema, sigue estos mismos pasos nuevamente y ¡mira si puedes determinar dónde te equivocaste! Puedes iniciar inmediatamente un servidor para ver tu sitio ejecutando

    http-server

en la ventana de terminal. Luego, haz clic con el comando (si estás en Mac) o haz clic con el control (si estás en PC) en el primer enlace que aparezca:

    http-server en ejecución en LINK

Donde LINK es la dirección de tu servidor.

## Especificación

Implementa en tu directorio `homepage` un sitio web que debe:

- Contener al menos cuatro páginas `.html` diferentes, al menos una de las cuales es `index.html` (la página principal de tu sitio web), y debería ser posible acceder a cualquier página de tu sitio web desde cualquier otra página siguiendo uno o más hipervínculos.
- Usar al menos diez (10) etiquetas HTML distintas además de `<html>`, `<head>`, `<body>` y `<title>`. ¡Utilizar una etiqueta (por ejemplo, `<p>`) varias veces todavía cuenta como solo una (1) de esas diez!
- Integrar una o más funciones de Bootstrap en tu sitio. Bootstrap es una biblioteca popular (que viene con muchas clases CSS y más) a través de la cual puedes embellecer tu sitio. Consulta la [documentación de Bootstrap](https://getbootstrap.com/docs/5.2/) para comenzar. En particular, puedes encontrar interesantes algunos de los [componentes de Bootstrap](https://getbootstrap.com/docs/5.2/components/). Para agregar Bootstrap a tu sitio, basta con incluir

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

en la `<head>` de tus páginas, debajo de la cual también puedes incluir

        <link href="styles.css" rel="stylesheet">

para vincular tu propio CSS.

- Tener al menos un archivo de hoja de estilo de tu propia creación, `styles.css`, que utilice al menos cinco (5) selectores CSS diferentes (por ejemplo, etiqueta (`example`), clase (`.example`) o ID (`#example`)), y dentro del cual utilices un total de al menos cinco (5) propiedades CSS diferentes, como `font-size` o `margin`; y
- Integrar una o más funciones de JavaScript en tu sitio para que sea más interactivo. Por ejemplo, puedes usar JavaScript para agregar alertas, para tener un efecto a un intervalo recurrente o para agregar interactividad a botones, menús desplegables o formularios. ¡Siéntete libre de ser creativo!
- Asegúrate de que tu sitio se vea bien en los navegadores tanto en dispositivos móviles como en laptops y computadoras de escritorio.

También debes crear un archivo de texto, `specification.txt`, que enumere las 10 etiquetas HTML y las 5 propiedades CSS que has utilizado, así como una breve descripción (de una oración) de cómo elegiste utilizar JavaScript y Bootstrap.

## Pruebas

Si quieres ver cómo se ve tu sitio mientras trabajas en él, puedes ejecutar `http-server`. Haz clic con el comando o el control en el primer enlace presentado por http-server, que debería abrir tu página web en una nueva pestaña. A continuación, deberías poder actualizar la pestaña que contiene tu página web para ver tus últimos cambios.

Recuerda también que al abrir las herramientas para desarrolladores en Google Chrome, puedes _simular_ visitar tu página en un dispositivo móvil haciendo clic en el ícono con forma de teléfono a la izquierda de **Elementos** en la ventana de herramientas para desarrolladores, o, una vez que la pestaña Herramientas para desarrolladores ha abierto, escribiendo `Ctrl` + `Shift` + `M` en una PC o `Cmd` + `Shift` + `M` en una Mac, ¡en lugar de tener que visitar tu sitio en un dispositivo móvil por separado!

## Evaluación

¡No hay `check50` para esta tarea! En cambio, la corrección de tu sitio se evaluará en función de si cumples con los requisitos de la especificación como se describe anteriormente, y si tu HTML está bien formado y es válido. Para asegurarte de que tus páginas lo estén, puedes utilizar este [Servicio de validación de marcado](https://validator.w3.org/#validate_by_input), copiando y pegando tu HTML directamente en el cuadro de texto proporcionado. ¡Ten cuidado de eliminar cualquier advertencia o error sugerido por el validador antes de enviar!

Considera también:

- si la estética de tu sitio es tal que es intuitivo y sencillo de navegar para el usuario;
- si tu CSS ha sido factorizado en un archivo o archivos CSS separados; y
- si has evitado la repetición y redundancia "cascading" de propiedades de estilo desde etiquetas principales.

Lamentablemente, `style50` no admite archivos HTML, por lo que te corresponde a ti sangrar y alinear tus etiquetas HTML de forma clara. También debes saber que puedes crear un comentario HTML con:

    <!-- Comentario aquí -->

pero comentar tu código HTML no es tan imperativo como lo es cuando se comentan códigos en, por ejemplo, C o Python. También puedes comentar tu CSS, en archivos CSS, con:

    /* Comentario aquí */

## Consejos

Para obtener guías bastante completas sobre los idiomas introducidos en este problema, consulta estos tutoriales:

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [JavaScript](https://www.w3schools.com/js/)

## Cómo enviar

    submit50 cs50/problems/2024/x/homepage