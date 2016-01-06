#!/usr/bin/python

print "hello world"

fileref = open('sample.txt','r')


a = fileref.readlines()
print(a)

fileref.close()
