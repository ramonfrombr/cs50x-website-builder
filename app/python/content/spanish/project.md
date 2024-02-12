# Proyecto Final

Una vez que hayas resuelto cada uno de los conjuntos de problemas del curso, es hora de implementar tu proyecto final, ¡un programa Python propio! El diseño y la implementación de tu proyecto dependen completamente de ti, aunque están sujetos a estos requisitos:

- Tu proyecto debe implementarse en Python.
- Tu proyecto debe tener una función `principal` y tres o más funciones adicionales. Al menos tres de esas funciones adicionales deben ir acompañadas de pruebas que se puedan ejecutar con `pytest`.
  - Tu función `principal` debe estar en un archivo llamado `proyecto.py`, que debe estar en la carpeta "raíz" (es decir, la carpeta de nivel superior) de tu proyecto.
  - Tus otras 3 funciones personalizadas requeridas además de `principal` también deben estar en `proyecto.py` y definirse al mismo nivel de sangría que `principal` (es decir, no anidadas bajo ninguna clase o función).
  - Tus funciones de prueba deben estar en un archivo llamado `test_proyecto.py`, que también debe estar en la carpeta "raíz" de tu proyecto. Asegúrate de que tengan el mismo nombre que tus funciones personalizadas, precedidas de `test_` (`test_funcion_personalizada`, por ejemplo, donde `funcion_personalizada` es una función que has implementado en `proyecto.py`).
  - Puedes implementar clases y funciones adicionales según consideres conveniente más allá del requisito mínimo.
- La implementación de tu proyecto debe requerir más tiempo y esfuerzo que el que se necesita para cada uno de los conjuntos de problemas del curso.
- Cualquier biblioteca instalable mediante `pip` que tu proyecto requiera debe estar enumerada, una por línea, en un archivo llamado `requirements.txt` en la carpeta raíz de tu proyecto.

Estructuras de Proyectos Ejemplo

`proyecto.py`

    def principal():
        ...


    def funcion_1():
        ...


    def funcion_2():
        ...


    def funcion_n():
        ...


    if __name__ == "__main__":
        principal()

`test_proyecto.py`

    def test_funcion_1():
        ...


    def test_funcion_2():
        ...


    def test_funcion_n():
        ...

