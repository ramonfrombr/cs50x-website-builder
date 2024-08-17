# [NOM](#name)

fscanf - obtenir une entrée à partir d'un fichier

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    int fscanf(FILE *stream, const char *format, ...);

Notez que `...` représente zéro ou plusieurs arguments supplémentaires.

# [DESCRIPTION](#description)

Cette fonction "scanne" un fichier pour des valeurs de types spécifiés. Elle attend en entrée le pointeur d'un `FILE` qui a été renvoyé par [fopen](fopen), une "chaîne de format" qui spécifie ce à quoi s'attendre, et zéro ou plusieurs arguments ultérieurs, chacun devant être un emplacement en mémoire. La chaîne de format devrait contenir des "spécifications de conversion", des espaces réservés qui commencent par `%` et qui spécifient quels types de valeurs attendre. Les arguments ultérieurs se verront attribuer ces valeurs. Par exemple, si `n` est un `int`, cette fonction peut obtenir un `int` de l'utilisateur en utilisant `%i` :

    scanf("%i", &n);

Parmi les spécifications de conversion prises en charge par cette fonction, on trouve :

| Spécification de conversion | Type     |
| -------------------------- | -------- |
| `%c`                       | `char`   |
| `%f`                       | `double` |
| `%f`                       | `float`  |
| `%i`                       | `int`    |
| `%li`                      | `long`   |

Pour obtenir un seul mot (c'est-à-dire une séquence de caractères sans espaces), utilisez `%s`. Mais il est sécuritaire d'utiliser cette fonction pour obtenir un mot à partir d'un fichier en utilisant `%s` seulement si ce mot a une longueur maximale définie. Par exemple, si `file` est un pointeur vers un `FILE` qui a été renvoyé par [fopen](fopen) et que `buffer` est un tableau de 3 octets, cette fonction pourrait être utilisée pour obtenir `"hi"`, y compris son `'\0'`, mais pas `"hi!"`, comme suit :

    fscanf(file, "%s", buffer);

# [VALEUR DE RETOUR](#return-value)

Cette fonction renvoie le nombre d'arguments auxquels des valeurs ont été attribuées ou `EOF`, une constante définie dans `stdio.h`, si la fin du fichier a été atteinte.

# [EXEMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("hi.txt", "r");
        if (file != NULL)
        {
            char buffer[3];
            fscanf(file, "%s", buffer);
            fclose(file);
            printf("%s\n", buffer);
        }
    }