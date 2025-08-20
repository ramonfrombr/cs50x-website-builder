# Trivia

Escribe una página web que permita a los usuarios responder preguntas de trivia.

![captura de pantalla de preguntas de trivia](https://cs50.harvard.edu/x/2024/psets/8/trivia/questions.png)

## Introducción

Abre [VS Code](https://cs50.dev/).

Comienza haciendo clic dentro de la ventana de tu terminal, luego ejecuta `cd` solo. Deberías encontrarte con que su "indicador" se asemeja a lo siguiente.

    $

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/8/trivia.zip

seguido de Enter para descargar un ZIP llamado `trivia.zip` en tu espacio de códigos. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter para el caso!

Ahora ejecuta

    unzip trivia.zip

para crear una carpeta llamada `trivia`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm trivia.zip

y responde con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd trivia

seguido de Enter para moverte (es decir, abrir) a ese directorio. Tu indicador ahora debería parecerse al siguiente.

    trivia/ $

Si todo tuvo éxito, debes ejecutar

    ls

y deberías ver un archivo `index.html` y un archivo `styles.css`.

Si tienes algún problema, sigue estos mismos pasos nuevamente y ve si puedes determinar dónde te equivocaste.

## Detalles de la implementación

Diseña una página web usando HTML, CSS y JavaScript para permitir que los usuarios respondan preguntas de trivia.

- En `index.html`, agrega debajo de la "Parte 1" una pregunta de trivia de opción múltiple de tu elección con HTML.
  - Debes usar un encabezado `h3` para el texto de tu pregunta.
  - Debes tener un `button` para cada una de las posibles opciones de respuesta. Debe haber al menos tres opciones de respuesta, de las cuales exactamente una debe ser correcta.
- Usando JavaScript, agrega lógica para que los botones cambien de color cuando un usuario hace clic en ellos.
  - Si un usuario hace clic en un botón con una respuesta incorrecta, el botón debe ponerse rojo y debe aparecer un texto debajo de la pregunta que diga "Incorrecto".
  - Si un usuario hace clic en un botón con la respuesta correcta, el botón debe ponerse verde y debe aparecer un texto debajo de la pregunta que diga "¡Correcto!".
- En `index.html`, agrega debajo de la "Parte 2" una pregunta de respuesta libre basada en texto de tu elección con HTML.
  - Debes usar un encabezado `h3` para el texto de tu pregunta.
  - Debes usar un campo `input` para permitir que el usuario escriba una respuesta.
  - Debes usar un `button` para permitir que el usuario confirme su respuesta.
- Usando JavaScript, agrega lógica para que el campo de texto cambie de color cuando un usuario confirma su respuesta.
  - Si el usuario escribe una respuesta incorrecta y presiona el botón de confirmación, el campo de texto debe ponerse rojo y debe aparecer un texto debajo de la pregunta que diga "Incorrecto".
  - Si el usuario escribe la respuesta correcta y presiona el botón de confirmación, el campo de entrada debe ponerse verde y debe aparecer un texto debajo de la pregunta que diga "¡Correcto!".

Opcionalmente, también puedes:

- ¡Editar `styles.css` para cambiar el CSS de tu página web!
- ¡Agrega preguntas de trivia adicionales a tu cuestionario de trivia si lo deseas!

### Tutorial

<div class="alert alert-primary" data-alert="primary" role="alert"><p>Este video fue grabado cuando el curso todavía usaba CS50 IDE para escribir código. Aunque la interfaz puede verse diferente de tu espacio de códigos, ¡el comportamiento de los dos entornos debería ser muy similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/WGd0Jx7rxUo"></iframe>

### Sugerencias

- Usa [`document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) para consultar un solo elemento HTML.
- Usa [`document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) para consultar múltiples elementos HTML que coincidan con una consulta. La función devuelve una matriz de todos los elementos coincidentes.

<details><summary>¿No estás seguro de cómo resolverlo?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/FLlI7rSSV_M"></iframe></details>

### Pruebas

¡No hay `check50` para este, ya que las implementaciones variarán según tus preguntas! Pero asegúrate de probar respuestas incorrectas y correctas para cada una de tus preguntas para garantizar que tu página web responda adecuadamente.

Ejecuta `http-server` en tu terminal mientras estás en tu directorio `trivia` para iniciar un servidor web que atienda tu página web.

## Cómo enviar

    submit50 cs50/problems/2024/x/trivia

**Creando escuchas de eventos con JavaScript**

    <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
            <link href="styles.css" rel="stylesheet">
            <title>¡Trivial!</title>
            <script>

                // Esperar a que se cargue el contenido DOM
                document.addEventListener('DOMContentLoaded', function() {

                    // Obtener todos los elementos con la clase "correcto"
                    let corrects = document.querySelectorAll('.correct');

                    // Añadir escuchas de eventos a cada botón correcto
                    for (let i = 0; i < corrects.length; i++) {
                        corrects[i].addEventListener('click', function() {

                            // Establecer el color de fondo a verde
                            corrects[i].style.backgroundColor = 'Green';

                            // Ir al elemento padre del botón correcto y encontrar el primer elemento con la clase "feedback" que tenga ese padre
                            corrects[i].parentElement.querySelector('.feedback').innerHTML = '¡Correcto!';
                        });
                    }

                    // Cuando se haga clic en cualquier respuesta incorrecta, cambiar el color a rojo.
                    let incorrects = document.querySelectorAll(".incorrect");
                    for (let i = 0; i < incorrects.length; i++) {
                        incorrects[i].addEventListener('click', function() {

                            // Establecer el color de fondo a rojo
                            incorrects[i].style.backgroundColor = 'Red';

                            // Ir al elemento padre del botón correcto y encontrar el primer elemento con la clase "feedback" que tenga ese padre
                            incorrects[i].parentElement.querySelector('.feedback').innerHTML = 'Incorrecto';
                        });
                    }

                    // Verificar el envío de respuesta libre
                    document.querySelector('#check').addEventListener('click', function() {
                        let input = document.querySelector('input');
                        if (input.value === 'Suiza') {
                            input.style.backgroundColor = 'green';
                            input.parentElement.querySelector('.feedback').innerHTML = '¡Correcto!';
                        }
                        else {
                            input.style.backgroundColor = 'red';
                            input.parentElement.querySelector('.feedback').innerHTML = 'Incorrecto';
                        }
                    });
                });
            </script>
        </head>
        <body>
            <div class="header">
                <h1>¡Trivial!</h1>
            </div>

            <div class="container">
                <div class="section">
                    <h2>Parte 1: Opción múltiple </h2>
                    <hr>
                    <h3>¿Cuál es la proporción aproximada de personas con respecto a las ovejas en Nueva Zelanda?</h3>
                    <button class="incorrect">6 personas por 1 oveja</button>
                    <button class="incorrect">3 personas por 1 oveja</button>
                    <button class="incorrect">1 persona por 1 oveja</button>
                    <button class="incorrect">1 persona por 3 ovejas</button>
                    <button class="correct">1 persona por cada 6 ovejas</button>
                    <p class="feedback"></p>
                </div>

                <div class="section">
                    <h2>Parte 2: Respuesta libre</h2>
                    <hr>
                    <h3>¿En qué país es ilegal poseer solo un conejillo de indias, ya que un conejillo de indias solitario puede sentirse solo?</h3>
                    <input type="text"></input>
                    <button id="check">Comprobar respuesta</button>
                    <p class="feedback"></p>
                </div>
            </div>
        </body>
    </html>

**Creación de escuchas de eventos con HTML**

    <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
            <link href="styles.css" rel="stylesheet">
            <title>¡Trivial!</title>
            <script>
                function checkMultiChoice(event) {

                    // Obtener el elemento que desencadenó el evento
                    let button = event.target;

                    // Verificar si el HTML interno del elemento coincide con la respuesta esperada
                    if (button.innerHTML == '1 persona por cada 6 ovejas') {
                        button.style.backgroundColor = 'Green';
                        button.parentElement.querySelector('.feedback').innerHTML = '¡Correcto!';
                    }
                    else {
                        button.style.backgroundColor = 'Red';
                        button.parentElement.querySelector('.feedback').innerHTML = 'Incorrecto';
                    }
                }

                function checkFreeResponse(event) {

                    // Obtener el elemento que desencadenó el evento
                    let button = event.target;

                    // Obtener el elemento de entrada correspondiente al botón
                    let input = button.parentElement.querySelector('input');

                    // Verificar la respuesta correcta
                    if (input.value === 'Suiza') {
                        input.style.backgroundColor = 'Green';
                        input.parentElement.querySelector('.feedback').innerHTML = '¡Correcto!';
                    }
                    else {
                        input.style.backgroundColor = 'Red';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Incorrecto';
                    }
                }
            </script>
        </head>
        <body>
            <div class="header">
                <h1>¡Trivial!</h1>
            </div>

            <div class="container">
                <div class="section">
                    <h2>Parte 1: Opción múltiple </h2>
                    <hr>
                    <h3>¿Cuál es la proporción aproximada de personas con respecto a las ovejas en Nueva Zelanda?</h3>
                    <button onclick="checkMultiChoice(event)">6 personas por 1 oveja</button>
                    <button onclick="checkMultiChoice(event)">3 personas por 1 oveja</button>
                    <button onclick="checkMultiChoice(event)">1 persona por 1 oveja</button>
                    <button onclick="checkMultiChoice(event)">1 persona por 3 ovejas</button>
                    <button onclick="checkMultiChoice(event)">1 persona por cada 6 ovejas</button>
                    <p class="feedback"></p>
                </div>

                <div class="section">
                    <h2>Parte 2: Respuesta libre</h2>
                    <hr>
                    <h3>¿En qué país es ilegal poseer solo un conejillo de indias, ya que un conejillo de indias solitario puede sentirse solo?</h3>
                    <input type="text"></input>
                    <button onclick="checkFreeResponse(event)">Comprobar respuesta</button>
                    <p class="feedback"></p>
                </div>
            </div>
        </body>
    </html>