Puedes colaborar, pero no es obligatorio, con uno o dos compañeros en tu proyecto. ([Quizás quieras colaborar con Live Share](https://code.visualstudio.com/learn/collaboration/live-share)!) Pero un proyecto de dos o tres personas requerirá el doble o triple de tiempo y esfuerzo que un proyecto individual.

Ten en cuenta que el personal de CS50 audita las presentaciones de CS50P, incluido este proyecto final. Los estudiantes que se encuentren en violación de [la política de Honestidad Académica](../#honestidad) serán eliminados del curso y no serán elegibles para recibir un certificado. Los estudiantes que ya han completado CS50P, si se encuentra que están en violación, tendrán su Certificado CS50 (y su certificado edX, si corresponde) revocado.

## Cuándo hacerlo

Antes del [2024-12-31T23:59:00-05:00](https://time.cs50.io/20241231T235900-0500).

## Primeros pasos

Crear un proyecto completo puede parecer abrumador. Aquí tienes algunas preguntas que debes tener en cuenta al comenzar:

- ¿Qué hará tu software? ¿Qué características tendrá? ¿Cómo se ejecutará?
- ¿Qué nuevas habilidades necesitarás adquirir? ¿Qué temas necesitarás investigar?
- Si trabajas con uno o dos compañeros, ¿quién hará qué?
- En el mundo del software, la mayoría de las cosas tardan más en implementarse de lo que esperas. Por lo tanto, no es raro lograr menos en una cantidad fija de tiempo de lo que esperas. ¿Qué podrías considerar como un buen resultado para tu proyecto? ¿Un resultado mejor? ¿El mejor resultado?

Considera establecer hitos de objetivo para mantenerte en el camino correcto.

## Cómo enviar el proyecto

**¡Debes completar los tres pasos!**

#### Paso 1 de 3

Crea un video corto (de no más de 3 minutos de duración) en el que presentes tu proyecto al mundo. Tu video **debe** comenzar con una sección de apertura que muestre:

- el título de tu proyecto;
- tu nombre;
- tus nombres de usuario de GitHub y edX;
- tu ciudad y país;
- y la fecha en que has grabado este video.

Luego, debe continuar demostrando tu proyecto en acción, utilizando diapositivas, capturas de pantalla, comentarios de voz y/o acción en vivo. Consulta [howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) para obtener consejos sobre cómo hacer una "grabación de pantalla", aunque también puedes usar una cámara real. Sube tu video a YouTube (o a un sitio similar si está bloqueado en tu país) y toma nota de su URL; está bien marcarlo como "no listado", pero no lo marques como "privado".

¡Envía [este formulario](https://forms.cs50.io/5e2dd8e8-3c8b-4eb2-b77d-085836253f26)!

#### Paso 2 de 3

Crea un archivo de texto `README.md` (¡con ese nombre exactamente!) en tu carpeta `~/proyecto` que explique tu proyecto. Este archivo debe incluir el título del proyecto, la URL de tu video (creado en el paso 1 anterior) y una descripción de tu proyecto. Puedes usar lo siguiente como plantilla.

        # TÍTULO DE TU PROYECTO
        #### Demostración en Video:  <URL AQUÍ>
        #### Descripción:
        TODO

Si no estás familiarizado con la sintaxis de Markdown, es posible que encuentres útil la [Sintaxis Básica de Escritura y Formato de GitHub](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax). Si estás usando CS50 Codespace y se te solicita "Abrir en CS50 Lab", simplemente presiona `cancelar` para abrirlo en el Editor. También puedes obtener una vista previa de tu archivo `.md` haciendo clic en el ícono de "vista previa", tal como se explica aquí: [Vista previa de Markdown en vscode](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview). Los archivos `README.md` estándar de proyectos de software a menudo pueden tener miles o decenas de miles de palabras de longitud; el tuyo no tiene que ser tan largo, pero debe tener al menos varios cientos de palabras que describan las cosas en detalle.

Tu archivo `README.md` debe tener al menos varios párrafos de longitud y debe explicar qué es tu proyecto, qué contiene y hace cada uno de los archivos que escribiste para el proyecto, y si debatiste ciertas opciones de diseño, explicar por qué las elegiste. Asegúrate de dedicar suficiente tiempo y energía a escribir un `README.md` que documente completamente tu proyecto. ¡Siéntete orgulloso de él! Un `README.md` de alrededor de 500 palabras probablemente será suficiente para describir tu proyecto y todos los aspectos de su funcionalidad. Si no puedes alcanzar ese umbral, probablemente eso significa que tu proyecto no es lo suficientemente complejo.

Ejecuta el comando `submit50` a continuación desde tu directorio `~/proyecto` (o desde el directorio que contenga el archivo `README.md` y el código de tu proyecto, que también debe enviarse). Si tu proyecto no cumple con todos los requisitos anteriores, puede ser rechazado, así que asegúrate de haber cumplido todos los puntos principales de esta especificación y haber escrito un `README` completo:

    submit50 cs50/problems/2022/python/project

¿Problemas para enviarlo?

Si encuentras problemas porque tu proyecto es demasiado grande, intenta comprimir todo el contenido de ese directorio en un archivo ZIP (excepto `README.md`) y envíalo así. Si sigue siendo demasiado grande, intenta eliminar ciertos archivos de configuración, reducir el tamaño de tu envío por debajo de 100MB, o intenta cargarlo directamente [utilizando la interfaz web de GitHub](https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/adding-a-file-to-a-repository) visitando [github.com/me50/USERNAME](https://github.com/me50/USERNAME) (donde `USERNAME` es tu propio nombre de usuario de GitHub) y arrastrando y soltando manualmente las carpetas, asegurándote de que al cargar lo haces en la rama `cs50/problems/2022/python/project`, de lo contrario, el sistema no podrá verificarlo.

#### Paso 3 de 3

¡Eso es todo! Tu proyecto debería ser calificado en unos pocos minutos. Asegúrate de visitar tu libro de calificaciones en [cs50.me/cs50p](https://cs50.me/cs50p) unos minutos después de enviarlo. Solo cargando tu Libro de Calificaciones, el sistema puede verificar si has completado el curso, y eso también es lo que desencadena la generación (instantánea) de tu certificado CS50 gratuito y la generación (dentro de los 30 días) del certificado verificado de edX, si has completado todas las demás tareas.

¡Esto fue CS50P!