#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // int list[3];

    // list[0] = 1;
    // list[1] = 2;
    // list[2] = 3;

    // for (int i = 0; i < 3; i++)
    // {
    //   printf("%i\n", list[i]);
    // }

    int *list = malloc(3 * sizeof(int)); // other way to create an array of ints
    if (list == NULL)
    {
        return 1;
    }

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // assume you want to add another integer to the original list (but you can't)
    // reallocate memory into existing variable that has already been allocated
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    tmp[3] = 4; // add new number to list

    free(list); // "delete" original list

    list = tmp; // reuse original variable

    // prove that list has a 4th integer now
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }
    
    free(list);
}