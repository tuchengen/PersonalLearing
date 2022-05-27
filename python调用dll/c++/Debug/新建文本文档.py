import ctypes as C

dll = C.cdll.LoadLibrary('Project2.dll')


p_str = C.c_char_p(b'hello')
str_length1 = dll.get_str_length(p_str)
print (str_length1)

get_str_length = dll.get_str_length
get_str_length.argtypes = [C.c_char_p]
get_str_length.restype = C.c_int
str_length2 = get_str_length(p_str)
print (str_length2)
