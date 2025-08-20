**# Lisibilité**

## Problème à résoudre

Écrivez, dans un fichier nommé `readability.py` situé dans un dossier nommé `sentimental-readability`, un programme qui demande tout d'abord à l'utilisateur d'entrer du texte, puis affiche le niveau scolaire du texte, conformément à la formule Coleman-Liau, exactement comme vous l'avez fait dans l'[ensemble des problèmes 2](../../2/), sauf que votre programme cette fois doit être écrit en Python.

## Démo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-WnE6pZNnDkDm8NtuxrTqY1Nu4" src="https://asciinema.org/a/WnE6pZNnDkDm8NtuxrTqY1Nu4.js"></script>

## Spécification

- Rappelez-vous que l'indice Coleman-Liau est calculé comme suit : `0,0588 * L - 0,296 * S - 15,8`, où `L` est le nombre moyen de lettres pour 100 mots dans le texte, et `S` est le nombre moyen de phrases pour 100 mots dans le texte.
- Utilisez `get_string` de la bibliothèque CS50 pour obtenir l'entrée de l'utilisateur, et `print` pour afficher votre réponse.
- Votre programme doit compter le nombre de lettres, de mots et de phrases dans le texte. Vous pouvez considérer qu'une lettre est tout caractère minuscule de `a` à `z` ou tout caractère majuscule de `A` à `Z`, que toute séquence de caractères séparés par des espaces doit être comptée comme un mot, et que toute occurrence d'un point, d'un point d'exclamation ou d'un point d'interrogation indique la fin d'une phrase.
- Votre programme doit afficher en sortie `"Niveau X"`, où `X` est le niveau scolaire calculé par la formule Coleman-Liau, arrondi à l'entier le plus proche.
- Si le nombre d'index résultant est égal ou supérieur à 16 (équivalent ou supérieur à un niveau de lecture de premier cycle), votre programme doit afficher `"Niveau 16+"` au lieu de donner le nombre d'index exact. Si le nombre d'index est inférieur à 1, votre programme doit afficher `"Avant le niveau 1"`.

## Comment tester

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à d'abord tester votre code par vous-même pour chacun des éléments suivants.

- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `One fish. Two fish. Red fish. Blue fish.` et appuyez sur Entrée. Votre programme doit afficher `Avant le niveau 1`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` et appuyez sur Entrée. Votre programme doit afficher `Niveau 2`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `Congratulations! Today is your day. You're off to Great Places! You're off and away!` et appuyez sur Entrée. Votre programme doit afficher `Niveau 3`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` et appuyez sur Entrée. Votre programme doit afficher `Niveau 5`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` et appuyez sur Entrée. Votre programme doit afficher `Niveau 7`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` et appuyez sur Entrée. Votre programme doit afficher `Niveau 8`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` et appuyez sur Entrée. Votre programme doit afficher `Niveau 8`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` et appuyez sur Entrée. Votre programme doit afficher `Niveau 9`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` et appuyez sur Entrée. Votre programme doit afficher `Niveau 10`.
- Exécutez votre programme comme `python readability.py`, et attendez une invite pour la saisie. Tapez `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` et appuyez sur Entrée. Votre programme doit afficher `Niveau 16+`.

### Correction

    check50 cs50/problems/2024/x/sentimental/readability

### Style

    style50 readability.py

## Comment soumettre

    submit50 cs50/problems/2024/x/sentimental/readability