// Compare deux chaines en utilisant strcmp

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtenir deux chaines
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Comparer les chaines
    if (strcmp(s, t) == 0)
    {
        printf("Identique\n");
    }
    else
    {
        printf("Différent\n");
    }
}