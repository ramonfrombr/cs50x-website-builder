// get_float et printf avec %f

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float prix = get_float("Quel est le prix ?\n$");
    printf("Votre total est de %.2f $.\n", prix * 1,0625);
}