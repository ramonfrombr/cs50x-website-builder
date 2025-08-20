// get_int y printf con %i

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int age = get_int("¿Cuál es tu edad?\n");
    printf("Tienes al menos %i días de edad.\n", age * 365);
}