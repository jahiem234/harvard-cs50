#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;

    do
    {
        cents = get_int("changed owe:  ");
    }
    while (cents < 1);

    int coins = 0;

    coins += cents / 25;
    cents %= 25;

    coins += cents / 10;
    cents %= 10;

    coins += cents / 5;
    cents %= 5;

    coins += cents;

    printf("%i\n", coins);
}
