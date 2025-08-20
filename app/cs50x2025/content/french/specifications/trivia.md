# Informations diverses

Rédigez une page Web permettant aux utilisateurs de répondre à des questions de culture générale.

![capture d'écran de questions de culture générale](https://cs50.harvard.edu/x/2024/psets/8/trivia/questions.png)

## Premiers pas

Ouvrez [VS Code](https://cs50.dev/).

Commencez par cliquer dans la fenêtre de votre terminal, puis exécutez `cd` seul. Vous devriez voir que son « invite » ressemble à ce qui suit.

    $

Cliquez dans la fenêtre du terminal, puis exécutez

    wget https://cdn.cs50.net/2023/fall/psets/8/trivia.zip

puis appuyez sur Entrée pour télécharger un fichier ZIP appelé `trivia.zip` dans votre espace de codage. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ni aucun autre caractère !

Exécutez ensuite

    unzip trivia.zip

pour créer un dossier appelé `trivia`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm trivia.zip

puis répondre par « y » suivi d'Entrée à l'invite pour supprimer le fichier ZIP téléchargé.

Tapez maintenant

    cd trivia

suivi d'Entrée pour accéder à ce répertoire (l'ouvrir). Votre invite devrait maintenant ressembler à ce qui suit.

    trivia/ $

Si tout s'est bien passé, vous devriez exécuter

    ls

et vous devriez voir un fichier `index.html` et un fichier `styles.css`.

Si vous rencontrez des problèmes, recommencez ces mêmes étapes et essayez de déterminer où vous avez fait une erreur !

## Détails de la mise en œuvre

Concevez une page Web à l'aide de HTML, CSS et JavaScript pour permettre aux utilisateurs de répondre à des questions de culture générale.

- Dans `index.html`, ajoutez sous « Partie 1 » une question de culture générale à choix multiples de votre choix avec HTML.
  - Vous devez utiliser un titre `h3` pour le texte de votre question.
  - Vous devez avoir un `button` pour chacun des choix de réponse possibles. Il doit y avoir au moins trois choix de réponse, dont un seul doit être correct.
- À l'aide de JavaScript, ajoutez une logique pour que les boutons changent de couleur lorsqu'un utilisateur clique dessus.
  - Si un utilisateur clique sur un bouton avec une réponse incorrecte, le bouton doit devenir rouge et un texte indiquant « Incorrect » doit apparaître sous la question.
  - Si un utilisateur clique sur un bouton avec la réponse correcte, le bouton doit devenir vert et un texte indiquant « Correct ! » doit apparaître sous la question.
- Dans `index.html`, ajoutez sous « Partie 2 » une question à réponse libre textuelle de votre choix avec HTML.
  - Vous devez utiliser un titre `h3` pour le texte de votre question.
  - Vous devez utiliser un champ `input` pour permettre à l'utilisateur de saisir une réponse.
  - Vous devez utiliser un `button` pour permettre à l'utilisateur de confirmer sa réponse.
- À l'aide de JavaScript, ajoutez une logique pour que le champ de texte change de couleur lorsqu'un utilisateur confirme sa réponse.
  - Si l'utilisateur saisit une réponse incorrecte et appuie sur le bouton de confirmation, le champ de texte doit devenir rouge et un texte indiquant « Incorrect » doit apparaître sous la question.
  - Si l'utilisateur saisit la réponse correcte et appuie sur le bouton de confirmation, le champ de saisie doit devenir vert et un texte indiquant « Correct ! » doit apparaître sous la question.

En option, vous pouvez également :

- Modifier `styles.css` pour changer le CSS de votre page Web !
- Ajouter des questions de culture générale supplémentaires à votre quiz de culture générale si vous le souhaitez !

### Marche à suivre

<div class="alert alert-primary" data-alert="primary" role="alert"><p>Cette vidéo a été enregistrée alors que le cours utilisait encore CS50 IDE pour écrire du code. Bien que l'interface puisse paraître différente de votre espace de codage, le comportement des deux environnements doit être très similaire !</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/WGd0Jx7rxUo"></iframe>

### Astuces

- Utilisez [`document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) pour rechercher un seul élément HTML.
- Utilisez [`document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) pour rechercher plusieurs éléments HTML qui correspondent à une requête. La fonction renvoie un tableau de tous les éléments correspondants.

<details><summary>Vous ne savez pas comment résoudre le problème ?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/FLlI7rSSV_M"></iframe></details>

### Tests

Pas de `check50` pour celle-ci, car les mises en œuvre varient en fonction de vos questions ! Mais assurez-vous de tester les réponses incorrectes et correctes pour chacune de vos questions pour vous assurer que votre page Web répond de manière appropriée.

Exécutez `http-server` dans votre terminal alors que vous êtes dans votre répertoire `trivia` pour démarrer un serveur Web qui héberge votre page Web.

## Comment soumettre

    submit50 cs50/problems/2024/x/trivia

Vous voulez voir la solution du personnel ? Vous pouvez trouver deux façons de résoudre le problème ici !

**Création d’écouteurs d’événements avec JavaScript **

    <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
            <link href="styles.css" rel="stylesheet">
            <title>Trivia!</title>
            <script>

                // Attendre que le contenu DOM soit chargé
                document.addEventListener('DOMContentLoaded', function() {

                    // Récupérer tous les éléments avec la classe "correct"
                    let corrects = document.querySelectorAll('.correct');

                    // Ajouter des écouteurs d’événements à chaque bouton correct
                    for (let i = 0; i < corrects.length; i++) {
                        corrects[i].addEventListener('click', function() {

                            // Définir la couleur d'arrière-plan sur vert
                            corrects[i].style.backgroundColor = 'Green';

                            // Accéder à l'élément parent du bouton correct et trouver le premier élément avec la classe "feedback" qui a ce parent
                            corrects[i].parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                        });
                    }

                    // Lorsqu'une réponse incorrecte est cliquée, changer la couleur en rouge.
                    let incorrects = document.querySelectorAll(".incorrect");
                    for (let i = 0; i < incorrects.length; i++) {
                        incorrects[i].addEventListener('click', function() {

                            // Définir la couleur d'arrière-plan sur rouge
                            incorrects[i].style.backgroundColor = 'Red';

                            // Accéder à l'élément parent du bouton correct et trouver le premier élément avec la classe "feedback" qui a ce parent
                            incorrects[i].parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                        });
                    }

                    // Vérifier la soumission de réponse libre
                    document.querySelector('#check').addEventListener('click', function() {
                        let input = document.querySelector('input');
                        if (input.value === 'Switzerland') {
                            input.style.backgroundColor = 'green';
                            input.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                        }
                        else {
                            input.style.backgroundColor = 'red';
                            input.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                        }
                    });
                });
            </script>
        </head>
        <body>
            <div class="header">
                <h1>Trivia!</h1>
            </div>

            <div class="container">
                <div class="section">
                    <h2>Partie 1 : Choix multiples </h2>
                    <hr>
                    <h3>Quel est le rapport approximatif entre la population et les moutons en Nouvelle-Zélande ?</h3>
                    <button class="incorrect">6 personnes pour 1 mouton</button>
                    <button class="incorrect">3 personnes pour 1 mouton</button>
                    <button class="incorrect">1 personne pour 1 mouton</button>
                    <button class="incorrect">1 personne pour 3 moutons</button>
                    <button class="correct">1 personne pour 6 moutons</button>
                    <p class="feedback"></p>
                </div>

                <div class="section">
                    <h2>Partie 2 : Réponse libre</h2>
                    <hr>
                    <h3>Dans quel pays est-il illégal de posséder un seul cochon d'Inde, car un cochon d'Inde solitaire pourrait se sentir seul ?</h3>
                    <input type="text"></input>
                    <button id="check">Vérifier la réponse</button>
                    <p class="feedback"></p>
                </div>
            </div>
        </body>
    </html>

**Création d'écouteurs d'événements avec HTML**

    <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
            <link href="styles.css" rel="stylesheet">
            <title>Trivia!</title>
            <script>
                function checkMultiChoice(event) {

                    // Récupérer l'élément qui a déclenché l'événement
                    let button = event.target;

                    // Vérifier si le HTML interne de l'élément correspond à la réponse attendue
                    if (button.innerHTML == '1 personne pour 6 moutons') {
                        button.style.backgroundColor = 'Green';
                        button.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                    }
                    else {
                        button.style.backgroundColor = 'Red';
                        button.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                    }
                }

                function checkFreeResponse(event) {

                    // Récupérer l'élément qui a déclenché l'événement
                    let button = event.target;

                    // Récupérer l'élément input correspondant au bouton
                    let input = button.parentElement.querySelector('input');

                    // Vérifier la réponse correcte
                    if (input.value === 'Switzerland') {
                        input.style.backgroundColor = 'Green';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                    }
                    else {
                        input.style.backgroundColor = 'Red';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                    }
                }
            </script>
        </head>
        <body>
            <div class="header">
                <h1>Trivia!</h1>
            </div>

            <div class="container">
                <div class="section">
                    <h2>Partie 1 : Choix multiples </h2>
                    <hr>
                    <h3>Quel est le rapport approximatif entre la population et les moutons en Nouvelle-Zélande ?</h3>
                    <button onclick="checkMultiChoice(event)">6 personnes pour 1 mouton</button>
                    <button onclick="checkMultiChoice(event)">3 personnes pour 1 mouton</button>
                    <button onclick="checkMultiChoice(event)">1 personne pour 1 mouton</button>
                    <button onclick="checkMultiChoice(event)">1 personne pour 3 moutons</button>
                    <button onclick="checkMultiChoice(event)">1 personne pour 6 moutons</button>
                    <p class="feedback"></p>
                </div>

                <div class="section">
                    <h2>Partie 2 : Réponse libre</h2>
                    <hr>
                    <h3>Dans quel pays est-il illégal de posséder un seul cochon d'Inde, car un cochon d'Inde solitaire pourrait se sentir seul ?</h3>
                    <input type="text"></input>
                    <button onclick="checkFreeResponse(event)">Vérifier la réponse</button>
                    <p class="feedback"></p>
                </div>
            </div>
        </body>
    </html>

