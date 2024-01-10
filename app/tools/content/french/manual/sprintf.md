# [NOM](#nom)

sprintf - imprimer dans une chaîne

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    int sprintf(char *str, const char *format, ...);

Notez que `...` représente zéro ou plusieurs arguments supplémentaires.

# [DESCRIPTION](#description)

Cette fonction imprime une "chaîne formatée" à un emplacement dans la mémoire. Elle attend en entrée l'adresse d'un tampon (qui doit être suffisamment grand pour contenir la chaîne, y compris son `\0`), une "chaîne de format" qui spécifie ce qui doit être imprimé, et zéro ou plusieurs arguments subséquents. La chaîne de format peut éventuellement contenir des "spécifications de conversion", des espace réservés qui commencent par `%` et qui spécifient comment formatter les arguments subséquents de la fonction, le cas échéant. Par exemple, si `buffer` est un tableau d'au moins 13 octets et `i` vaut `50`, cette fonction pourrait formatter une chaîne comme suit :

    sprintf(buffer, "bonjour, %s\n", i);

Parmi les spécifications de conversion supportées par cette fonction, on trouve :

| Spécification de conversion | Type     |
| -------------------------- | -------- |
| `%c`                       | `char`   |
| `%f`                       | `double` |
| `%f`                       | `float`  |
| `%i`                       | `int`    |
| `%li`                      | `long`   |
| `%s`                       | `char *` |

Pour imprimer un signe de pourcentage réel, utilisez `%%`.

Pour spécifier la « précision » d'un `float` ou d'un `double`, `%f` peut éventuellement contenir un `.` après le `%`, suivi d'un nombre de décimales. Par exemple, cette fonction pourrait formatter la valeur d'un tiers à une décimale près en utilisant `%.1f`, en supposant que `buffer` est un tableau de taille 4 (au moins) :

    sprintf(buffer, "%.1f\n", 1.0 / 3.0);

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie le nombre de caractères imprimés.

# [EXEMPLES](#exemples)

    #include <stdio.h>

    int main(void)
    {
        char buffer[13];

        int i = 50;
        sprintf(buffer, "Ceci est l'informatique %i", i);
        printf("%s\n", buffer);

        float f = 50.0;
        sprintf(buffer, "Ceci est l'informatique %.0f", f);
        printf("%s\n", buffer);
    }