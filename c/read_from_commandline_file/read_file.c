/* 除了重定向以外的高级io函数
stdin is the file for scanf, getchar, stdout is the file for putchar(), puts(), printf()*/
#include<stdio.h>
#include<stdlib.h>
#define STLEN 10
int main(int argc, char * argv[]){
    FILE * fp;
    int i,j,k;
    double f,y;
    char name[STLEN];
    char * fname, *fname1;
    fname = argv[1];
    fname1 = argv[2];
    printf("the file name is: %s\n", fname);
    //read number from file
    if((fp=fopen(fname, "r"))==NULL)
    {
        printf("there is error in reading the file: %s\n", fname);
        exit(EXIT_FAILURE);
    }
    //read number from file
    fscanf(fp, "%d %lf %d %lf", &i, &f, &j, &y);
    while (feof(fp)==0)
    {
        printf("%d, %lf, %d, %lf\n", i,f,j,y);
        fscanf(fp, "%d %lf %d %lf", &i, &f, &j, &y);
    }
    if(fclose(fp)!=0)
    {
        printf("there is error in closing the file: %s\n", fname);
    }


    //read chars from file
    printf("the file name is: %s\n", fname1);
    if((fp=fopen(fname1, "r"))==NULL)
    {
        printf("there is error in reading the file: %s\n", fname);
        exit(EXIT_FAILURE);
    }
    while (1)
    {
        fgets(name, STLEN, fp);
        if(feof(fp)!=0)
            break;
        //remove \n from name
        i=0;
        while(name[i]!='\n' && name[i]!='\0')
            i++;
        if(name[i]=='\n')
            name[i] = '\0';
        else
        {
            while (getc(fp)!='\n'&&feof(fp)==0)
            {
                continue;
            }
        }
        printf("%s\n", name);
    }
    if(fclose(fp)!=0)
    {
        printf("there is error in closing the file: %s\n", fname1);
    }
    return 0;
}
