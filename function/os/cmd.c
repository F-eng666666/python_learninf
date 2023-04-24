#include <stdio.h>
#include <windows.h>

int main(int argc, char **argv)
{
    for (int i = 3; i; i--)
    {
        printf("hello,os.system\n");
        Sleep(1000); // ms
        fflush(stdout);
    }

    return 66;
}