#!/usr/bin/python
# Homework 2
# Zijie Ku

# 1. Set x to 1812, then compute 16 times the sum of x and 120 (and Set A1 to 
# the result).
x = 1812
A1 = 16 * (x + 120)

# 2. Get the fourth token of text1. (Fourth counting from 1 in the usual way, 
# e.g., "d" in the list ["a", "b", "c", "d"]. Note: a text behaves just like a 
# list containing strings, each string representing one word token. Also, you 
# will of course need an import statement to get access to text1.)

import nltk
from nltk.book import *
A2 = text1[3]

# 3. Get the last token of text1
A3 = text1[-1]

# 4. Concatenate the strings "sing" and "er"
A4 = "sing" + "er"

# 5. Concatenate the string "la" with itself three times. (I.e., the result 
# should be "lalala".) The literal "la" shuold appear in your expression only 
# once.
A5 = "la" * 3

# 6. Define words to be a list whose elements are 'dog', 'cat', 'fish', and 
# 'diplodocus'. Concatenate its second and third elements (counting from 1)
words = [ 'dog', 'cat', 'fish', 'diplodocus' ]
A6 = words[1] + words[2]

# 7. Determine whether or not the fourth word in words (counting from 1) is at 
# least 7 letters long. (The result will be either True or False.)
A7 = len( words[3] ) >= 7 

# 8. Determing whether the third word in words (counting from 1) is longer than
# the second word.
A8 = len( words[2] ) > len( words[1] )

# 9. Determine whether the first letter of the first word in words is the same
# as the first letter of the last word.
A9 = words[0][0] == words[-1][0]

# 10. Get the sublist consisting of just the second and third words of words 
# (counting from 1). Use a slice.
A10 = words[ 1 : 3]

# 11. Let s be the string 'garnish'. Create a list whose first element is the 
# first letter of s, whose second element is the next-to-last letter of s, and 
# whose third element is the length of s.
s = 'garnish'
A11 = [ s[0], s[1:len(s)], len(s)]

# 12. Let the value of w be the string "serendipity". Write an expression whose
# value is "tyre". Your expression should contain the variable w, but it should
# not contain any string literals. Use slices.
w = "serendipity"
A12 = w[-2:] + w[2:4]

# 13. Determine wheter 'monstrous' occurs more frequently in Moby Dick (text1) 
# than it does in Sense and Sensibility (text2). Write an expression that 
# compares the counts and returns True or False.
A13 = text1.count('monstrous') > text2.count('monstrous')

# 14. Turn the sentence 'this is a test' into a list of words.
A14 = "this is a test".split()

# 15. Turn the spelled word ['f', 'r', 'o', 'd', 'o'] into a string.
A15 = ''.join(['f', 'r', 'o', 'd', 'o'])

# 16. Take the sequence of 10 tokens in Moby Dick beginning at position 1000
# (counting from 0), and turn them into a string, with words separated by
# spaces.
A16 = ' '.join(text1[999: 999 + 10])

# 17. Determine whether or not Moby Dick contains the word 'vestibule'. 
# The result should be True or False.
A17 = 'vestibule' in text1[:]

# 18. Set s1 = 'this is a test' and set s2 = 'here is another test'. Determine
# which words s1 and s2 have in common. The result should be a set.
s1 = 'this is a test'
s2 = 'here is another test'
A18 = set( s1.split() ) & set( s2.split() ) 

# 19. Determine how many word types are found in Sense and Sensibility but
# not in Moby Dick. The result is the number of word types. 
A19 = len( set( text2 ) - set( text1 ) )

# Print Solutions:
print('Q1:',  A1)
print('Q2:',  A2)
print('Q3:',  A3)
print('Q4:',  A4)
print('Q5:',  A5)
print('Q6:',  A6)
print('Q7:',  A7)
print('Q8:',  A8)
print('Q9:',  A9)
print('Q10:', A10)
print('Q11:', A11)
print('Q12:', A12)
print('Q13:', A13)
print('Q14:', A14)
print('Q15:', A15)
print('Q16:', A16)
print('Q17:', A17)
print('Q18:', A18)
print('Q19:', A19)
