## Lisibilité

![Couverture de Charlotte's Web](https://cs50.harvard.edu/x/2024/psets/2/readability/charlottes_web.jpg)

## Problème à résoudre

D'après [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), _Charlotte’s Web_ de E.B. White se situe entre le niveau de lecture d'un élève de CE2 et de CM2, et _The Giver_ de Lois Lowry entre le niveau de lecture d'un élève de sixième et de terminale. Mais que signifie qu'un livre soit à un niveau de lecture particulier ?

Eh bien, dans de nombreux cas, un expert humain peut lire un livre et décider pour quelle classe (c'est-à-dire quelle année d'école) il pense que le livre est le plus approprié. Mais un algorithme pourrait aussi probablement le déterminer !

Dans un fichier nommé `readability.c` dans un dossier nommé `readability`, vous allez implémenter un programme qui calcule le niveau scolaire approximatif nécessaire pour comprendre un texte. Votre programme doit imprimer en sortie « Niveau X » où « X » est le niveau scolaire calculé, arrondi à l'entier le plus proche. Si le niveau scolaire est 16 ou plus (équivalent ou supérieur à un niveau de lecture d'étudiant en deuxième cycle), votre programme doit sortir « Niveau 16+ » au lieu de donner le numéro d'index exact. Si le niveau scolaire est inférieur à 1, votre programme doit générer en sortie « Avant le niveau 1 ».

## Démo

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script>

## Contexte

Alors, quels sont les traits caractéristiques des niveaux de lecture supérieurs ? Eh bien, les mots plus longs sont probablement corrélés à des niveaux de lecture plus élevés. De même, les phrases plus longues sont probablement également en corrélation avec des niveaux de lecture plus élevés.

Un certain nombre de « tests de lisibilité » ont été développés au fil des ans qui définissent des formules pour calculer le niveau de lecture d'un texte. L'un de ces tests de lisibilité est l'_indice Coleman-Liau_. L'indice Coleman-Liau d'un texte est conçu pour sortir le niveau scolaire (américain) nécessaire pour comprendre un texte. La formule est

    indice = 0,0588 * L - 0,296 * S - 15,8

où `L` est le nombre moyen de lettres pour 100 mots dans le texte, et `S` est le nombre moyen de phrases pour 100 mots dans le texte.

## Conseils

### Écrivez du code que vous savez compiler

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {

    }

Notez que vous avez maintenant inclus quelques fichiers d'en-tête qui vous donneront accès à des fonctions qui pourraient vous aider à résoudre ce problème.

### Écrivez du pseudocode avant d'écrire plus de code

Si vous n'êtes pas sûr de savoir comment résoudre le problème lui-même, décomposez-le en problèmes plus petits que vous pouvez probablement résoudre en premier. Par exemple, ce problème n'est en réalité qu'une poignée de problèmes :

1.  Demandez à l'utilisateur du texte
2.  Comptez le nombre de lettres, de mots et de phrases dans le texte
3.  Calculez l'indice Coleman-Liau
4.  Imprimez le niveau scolaire

Écrivons du pseudocode sous forme de commentaires pour vous rappeler de faire exactement cela :

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Demandez à l'utilisateur du texte

        // Comptez le nombre de lettres, de mots et de phrases dans le texte

        // Calculez l'indice Coleman-Liau

        // Imprimez le niveau scolaire
    }

### Conversion du pseudo-code en code

Tout d'abord, réfléchissez à la façon dont vous pourriez inviter l'utilisateur à saisir du texte. Rappelez-vous que `get_string`, une fonction de la bibliothèque CS50, peut inviter l'utilisateur à saisir une chaîne.

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Invitez l'utilisateur à saisir du texte
        string text = get_string("Texte : ");

        // Comptez le nombre de lettres, de mots et de phrases dans le texte

        // Calculez l'index de Coleman-Liau

        // Imprimez le niveau de classe
    }

Maintenant que vous avez recueilli les données de l'utilisateur, vous pouvez commencer à les analyser. Tout d'abord, essayez de compter le nombre de lettres dans le texte. Considérez les lettres comme des caractères alphabétiques majuscules ou minuscules, et non comme des caractères de ponctuation, des chiffres ou d'autres symboles.

