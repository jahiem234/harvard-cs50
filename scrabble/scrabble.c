#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int score(string w)
{
    int s = 0;
    for (int i = 0; w[i]; i++)
        if (isalpha(w[i]))
            s += POINTS[toupper(w[i]) - 'A'];
    return s;
}

int main(void)
{
    string w1 = get_string("player 1: ");
    string w2 = get_string("player 2: ");
    int s1 = score(w1), s2 = score(w2);

    if (s1 > s2)
        printf("player 1 wins!\n");
    else if (s2 > s1)
        printf("player 2 wins!\n");
    else
        printf("tie!\n");
}
