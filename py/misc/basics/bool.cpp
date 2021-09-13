#include <stdio.h>

int main(void)
{

    if(0 == false)
    {
        printf("0 == false is True\n");
    }
    else
    {
        printf("0 == false is False\n");
    }

    if(1 == true)
    {
        printf("1 == true is True\n");
    }
    else
    {
        printf("1 == true is False\n");
    }

    if(5 == true)
    {
        printf("5 == true is True\n");
    }
    else
    {
        printf("5 == true is False\n");
    }

    if(0)
    {
        printf("0 is True\n");
    }
    else
    {
        printf("0 is False\n");
    }



    if(5)
    {
        printf("5 is True\n");
    }
    else
    {
        printf("5 is False\n");
    }

    printf("Numerical value of false : %d\n", false);
    printf("Numerical value of true : %d\n", true);





    return 0;

}
