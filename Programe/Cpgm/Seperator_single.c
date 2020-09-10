#include<stdio.h>
#include<stdlib.h>
void main(int argc,char *argv[])
{
  char ch,name[] = "1.c";
  FILE *fp = fopen(argv[1],"r");
  FILE *fn = fopen(name,"w");
  while((ch = fgetc(fp))!=EOF)
  {
        if((ch>='0')&&(ch<='9'))
        {
          name[0] = ch;
          ch = fgetc(fp);
          if(ch == ')')
          {
            fclose(fn);
            fn = fopen(name,"w");
            fputs("#include<stdio.h>\n",fn);
          }
          else
          {
            fseek(fp,-2,SEEK_CUR);
            ch = fgetc(fp);
            goto put;
          }
       }
       else
       {
put:     if(ch == '     ')
           continue;
         else
           fputc(ch,fn);
       }
  }
  fclose(fn);
  fclose(fp);
}