Une façon d'aborder ce problème est de créer une fonction appelée `count_letters` qui prend une chaîne, `text`, comme entrée, puis renvoie le nombre de lettres dans ce texte sous la forme d'un `int`.

    int count_letters(string text)
    {
        // Renvoie le nombre de lettres dans text
    }

Vous devrez écrire votre propre code pour compter le nombre de lettres dans le texte. Mais quelqu'un de plus expérimenté que vous a peut-être déjà écrit une fonction pour déterminer si un caractère est alphabétique. C'est une bonne occasion d'utiliser le [manuel CS50](https://manual.cs50.io/), une collection d'explications sur les fonctions courantes de la bibliothèque standard C.

Vous pouvez intégrer `count_letters` dans le code que vous avez déjà écrit, comme suit.

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string text);

    int main(void)
    {
        // Invitez l'utilisateur à saisir du texte
        string text = get_string("Texte : ");

        // Comptez le nombre de lettres, de mots et de phrases dans le texte
        int letters = count_letters(text);

        // Calculez l'index de Coleman-Liau

        // Imprimez le niveau de classe
    }

    int count_letters(string text)
    {
        // Renvoie le nombre de lettres dans text
    }

Ensuite, écrivez une fonction pour compter les mots.

    int count_words(string text)
    {
        // Renvoie le nombre de mots dans text
    }

Pour les besoins de ce problème, nous considérerons que toute séquence de caractères séparée par un espace est un mot (donc un mot composé comme « beau-frère » doit être considéré comme un mot, et non trois). Vous pouvez supposer qu'une phrase :

- contiendra au moins un mot ;
- ne commencera ni ne se terminera par un espace ;
- ne contiendra pas plusieurs espaces d'affilée.

Dans ces hypothèses, vous pourriez être en mesure de trouver une relation entre le nombre de mots et le nombre d'espaces. Bien entendu, vous pouvez essayer une solution qui tolérera plusieurs espaces entre les mots ou même aucun mot !

Vous pouvez maintenant intégrer `count_words` dans votre programme comme suit :

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string text);
    int count_words(string text);

    int main(void)
    {
        // Invitez l'utilisateur à saisir du texte
        string text = get_string("Texte : ");

        // Comptez le nombre de lettres, de mots et de phrases dans le texte
        int letters = count_letters(text);
        int words = count_words(text);

        // Calculez l'index de Coleman-Liau

        // Imprimez le niveau de classe
    }

    int count_letters(string text)
    {
        // Renvoie le nombre de lettres dans text
    }

    int count_words(string text)
    {
        // Renvoie le nombre de mots dans text
    }

Enfin, écrivez une fonction pour compter les phrases. Vous pouvez considérer toute séquence de caractères se terminant par un `.`, un `!` ou un `?` comme une phrase.

    int count_sentences(string text)
    {
        // Renvoie le nombre de phrases dans text
    }

Vous pouvez intégrer `count_sentences` dans votre programme comme suit :

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string text);
    int count_words(string text);
    int count_sentences(string text);

    int main(void)
    {
        // Demandez à l'utilisateur s'il souhaite obtenir du texte
        string text = get_string("Texte : ");

        // Comptez le nombre de lettres, de mots et de phrases dans le texte
        int letters = count_letters(text);
        int words = count_words(text);
        int sentences = count_sentences(text);

        // Calculez l'indice de lisibilité Coleman-Liau

        // Imprimez le niveau scolaire
    }

    int count_letters(string text)
    {
        // Renvoyez le nombre de lettres dans le texte
    }

    int count_words(string text)
    {
        // Renvoyez le nombre de mots dans le texte
    }

    int count_sentences(string text)
    {
        // Renvoyez le nombre de phrases dans le texte
    }

Enfin, calculez l'indice Coleman-Liau et imprimez le niveau scolaire correspondant.

