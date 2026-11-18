#include <stdio.h>
int main()
{
    int a, b, choice;
    printf("simple calculator\n");
    printf("1.addition\n");
    printf("2.subtraction\n");
    printf("3.multiplication\n");
    printf("4.division\n");
    printf("enter your choice:");
    scanf("%d", &choice);
    printf("enter two numbers:");
    scanf("%d%d",&a,&b);
    switch(choice)
    {
        case 1: 
        printf("addition=%d",a+b);
        break;
        case 2:
        printf("subtraction= %d",a-b);
        break;
        printf("multiplication =%d",a*b);
        break;
        case 4:
        if(b==0)
        {
            printf("error:division by zero is not allowed.");
        }
        else
        {
            printf("division = %.2f",(float)a/b);
        }
        break;
        default:
        printf("invalid choice!");
    }
    return 0;
}