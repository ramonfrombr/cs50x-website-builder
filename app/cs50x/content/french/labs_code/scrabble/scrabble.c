#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points attribués à chaque lettre de l'alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int calculer_points(string mot);

int main(void)
{
    // Obtenir les mots entrés par les deux joueurs
    string mot1 = get_string("Joueur 1 : ");
    string mot2 = get_string("Joueur 2 : ");

    // Calculer les points des deux mots
    int score1 = calculer_points(mot1);
    int score2 = calculer_points(mot2);

    // TODO: Imprimer le gagnant
}

int calculer_points(string mot)
{
    // TODO: Calculer et retourner les points du mot
}