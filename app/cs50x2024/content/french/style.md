## Guide de style pour C

Il n'y a pas une manière unique et idéale d'écrire le code. En revanche, il existe de nombreuses manières erronées (ou tout du moins, maladroites). Malgré cela, CS50 vous demande d'adhérer aux conventions ci-dessous afin que nous puissions analyser le style de votre code de manière fiable. De même, les entreprises adoptent généralement leurs propres conventions de style à l'échelle de l'entreprise.

## Longueur de ligne

Par convention, la longueur maximale d'une ligne de code en C est de 80 caractères, avec cet historique ancré dans les moniteurs de taille standard des anciens terminaux informatiques, qui pouvaient afficher 24 lignes verticales et 80 caractères horizontales. Bien que la technologie moderne ait rendu obsolète la nécessité de limiter les lignes à 80 caractères, il s'agit toujours d'une ligne directrice qui doit être considérée comme un "arrêt souple", et une ligne de 100 caractères doit vraiment être la plus longue que vous écrivez en C, sinon les lecteurs devront généralement faire défiler. Si vous avez besoin de plus de 100 caractères, il est peut-être temps de repenser vos noms de variables ou votre conception globale&nbsp;!

    // Ces lignes de code suivantes invitent d'abord l'utilisateur à donner deux valeurs entières, puis multiplient ces deux valeurs entières ensemble afin qu'elles puissent être utilisées plus tard dans le programme
    int first_collected_integer_value_from_user = get_int("Valeur entière, s'il vous plaît : ");
    int second_collected_integer_value_from_user = get_int("Un autre nombre entier, s'il vous plaît : ");
    int product_of_the_two_integer_values_from_user = first_collected_integer_value_from_user * second_collected_integer_value_from_user;

Dans d'autres langages, notamment JavaScript, il est beaucoup plus difficile de contraindre les lignes à une longueur maximale ; à cet endroit, votre objectif doit plutôt être de fractionner les lignes (comme via `\n`) dans des emplacements qui maximisent la lisibilité et la clarté.

## Commentaires

