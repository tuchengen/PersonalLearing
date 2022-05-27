from base64 import encode
import ctypes as C
from pickletools import bytes_types

dll = C.cdll.LoadLibrary('Project2.dll')

p=bytes("涂成恩",encoding="gbk")
p_str = C.c_char_p(p)
# str_length1 = dll.get_str_length(p_str)
# print (str_length1)

back_str = dll.back_str
back_str.argtypes = [C.c_char_p]
back_str.restype = C.c_char_p
str_length2 = back_str(p_str)
print (str_length2.decode('gbk'))
# print(pp)