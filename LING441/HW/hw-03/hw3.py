#!/usr/bin/python
# Homework 3
# Zijie Ku

# 1. Define a function called splice that takes two strings. 
# It should return a string consisting of the first half of the first string
# and the second half of the second string. Tip: int(x) drops the fractional
# part of x and returns an integer. Example:
# >>> splice('dogfish', 'fishfood')
# >>> 'dogfood'
def splice(first, second):
	return first[:int(len(first)/2)] + second[int(len(second)/2):]

# 2. Define a function called scrunch that takes a string s and returns a 
# length-two string consisting of the first and last letters of s. However,
# if the input string is less than two letters long, scrunch should just 
# return the original string. Examples:
# >>> scrunch('dog')
# >>> 'dg'
# >>> scrunch('a')
# >>> 'a'
def scrunch(str):
	return str if (len(str) < 2) else (str[0] + str[-1])

# 3. Write a function add_s that takes a word (i.e., a string) as input, 
# and returns the word with s added to the end. However, if the word ends
# in s, z, sh, or ch, the ending should be es. Example:
# >>> add_s('dog')
# >>> 'dogs'
# >>> add_s('fish')
# >>> 'fishes'
def add_s(str):
	if((str[-1]=='s') | (str[-1]=='z') | (str[-2:]=='sh') | (str[-2:]=='ch')):
		return str + 'es'
	else:
		return str + 's'

# 4. Write a function is_plural that takes a workd as input, and returns True
# or False depending on whether the word is plural or not. Consider a word to be
# plural if it ends in s, unless the word ends in ss or us, in which case it is
# not plural. Return False for all single-letter words. Examples:
# >>> is_plural('dogs')
# >>> True
# >>> is_plural('campus')
# >>> False
# >>> is_plural('s')
# >>> False
def is_plural(str):
	if(len(str) < 1):
		return False
	if((str[-1]=='s') & (str[-2:]!='ss') & (str[-2:]!='us') & (len(str)!=1)):
		return True
	else:
		return False 

# 5. Write a function make_np that takes a word w and returns a two-element
# list consisting of 'the' followed by w. Then write a function make_sentence
# that takes three words: subject, verb, and object. It should return a list 
# in which the subject and object have been turned into noun phrases, and the
# verb form has been modified to match the subject. Specically, 'the' should
# be inserted before the subject and before the object, and s should be added
# to the verb if the subject is singular, but not if the subject is plural.
# In the definition of make_sentence, you MUST call the function is_plural, 
# add_s, and make_np. Examples:
# >>> make_sentence('dogs', 'chase', 'cat')
# >>> ['the', 'dogs', 'chase', 'the', 'cat']
# >>> make_sentence('cat', 'scratch', 'sofa')
# >>> ['the', 'cat', 'scratches', 'the', 'sofa']
# You may assume that the input verb is in the plural form (no ending)

def make_np(w):
	return ['the', w]

def make_sentence(subj, v, obj):
	return make_np(subj) + ([add_s(v)] if (not is_plural(subj)) else [v]) + make_np(obj)

# For each of the questions 6-11, you must write a LIST COMPREHENSION. The
# Answer will not count as correct unless you use a list comprehension to 
# obtain it. Set:
# mytext = 'This is a test ; it is only a test . It is not a pipe .'.split()
mytext = 'This is a test ; it is only a test . It is not a pipe .'.split()

# 6. Define a function called vocab that takes a text or list, eliminates 
# duplicates, discards numbers and punctuation (anything that is not purely
# alphabetic), and maps uppercase to lowercase. The return value should
# be a set. Then do:
# V = vocab(mytext)
# If you have done it right, the set V will contian eight elements
def vocab(text):
	return set((w.lower() for w in text if w.isalpha()))

V = vocab(mytext)

# 7. Get the list of four-letter words from V, put them in alphabetic order,
# and store the result in A7.
A7 = sorted([ v for v in V if (len(v) == 4) ])

# 8. Get the list of words from V that begin and end with the same letter,
# sorted alphabetically. Single-letter words are allowed. Store the result in A8
A8 = sorted([ v for v in V if v[0] == v[len(v)-1] ])

# 9. Define a function called acronym that takes a string, splits it into words,
# and returns a string consisting of the intial letters of the words. For 
# example:
# >>> acronym('International Business Machines')
# >>> 'IBM'
# >>> acronym('Lord of the Rings')
# >>> 'LotR'
def acronym(str):
	return ''.join([s[0] for s in str.split()])

# 10. This question has two steps. You only need to use a list comprehension
# in the second step.
# a. There is a function called reversed that iterates over the characters of 
#    a string or the elements of a list in reverse order. It returns a generator
#    which we can turn into a list:
#    >>> list( reversed('wolf'))
#    >>> ['f', 'l', 'o', 'w']
# A palindrome is a word that is written the same forward and backward. That is,
# reversing it does not change it. Define a function called is_palindrome that
# takes a word w and returns True if w is a palindrome and False if not. 
# For example:
# >>> is_palindrome('wolf')
# >>> False
# >>> is_palindrome('bob')
# >>> True
def is_palindrome(w):
	return(w == ''.join(list(reversed(w))))

# b. Set M = vocab(text1). Get the list of palindromes that occur in M, sorted
# alphabetically, and store the result in A10.
import nltk
from nltk.book import *
M = vocab(text1)
A10 = sorted(list( m for m in M if is_palindrome(m) ))

# 11. Define a word w to be reversible if w written backwards is also a word.
# Set A11 to the list of reversible words in M, sorted alphabetically.
A11 = list(sorted(w for w in M if (''.join(reversed(w)) in M )))


# We will often have occasion to print tables. For example, suppose we want to
# print a table of strings with their lengths.
# >>> words = ['hi', 'there', 'cat']
# >>> for w in words:
# ...   print(w, len(w))
# >>> hi 2
# >>> there 5
# >>> cat 3
# To improve readability, we would like to have the first column be five 
# characters wide all the way down. The method format will pad strings with
# spaces to make them be the right width:
# >>> '{:5}--{:1}'.format('cat', 2)
# >>> 'cat   --2'
# In the format string, each pair of braces corresponds to one argument. 
# Characters outside of the braces are preserved as they stand. Thus:
# >>> for w in words:
# ...   print('{:5} {:1}'.format(w, len(w)))
# hi    2
# there 5
# cat   3
# You can get right alightment of strings by inserting > before the field width:
# >>> for w in words:
# ...   print('{:>5} {}'.format(w, len(w)))
# >>>    hi 2
# >>> there 5
# >>>   cat 3


# 12. Write a function called text_table that takes a list of texts and prints 
# out a table in which the first column contains the text name, the second 
# column contains the number of tokens in the text, and the third column 
# contains the number of types. The first column should have width 55, the 
# second has width 6, and the third column has width 5. You should also print a 
# header line containing the words ’TITLE’, ’#TOK’, and ’#TYP’. Use the format 
# method for the header line as well, and right-align the header strings for the 
# last two columns. Here is an example of the output:
# >>> text_table([text1, text2, text3])
# TITLE                                                              #TOK  #TYP
# Moby Dick by Herman Melville 1851 							   260819 19317
# Sense and Sensibility by Jane Austen 1811 						44764  2789
# The Book of Genesis  											   141576  6833

def text_table(texts):
	print('{:55} {:>6} {:>5}'.format('TITLE', '#TOK', '#TYP'))
	for t in texts:
		print('{:55} {:>6} {:>5}'.format(t.name, len(t), len(set(t))))

