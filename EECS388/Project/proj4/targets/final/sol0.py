'''
Since we know that char grade[5] is created on the stack
earlier than name[10], it has a starting memory address larger
than name. Hence, whatever that is written in name via stdin
could overwrite the data in grade by buffer overflow.
This assumes that memory address used are not randomized.
Using "kuzijie" as an example. It has 7 chars. and we can 
append 3 null characters and overwrite the data in grade with A+.
'''
print "kuzijie"+"\x00"*3+"A+\0" 
