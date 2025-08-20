// get_string et printf avec %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("Quel est votre nom ?\n");
    printf("bonjour, %s\n", s);
}