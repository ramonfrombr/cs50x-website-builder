# [NOM](#name)

printf - imprimer à l'écran

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    int printf(char* format, ...);

Notez que `...` représente zéro ou plusieurs arguments supplémentaires.

# [DESCRIPTION](#description)

Cette fonction imprime une "chaîne formatée" à l'écran. Elle attend en entrée une "chaîne de format" qui spécifie ce qu'il faut imprimer et zéro ou plusieurs arguments ultérieurs. La chaîne de format peut éventuellement contenir des "spécifications de conversion", des espaces réservés qui commencent par `%` et qui spécifient comment formater les arguments ultérieurs de la fonction, le cas échéant. Par exemple, si `c` est de type `char`, cette fonction peut l'imprimer de la manière suivante en utilisant `%c`:

    printf("%c\n", c);

Alternativement, cette fonction pourrait également formater cette même valeur en tant qu'`int` en utilisant `%i`, comme dans un tableau ASCII:

    printf("%c %i\n", c, c);

Et cette fonction peut également imprimer des chaînes sans aucune spécification de conversion:

    printf("hello, world\n");

Parmi les spécifications de conversion prises en charge par cette fonction, on trouve:

| Spécification de Conversion | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `string` |

Pour imprimer un signe pourcent réel, utilisez `%%`.

Pour spécifier la "précision" d'un `float` ou d'un `double`, `%f` peut éventuellement contenir un `.` après le `%` suivi d'un nombre de décimales. Par exemple, cette fonction pourrait formater la valeur d'un tiers à une décimale en utilisant `%.1f`:

    printf("%.1f\n", 1.0 / 3.0);

# [VALEUR DE RETOUR](#return-value)

Cette fonction renvoie le nombre de caractères imprimés.

# [EXEMPLES](#examples)

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        string s = "This is CS50";
        printf("%s\n", s);

        int i = 50;
        printf("This is CS%i\n", i);

        float f = 50.0;
        printf("This is CS%.0f\n", f);
    }