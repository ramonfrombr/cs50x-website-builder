// Simuler l'hérédité génétique du groupe sanguin

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Chaque personne a deux parents et deux allèles
typedef struct personne
{
    struct personne *parents[2];
    char allèles[2];
}
personne;

const int GENERATIONS = 3;
const int LONGUEUR_RETRAIT = 4;

personne *créer_famille(int générations);
void afficher_famille(personne *p, int génération);
void libérer_famille(personne *p);
char allèle_aléatoire();

int main(void)
{
    // Initialiser le générateur de nombres aléatoires
    srand(time(0));

    // Créer une nouvelle famille avec trois générations
    personne *p = créer_famille(GENERATIONS);

    // Afficher l'arbre généalogique des groupes sanguins
    afficher_famille(p, 0);

    // Libérer la mémoire
    libérer_famille(p);
}

// Créer un nouvel individu avec `générations`
personne *créer_famille(int générations)
{
    // TODO: Allouer de la mémoire pour la nouvelle personne

    // S'il reste encore des générations à créer
    if (générations > 1)
    {
        // Créer deux nouveaux parents pour la personne actuelle en appelant récursivement créer_famille
        personne *parent0 = créer_famille(générations - 1);
        personne *parent1 = créer_famille(générations - 1);

        // TODO: Définir les pointeurs de parent pour la personne actuelle

        // TODO: Assigner aléatoirement les allèles de la personne actuelle en fonction des allèles de leurs parents

    }

    // S'il ne reste plus de générations à créer
    else
    {
        // TODO: Définir les pointeurs de parent à NULL

        // TODO: Assigner aléatoirement les allèles

    }

    // TODO: Retourner la personne nouvellement créée
    return NULL;
}

// Libérer `p` et tous les ancêtres de `p`.
void libérer_famille(personne *p)
{
    // TODO: Gérer le cas de base

    // TODO: Libérer les parents de manière récursive

    // TODO: Libérer l'enfant

}

// Afficher chaque membre de la famille et leurs allèles.
void afficher_famille(personne *p, int génération)
{
    // Gérer le cas de base
    if (p == NULL)
    {
        return;
    }

    // Afficher le retrait
    for (int i = 0; i < génération * LONGUEUR_RETRAIT; i++)
    {
        printf(" ");
    }

    // Afficher la personne
    if (génération == 0)
    {
        printf("Enfant (Génération %i) : groupe sanguin %c%c\n", génération, p->allèles[0], p->allèles[1]);
    }
    else if (génération == 1)
    {
        printf("Parent (Génération %i) : groupe sanguin %c%c\n", génération, p->allèles[0], p->allèles[1]);
    }
    else
    {
        for (int i = 0; i < génération - 2; i++)
        {
            printf("Grand-");
        }
        printf("Grand-parent (Génération %i) : groupe sanguin %c%c\n", génération, p->allèles[0], p->allèles[1]);
    }

    // Afficher les parents de la génération courante
    afficher_famille(p->parents[0], génération + 1);
    afficher_famille(p->parents[1], génération + 1);
}

// Choisit aléatoirement un allèle de groupe sanguin.
char allèle_aléatoire()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}