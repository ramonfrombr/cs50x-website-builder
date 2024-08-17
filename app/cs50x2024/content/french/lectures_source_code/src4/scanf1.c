// Obtient incorrectement une chaîne de la part de l'utilisateur à l'aide de scanf

#include <stdio.h>

int main(void)
{
    char *s;
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}