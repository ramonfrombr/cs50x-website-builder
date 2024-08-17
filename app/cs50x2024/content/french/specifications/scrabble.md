# Scrabble

![Scrabble Board](https://cs50.harvard.edu/x/2024/psets/2/scrabble/scrabble.png)

## Problème à Résoudre

Dans le jeu [Scrabble](https://scrabble.hasbro.com/en-us/rules), les joueurs créent des mots pour marquer des points, et les points sont la somme des points de chaque lettre dans le mot.

| A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 3   | 3   | 2   | 1   | 4   | 2   | 4   | 1   | 8   | 5   | 1   | 3   | 1   | 1   | 3   | 10  | 1   | 1   | 1   | 1   | 4   | 4   | 8   | 4   | 10  |

Par exemple, pour marquer le mot « CODE », nous noterons que « C » vaut 3 points, « O » vaut 1 point, « D » vaut 2 points et « E » vaut 1 point. En les additionnant, nous obtenons que « CODE » vaut 7 points.

Dans un fichier appelé `scrabble.c` dans un dossier appelé `scrabble`, implémentez un programme en C qui détermine le gagnant d’une courte partie de type Scrabble. Votre programme demandera la saisie deux fois : une fois au « Joueur 1 » pour saisir son mot et une fois au « Joueur 2 » pour saisir son mot. Puis, en fonction du joueur qui marque le plus de points, votre programme imprimera « Joueur 1 gagne ! », « Joueur 2 gagne ! » ou « Égalité ! »  (si les deux joueurs ont marqué le même nombre de points).

## Démo

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-74B4kq3ftleKe6AdN0NxFV8CN" src="https://asciinema.org/a/74B4kq3ftleKe6AdN0NxFV8CN.js"></script>

## Conseil

### Écrire du code qui s’exécutera

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {

    }

Notez que vous avez maintenant inclus quelques fichiers d’en-tête qui vous donneront accès à des fonctions qui pourraient vous aider à résoudre le problème.

### Écrire du pseudocode avant d’écrire du code

Si vous n’êtes pas sûr de la manière de résoudre le problème, découpez-le en petits problèmes que vous pourrez probablement résoudre d’abord. Par exemple, ce problème n’est en fait qu’un ensemble de problèmes :

1. Demander à l’utilisateur de saisir deux mots
2. Calculer le score de chaque mot
3. Imprimer le gagnant

Écrivons du pseudocode en tant que commentaires pour vous rappeler de faire exactement cela :

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Demander à l'utilisateur de saisir deux mots

        // Calculer le score de chaque mot

        // Imprimer le gagnant
    }

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Certains problèmes dans les ensembles de problèmes, comme celui-ci, peuvent contenir des spoilers (comme le suivant) qui vous guident finalement tout au long de la solution. Bien que vous soyez autorisé à utiliser ce code, nous vous encourageons vivement à essayer des choses par vous-même en premier ! Les autres problèmes de l’ensemble de problèmes n’auront pas ce type de solution complète, et généralement le problème qui contient le « spoiler complet » est une version d’échauffement du plus gros problème auquel vous devrez vous attaquer plus tard.</p></div>

### Convertir le pseudocode en code

Tout d’abord, réfléchissez à la manière dont vous pourriez demander à l’utilisateur de saisir deux mots. Rappelez-vous que `get_string`, une fonction de la bibliothèque CS50, peut demander à l’utilisateur de saisir une chaîne.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Demander à l'utilisateur de saisir deux mots
        string word1 = get_string("Joueur 1 : ");
        string word2 = get_string("Joueur 2 : ");

        // Calculer le score de chaque mot

        // Imprimer le gagnant
    }

Ensuite, réfléchissez à la manière de calculer le score de chaque mot. Étant donné que le même algorithme de notation s’applique aux deux mots, vous avez une bonne opportunité d’_abstraction_. Ici, nous définirons une fonction appelée `compute_score` qui prend une chaîne, appelée `word`, comme entrée, puis renvoie le score de `word` sous forme de `int`.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int compute_score(string word);

    int main(void)
    {
        // Demander à l'utilisateur de saisir deux mots
        string word1 = get_string("Joueur 1 : ");
        string word2 = get_string("Joueur 2 : ");

        // Calculer le score de chaque mot
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Imprimer le gagnant
    }

    int compute_score(string word)
    {
        // Calculer et renvoyer le score de word
    }

Passez maintenant à l'implémentation de `compute_score`. Pour calculer le score d'un mot, vous devez connaître la valeur de chaque lettre du mot. Vous pouvez associer des lettres et leurs valeurs de point à un _array_. Imaginez un array de 26 `int`, appelé `POINTS`, dans lequel le premier nombre est la valeur de point pour ‘A’, le deuxième nombre est la valeur de point pour ‘B’, et ainsi de suite. En déclarant et en initialisant un tel array en dehors de toute fonction, vous pouvez vous assurer que cet array soit accessible à n'importe quelle fonction, y compris `compute_score`.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Points attribués à chaque lettre de l'alphabet
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string word);

    int main(void)
    {
        // Demandez à l'utilisateur de saisir deux mots
        string word1 = get_string("Joueur 1 : ");
        string word2 = get_string("Joueur 2 : ");

        // Calculez le score de chaque mot
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Affichez le gagnant
    }

    int compute_score(string word)
    {
        // Calculez et renvoyez le score du mot
    }

