#include<stdio.h>
#include<stdlib.h>
int main()
{
        int i,n;
        char *p;
        printf("Enter the size : ");
        scanf("%d",&n);
        p=(char *)malloc(n+2*sizeof(char));
        printf("Enter the plain text : ");
        scanf(" %[^\n]",p);
key:    printf("Enter the key between 0-9 : ");
        scanf("%d",&n);
        if(!((n>=1)&&(n<=10)))
        {
                printf("Enter the key between 0-9\n");
                goto key;
        }
        for(i=0;p[i];i++)
                p[i]=p[i]+n;
        p[i++]=n+97;
        p[i]='\0';
        printf("%s\n",p);
        return 0;
}
