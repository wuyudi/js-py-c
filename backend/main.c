// gcc -c main.c
// gcc -shared -o main.dll main.o
#include <stdio.h>
// https://cygwin.com/cygwin-ug-net/dll.html
char *return_char_p()
{
    return "Hello World!\n";
}
int return_int()
{
    return 1;
}
int return_int_add(int num)
{
    return num + 1;
}