Pour implémenter `compute_score`, essayez d'abord de trouver la valeur de point d'une seule lettre dans `word`.

- Rappelez-vous que pour trouver le caractère à l'index n d'une chaîne, `s`, vous pouvez écrire `s[n]`. `word[0]`, par exemple, vous donnera le premier caractère de `word`.
- Maintenant, rappelez-vous que les ordinateurs représentent les caractères en utilisant [ASCII](http://asciitable.com/), une norme qui représente chaque caractère par un nombre.
- Rappelez-vous aussi que le 0e index de `POINTS`, `POINTS[0]`, vous donne la valeur de point de ‘A’. Pensez à la façon dont vous pourriez transformer la représentation numérique de ‘A’ en l'index de sa valeur de point. Et qu'en est-il de ‘a’ ? Vous devrez appliquer des transformations différentes aux lettres majuscules et minuscules. Les fonctions [`isupper`](https://manual.cs50.io/3/isupper) et [`islower`](https://manual.cs50.io/3/islower) pourraient vous être utiles.
- Gardez à l'esprit que les caractères qui ne sont _pas_ des lettres doivent recevoir zéro point. Par exemple, ‘!` vaut 0 point.

Si vous pouvez calculer correctement le score d'un _un_ caractère dans `words`, il est probable que vous puissiez utiliser une boucle pour additionner les points des autres caractères. Une fois que vous avez essayé ce qui précède par vous-même, considérez cet indice (très révélateur !) ci-dessous.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Points attribués à chaque lettre de l'alphabet
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string word);

    int main(void)
    {
        // Demandez à l'utilisateur de saisir deux mots
        string word1 = get_string("Joueur 1 : ");
        string word2 = get_string("Joueur 2 : ");

        // Calculez le score de chaque mot
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Affichez le gagnant
    }

    int compute_score(string word)
    {
        // Gardez une trace du score
        int score = 0;

        // Calculez le score pour chaque caractère
        for (int i = 0, len = strlen(word); i < len; i++)
        {
            if (isupper(word[i]))
            {
                score += POINTS[word[i] - 'A'];
            }
            else if (islower(word[i]))
            {
                score += POINTS[word[i] - 'a'];
            }
        }

        return score;
    }

Finalement, terminez la dernière étape de votre pseudocode : l'impression du gagnant. Rappelez-vous qu'une instruction `if` peut être utilisée pour vérifier si une condition est remplie, et que l'utilisation supplémentaire de `else if` ou `else` peut vérifier d'autres conditions (exclusives).

    if (/* Le joueur 1 gagne */)
    {
        // ...
    }
    else if (/* Le joueur 2 gagne */)
    {
        // ...
    }
    else
    {
        // ...
    }

Et une fois que vous avez essayé ce qui précède, n'hésitez pas à jeter un œil à l'indice (ou plutôt à la solution complète !) ci-dessous.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Points attribués à chaque lettre de l'alphabet
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string mot);

    int main(void)
    {
        // Demandez à l'utilisateur deux mots
        string mot1 = get_string("Joueur 1 : ");
        string mot2 = get_string("Joueur 2 : ");

        // Calculez le score de chaque mot
        int score1 = compute_score(mot1);
        int score2 = compute_score(mot2);

        // Imprimez le gagnant
        if (score1 > score2)
        {
            printf("Le joueur 1 gagne !\n");
        }
        else if (score1 < score2)
        {
            printf("Le joueur 2 gagne !\n");
        }
        else
        {
            printf("Égalité !\n");
        }
    }

    int compute_score(string mot)
    {
        // Gardez une trace du score
        int score = 0;

        // Calculez le score pour chaque caractère
        for (int i = 0, len = strlen(mot); i < len; i++)
        {
            if (isupper(mot[i]))
            {
                score += POINTS[mot[i] - 'A'];
            }
            else if (islower(mot[i]))
            {
                score += POINTS[mot[i] - 'a'];
            }
        }

        return score;
    }

## Comment tester

Votre programme doit se comporter selon les exemples ci-dessous.

    $ ./scrabble
    Joueur 1 : Question ?
    Joueur 2 : Question !
    Égalité !


    $ ./scrabble
    Joueur 1 : rouge
    Joueur 2 : Brouette
    Le joueur 2 gagne !


    $ ./scrabble
    Joueur 1 : ORDINATEUR
    Joueur 2 : sciences
    Le joueur 1 gagne !


    $ ./scrabble
    Joueur 1 : Scrabble
    Joueur 2 : gagnant
    Le joueur 1 gagne !

### Correction

Dans votre terminal, exécutez ce qui suit pour vérifier l'exactitude de votre travail.

    check50 cs50/problems/2024/x/scrabble

### Style

Exécutez ce qui suit pour évaluer le style de votre code à l'aide de `style50`.

    style50 scrabble.c

## Comment soumettre

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2024/x/scrabble

