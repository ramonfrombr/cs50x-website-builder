// Récupère la saisie d'une chaîne de manière non sécurisée avec scanf

#include <stdio.h>

int main(void)
{
    char s[5];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}