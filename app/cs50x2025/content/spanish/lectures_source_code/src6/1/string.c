// get_string y printf con %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("¿Cuál es tu nombre?\n");
    printf("hola, %s\n", s);
}