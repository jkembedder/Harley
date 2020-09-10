#include<stdio.h>
#include<stdlib.h>
void main(int argc,char *argv[])
{
  char ch;
  int i=0;
  FILE *fp = fopen(argv[1],"r");
  while((ch = fgetc(fp))!=EOF)
        i++;i++;
  char *buf = (char *)malloc(i*sizeof(char));
  rewind(fp);
  i=0;
  while((ch = fgetc(fp))!=EOF)
  {
          if(ch == '    ')
           continue;
          else
           buf[i++] = ch;
  }
  buf[i] = '\0';
  fclose(fp);

  fp = fopen(argv[1],"w");

  for(i=0;buf[i];i++)
          fputc(buf[i],fp);
  fclose(fp);
}
