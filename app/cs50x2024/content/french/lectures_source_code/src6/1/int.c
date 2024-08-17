// get_int et printf avec %i

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int age = get_int("Quel âge avez-vous ?\n") ;
    printf("Vous avez au moins %i jours.\n", age * 365) ;
}