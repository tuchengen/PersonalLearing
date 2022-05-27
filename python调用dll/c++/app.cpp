#include <iostream>
extern "C" __declspec(dllexport) int get_str_length(char* str);
extern "C" __declspec(dllexport) char* back_str(char* str);
int get_str_length(char* in_str)
{
    std::string str(in_str);
    printf(in_str);
    return str.length();
}

char* back_str(char* in_str)
{
    char* out_str;
    out_str = (char*)("2kkkkkkkk込込込込込");
    return out_str;
}
