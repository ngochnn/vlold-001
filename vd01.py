#include<stdio.h>
#include<conio.h>
#include<math.h>
 
int main ()
{   clrscr ();
    float a,b,c;
    printf("Nhap a:");
    scanf("%f",&a);
    printf("Nhap b:");
    scanf("%f",&b);
    printf("Nhap c:");
    scanf("%f",&c);
    if ( a+b > c || b+c>a || c+a>b)
    {
        if ( a*a + b*b == c*c || b*b + c*c == a*a || c*c + a*a == b*b)
        {
            printf("\n 3 so ban vua nhap la do dai 3 canh cua 1 tam giac vuong");
        }
        else
        {
            if( a== b==c)
            {
                printf("\n 3 so ban vua nhap la do dai 3 canh cua 1 tam giac deu");
            }
            else
            {
            if(a*a > b*b + c*c || b*b > a*a + c*c || c*c > a*a + b*b)
            {
                printf("\n 3 so ban vua nhap la do dai 3 canh cua 1 tam giac tu");
            }
            else
            {
                printf("\n 3 so ban vua nhap la do dai 3 canh cua 1 tam giac nhon");
            }
            }
        }
    }
    else
    {
    printf("\n Ba so ban vua nhap ko phai la do \
       dai 3 canh cua 1 tam giac");
    }
    getch ();
    return 0;
}
