// Détermine la longueur d'une chaîne

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Invite l'utilisateur à entrer son nom
    string s = get_string("Nom : ");

    // Compte le nombre de caractères jusqu'à '\0' (ou NUL)
    int n = 0;
    while (s[n] != '\0')
    {
        n++;
    }
    printf("%i\n", n);
}