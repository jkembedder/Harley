#include<stdio.h>
#include<stdlib.h>
int main()
{
        int i,n;
        char *p;
        printf("Enter the size : ");
        scanf("%d",&n);
        p=(char *)malloc(n+1*sizeof(char));
        printf("Enter the cyper text : ");
        scanf(" %[^\n]",p);
        n=p[n-1]-97;
        for(i=0;p[i+1];i++)
                p[i]=p[i]-n;
        p[i]='\0';
        printf("%s\n",p);
        return 0;
}
