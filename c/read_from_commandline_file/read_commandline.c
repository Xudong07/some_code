/*************************************************************************
    > File Name: read_commandline.c
    > Author: Xudong Duan
    > Mail: duanxudong12014401@163.com 
    > Created Time: 2020年07月12日 星期日 14时44分19秒
 ************************************************************************/
/*
code for reading from stdin or command line
*/
#include<stdio.h>
#include<stdlib.h>
#define STLEN 10
int main(int argc, char * argv[])
{
    int i,j,k;
    double f, y;
    double grade;
    char * name;
    char words[STLEN];
    // test command line: char and number (int or double)
    /*
    we can translate number to char with sprintf
    */
    name = argv[1];
    i = atoi(argv[2]);
    grade = atof(argv[3]);
    printf("there are %d command line arguments\n", argc);
    printf("the program name is : %s\n", argv[0]);
    printf("the chars of %s should be printed %d times\n", name, i);
    for (j=0;j<i;j++)
        puts(name);
    printf("%s's grade is %lf\n",name, grade);
    //test read from stdin or file (number) scanf in loop
    puts("Now, read data from stdin using scanf");
    while(scanf("%d %lf %d %lf", &i, &f, &j, &y)==4)
    {
        printf("%d, %lf, %d, %lf\n", i, f, j, y);
        // 跳过本行剩余的字符
        while(getchar()!='\n')
            continue;
    }
    //scanf will give the wrong input back to the input

    while (getchar()!='\n')
    {
        continue;
    }  
    // test read from stdin or file (chars)  gets;puts/ fgets;fputs/ gets_s;s_gets()
    /*
    scanf and gets are not good
    using fgets
    fgets will store the '\n', and stop @ max number
    */
   puts("Now, read data from stdin using fgets");
   while (fgets(words, STLEN, stdin)!=NULL && words[0]!='\n')
   {
       //remove \n from words
       i = 0;
        while (words[i]!='\0' && words[i]!='\n')
            i++;
        if(words[i]=='\n')
            words[i] = '\0';
        else
        {
            // there is no \n in the chars, which mean that the length of input chars is longer than STLEN，We need to remove the data in the following input line
            while(getchar()!='\n')
                continue;
        }
        puts(words);
   }
    //test read from stdin (chars)
    return 0;
}
