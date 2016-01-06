#!/usr/bin/python
# Homework 1
# Zijie Ku

# 1. Set A1 to the result of adding two and two
A1 = 2 + 2

import nltk
from nltk.book import *
# 2. How many tokens does the Book of Genesis contain? Set A2 to the answer.
A2 = len(text3)

# 3. How many types does Genesis contain? Set A3 to the answer.
A3 = len(set(text3))

# 4. How many times does the word heavens occur in Genesis? Set gen_ct to the 
# answer. Also, set moby_ct to the number of times heavens appears in Moby Dick. 
gen_ct = text3.count('heavens')
moby_ct = text1.count('heavens') 

# 5. Set A5 to the lexical diversity of Genesis. You will need to include the 
# definition of lexical_diversity in hw1.py.
def lexical_diversity(text):
  return len(set(text)) / len(text)

A5 = lexical_diversity(text3)

# 6. Write a function ppm that takes two numbers count and total and returns 
# the count expressed as parts per million. For example, 2 parts out of 500,000 
# corresponds to 4 parts per million, so you should have:
# >>> ppm(2, 500000)
# >>> 4.0
# It suffices to include the function definition ("def ppm ...") in hw1.py. 
# The function will be tested by calling it on some representative inputs and 
# making sure that it returns the right output. Obviously, you should also do 
# your own testing make sure it is working right.
def ppm(count, total):
  return float(count) / float(total) * 1000000

# 7. Express gen_ct as parts per million out of the total number of tokens in 
# Genesis, and get gen_ppm to the result. Similarly express moby_ct as parts per
# million out of the total number of tokens in Moby Dick, and set moby_ppm to
# the result
gen_ppm = ppm(gen_ct, len(text3))
moby_ppm = ppm(moby_ct, len(text1))

# Print Solutions:
print('Q1:', A1)
print('Q2:', A2)
print('Q3:', A3)
print('gen_ct:', gen_ct)
print('moby_ct:', moby_ct)
print('Q5:', A5)
print('gen_ppm', gen_ppm)
print('moby_ppm', moby_ppm)