- Souvenez-vous que l'indice Coleman-Liau est calculé à l'aide de la formule : `index = 0,0588 * L - 0,296 * S - 15,8`
- `L` est le nombre moyen de lettres pour 100 mots dans le texte : il s'agit du nombre de lettres divisé par le nombre de mots, multiplié par 100.
- `S` est le nombre moyen de phrases pour 100 mots dans le texte : il s'agit du nombre de phrases divisé par le nombre de mots, multiplié par 100.
- Vous souhaiterez arrondir le résultat au nombre entier le plus proche, en rappelant que `round` est déclarée dans `math.h`, conformément à : [manual.cs50.io](https://manual.cs50.io/).
- Rappelez-vous que, lorsque vous divisez des valeurs de type `int` en C, le résultat sera également un `int`, et que tout reste (c.-à-d., les chiffres après la virgule décimale) sera ignoré. En d'autres termes, le résultat sera « tronqué ». Vous pouvez convertir une ou plusieurs de vos valeurs en `float` avant d'effectuer une division lors du calcul de `L` et `S` !

Si l'indice résultant est supérieur ou égal à 16 (équivalent ou supérieur au niveau de lecture d'un étudiant en licence), votre programme doit afficher « Niveau 16+ » au lieu d'un indice numérique exact. Si l'indice est inférieur à 1, votre programme doit afficher « Avant le niveau 1 ».

## Procédure pas à pas

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/AOVyZEh9zgE?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Comment tester

Exécutez votre programme sur les textes suivants pour vérifier que vous obtenez le niveau scolaire spécifié. Veillez à ne copier que le texte, sans espaces supplémentaires.

- `Un poisson. Deux poissons. Poisson rouge. Poisson bleu.` (Avant le niveau 1)
- `Les souhaitez-vous ici ou là ? Je ne les voudrais ni ici ni là. Je ne les voudrais nulle part.` (Niveau 2)
- `Félicitations ! Aujourd'hui, c'est votre jour. Vous êtes parti pour des endroits formidables ! Vous êtes parti, en route !` (Niveau 3)
- `Harry Potter était un garçon très inhabituel à bien des égards. D'abord, il détestait les vacances d'été plus que toute autre période de l'année. Par ailleurs, il avait vraiment envie de faire ses devoirs, mais était obligé de les faire en secret, dans le silence de la nuit. Et il se trouvait qu'il était aussi un sorcier.` (Niveau 5)
- `Dans mes jeunes années, plus vulnérables, mon père m'a donné quelques conseils que je n'ai cessé de méditer depuis.` (Niveau 7)
- `Alice commençait à trouver très fatigant de rester assise près de sa sœur sur la berge, et de n'avoir rien à faire : une ou deux fois, elle avait jeté un coup d'œil dans le livre que sa sœur lisait, mais il n'y avait ni images ni conversations dedans ; « Et à quoi bon un livre », pensa Alice, « sans images ni conversations ? »` (Niveau 8)
- `Alors qu'il avait presque treize ans, mon frère Jem s'est cassé le bras au niveau du coude. Quand il a guéri, et que les craintes de Jem de ne plus jamais pouvoir jouer au football ont été apaisées, il s'est rarement complexé à propos de sa blessure. Son bras gauche était un peu plus court que le droit ; quand il se tenait debout ou qu'il marchait, le dos de sa main formait un angle droit avec son corps, son pouce était parallèle à sa cuisse.` (Niveau 8)
- `Il y a plus de choses au paradis et sur Terre, Horatio, que ce dont rêve votre philosophie.` (Niveau 9)
- `C'était une journée froide et ensoleillée d'avril, et les horloges sonnaient les treize heures. Winston Smith, son menton enfoui dans sa poitrine pour essayer d'échapper au vent vil, se glissa rapidement dans les portes vitrées de Victory Mansions, mais pas assez vite pour empêcher un tourbillon de poussière crasseuse d'entrer avec lui.` (Niveau 10)
- `Une grande partie des problèmes de calcul implique la détermination des propriétés de graphes, de digraphes, d'entiers, de tableaux d'entiers, de familles finies d'ensembles finis, de formules booléennes et d'éléments d'autres domaines dénombrables.` (Niveau 16+)

### Justesse

Dans votre terminal, exécutez la commande ci-dessous pour vérifier la justesse de votre travail.

    check50 cs50/problems/2024/x/readability

### Style

Exécutez la commande ci-dessous pour évaluer le style de votre code à l'aide de `style50`.

    style50 readability.c

## Comment soumettre

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2024/x/readability