Les commentaires rendent le code plus lisible, non seulement pour les autres (par exemple, votre guide pédagogique), mais aussi pour vous, en particulier lorsque des heures, des jours, des semaines, des mois ou des années s'écoulent entre l'écriture et la lecture de votre propre code. Commenter trop peu est mauvais. Commenter trop est mauvais. Où est le juste milieu&nbsp;? Commenter toutes les quelques lignes de code (c'est-à-dire les blocs intéressants) est une directive décente. Essayez d'écrire des commentaires qui répondent à l'une ou aux deux questions suivantes :

1.  Que fait ce bloc ?
2.  Pourquoi ai-je implémenté ce bloc de cette façon ?

Dans les fonctions, utilisez des "commentaires en ligne" et gardez-les courts (par exemple, une ligne), sinon il devient difficile de distinguer les commentaires du code, même avec la [mise en évidence de la syntaxe](http://en.wikipedia.org/wiki/Syntax_highlighting). Placez le commentaire au-dessus de la ou des lignes auxquelles il s'applique. Inutile d'écrire en phrases complètes, mais mettez en majuscule le premier mot du commentaire (sauf s'il s'agit du nom d'une fonction, d'une variable ou autre), et laissez un espace entre `//` et le premier caractère de votre commentaire, comme dans :

    // Convertir Fahrenheit en Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

En d'autres termes, ne faites pas ceci :

    //Convertir Fahrenheit en Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

Ou ceci :

    // convertir Fahrenheit en Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

Ou ceci :

    float c = 5.0 / 9.0 * (f - 32.0); // Convertir Fahrenheit en Celsius

Au-dessus de vos fichiers .c et .h doit figurer un commentaire qui résume ce que fait votre programme (ou ce fichier particulier), comme dans :

    // Dit bonjour au monde

Au-dessus de chacune de vos fonctions (sauf peut-être `main`), en attendant, doit figurer un commentaire qui résume ce que fait votre fonction, comme dans :

    // Renvoie le carré de n
    int square(int n)
    {
        return n * n;
    }

## En-têtes de bibliothèque

Tous les en-têtes de bibliothèque que vous incluez doivent être classés par ordre alphabétique, comme dans :

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

Cela permet de voir plus facilement en un coup d'œil, en particulier dans une longue liste, si vous avez inclus un en-tête.

## Conditions

Les conditions doivent être formulées comme suit&nbsp;:

    if (x > 0)
    {
        printf("x est positif\n");
    }
        else if (x < 0)
    {
        printf("x est négatif\n");
    }
    else
    {
        printf("x est zéro\n");
    }

Remarquez comment :

- les accolades s'alignent bien, chacune sur sa propre ligne, indiquant clairement ce qui se trouve à l'intérieur de la branche ;
- il y a un seul espace après chaque `if` ;
- chaque appel à `printf` est indenté de 4 espaces ;
- il y a des espaces simples autour de `>` et autour de `<` ;
- et il n'y a aucun espace immédiatement après chaque `(` ou immédiatement avant chaque `)`.

Pour gagner de la place, certains programmeurs aiment garder les accolades du premier au même niveau que la condition elle-même, mais nous ne le recommandons pas, car c'est plus difficile à lire, alors ne faites pas ceci :

    if (x < 0) {
        printf("x est négatif\n");
    } else if (x < 0) {
        printf("x est négatif\n");
    }

Et ne faites surtout pas ceci :

    if (x < 0)
        {
        printf("x est négatif\n");
        }
    else
        {
        printf("x est négatif\n");
        }

## Sélecteurs

Déclarez un `switch` comme suit&nbsp;:

    switch (n)
    {
        case -1:
            printf("n est -1\n");
            break;

        case 1:
            printf("n est 1\n");
            break;

        default:
            printf("n n'est ni -1 ni 1\n");
            break;
    }

Remarquez comment :

- chaque accolade est sur sa propre ligne ;
- il y a un seul espace après `switch` ;
- il n'y a aucun espace immédiatement après chaque `(` ou immédiatement avant chaque `)` ;
- les cas du sélecteur sont indentés de 4 espaces ;
- les corps des cas sont indentés davantage avec 4 espaces ;
- et chaque `case` (y compris `default`) se termine par un `break`.

## Fonctions

Conformément à [C99](http://en.wikipedia.org/wiki/C99), assurez-vous de déclarer `main` avec :

    int main(void)
    {

    }

ou, si vous utilisez la bibliothèque CS50, avec :

    #include <cs50.h>

    int main(int argc, string argv[])
    {

    }

ou avec :

    int main(int argc, char *argv[])
    {

    }

ou même avec :

    int main(int argc, char **argv)
    {

    }

Ne déclarez pas `main` avec :

    int main()
    {

    }

ou avec :

    void main()
    {

    }

ou avec :

    main()
    {

    }

Quant à vos propres fonctions, assurez-vous de les définir de manière similaire, avec chaque accolade sur sa propre ligne et avec le type de retour sur la même ligne que le nom de la fonction, comme nous l'avons fait avec `main`.

## Indentation

Indentez votre code de quatre espaces à la fois pour indiquer clairement quels blocs de code se trouvent à l'intérieur des autres. Si vous utilisez la touche Tab de votre clavier pour ce faire, assurez-vous que votre éditeur de texte est configuré pour convertir les tabulations (`\t`) en quatre espaces, sinon votre code risque de ne pas s'imprimer ou de ne pas s'afficher correctement sur l'ordinateur de quelqu'un d'autre, car

## Les boucles

### for

Chaque fois que vous avez besoin de variables temporaires pour une itération, utilisez « i », puis « j », puis « k », sauf si des noms plus spécifiques rendent votre code plus lisible :

```cpp
for (int i = 0 ; i < LIMITE ; i++)
{
    for (int j = 0 ; j < LIMITE ; j++)
    {
        for (int k = 0 ; k < LIMITE ; k++)
        {
            // Faites quelque chose
        }
    }
}
```

Si vous avez besoin de plus de trois variables pour l’itération, il est peut-être temps de repenser votre conception !

### while

Déclarez les boucles « while » comme suit :

```cpp
while (condition)
{
    // Faites quelque chose
}
```

Remarquez comment :

- chaque accolade est sur sa propre ligne ;
- il y a un seul espace après « while » ;
- il n’y a pas d’espace immédiatement après la « ( » ou immédiatement avant la « ) » ; et
- le corps de la boucle (un commentaire dans ce cas) est indenté avec 4 espaces.

### do … while

Déclarez les boucles « do ... while » comme suit :

```cpp
do
{
    // Faites quelque chose
}
while (condition) ;
```

Remarquez comment :

- chaque accolade est sur sa propre ligne ;
- il y a un seul espace après « while » ;
- il n’y a pas d’espace immédiatement après la « ( » ou immédiatement avant la « ) » ; et
- le corps de la boucle (un commentaire dans ce cas) est indenté avec 4 espaces.

## Les pointeurs

Lorsque vous déclarez un pointeur, écrivez « * » à côté de la variable, comme dans :

```cpp
int *p ;
```

Ne l’écrivez pas à côté du type, comme dans :

```cpp
int* p ;
```

## Les variables

Parce que CS50 utilise [C99](http://en.wikipedia.org/wiki/C99), ne définissez pas toutes vos variables tout en haut de vos fonctions, mais plutôt quand et où vous en avez réellement besoin. De plus, limitez la portée de vos variables autant que possible. Par exemple, si « i » n’est nécessaire que pour une boucle, déclarez « i » dans la boucle elle-même :

```cpp
for (int i = 0 ; i < LIMITE ; i++)
{
    printf("%i\n", i) ;
}
```

Bien qu’il soit acceptable d’utiliser des variables comme « i », « j » et « k » pour l’itération, la plupart de vos variables doivent avoir un nom plus spécifique. Si vous additionnez certaines valeurs, par exemple, appelez votre variable « somme ». Si le nom de votre variable nécessite deux mots (par exemple, « est_prêt »), mettez un tiret bas entre eux, une convention courante en C mais moins dans d’autres langages.

Si vous déclarez plusieurs variables du même type à la fois, il est possible de les déclarer ensemble, comme dans :

```cpp
int quarts, dimes, nickels, pennies ;
```

N’initialisez pas certaines variables mais pas d’autres, comme dans :

```cpp
int quarts, dimes = 0, nickels = 0 ; // pennies ;
```

Veillez également à déclarer les pointeurs séparément des non-pointeurs, comme dans :

```cpp
int *p ;
int n ;
```

Ne déclarez pas les pointeurs sur la même ligne que les non-pointeurs, comme dans :

```cpp
int *p, n ;
```

## Structures

Déclarez une « struct » comme un type, avec chaque accolade sur sa propre ligne et des membres indentés, avec le nom du type également sur sa propre ligne :

```cpp
typedef struct
{
    string nom ;
    string dortoir ;
}
etudiant ;
```

Si la « struct » contient comme membre un pointeur vers une telle « struct », déclarez la « struct » avec un nom identique au type, sans utiliser de tiret bas :

```cpp
typedef struct node
{
    int n ;
    struct node *suivant ;
}
node ;
```

