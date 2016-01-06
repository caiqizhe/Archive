#!/usr/bin/python
# Accumulation Extra Credit
# Zijie Ku

sName = '        Zijie Ku'
print( '---------------------------')
print( sName )


''' You will earn 20 points each example that you're able to find and 
rewrite. You can earn a maximum of 40 points for each one of the five
( map, filter, reduce, zip, list comprehension), and a maximum of 100 
points overall.

Turn in your answer as .py file. For each snippet you are tranlating,
include a comment saying where you found it, the original code, and
then your replacement code.'''
print

print( '===========================' )
print( '      [[ Map - 1 ]]')
print( '---------------------------' )
''' Found under 'Lists and for loops' Chapter 09 03b '''
''' Original Code '''
'''
numbers = [10, 20, 30, 40, 50]
print numbers
for i in range(len(numbers)):
    numbers[i] = numbers[i]**2
print numbers
'''
''' improved code '''
numbers = [ 10, 20, 30, 40, 50 ]
print numbers
print map( lambda num: num ** 2, numbers )
print

print( '---------------------------' )
print( '      [[ Map - 2 ]]')
print( '---------------------------' )
''' Found under 'The Accumulator Pattern with Lists' exceptions-62 '''
''' Original Code '''
'''
list= [3,0,9,4,1,7]
new_list=[]
for i in range(len(list)):
   new_list.append(list[i]+5)
print new_list
'''
''' improved code '''
list=[3, 0, 9, 4, 1, 7]
print list
print map( lambda l: l + 5, list)
print

print( '===========================' )
print( '      [[ Filter - 1 ]]')
print( '---------------------------' )
''' Found under 'Understanding Code' Example '''
''' Original Code '''
'''
numbers = [1,2,6,4,5,6, 93]
z = 0
for num in numbers:
  print "*** LOOP ***"
  print "Num =",num
  if (num % 2) == 0:
    print "Is even. Adding",num,"to",z
    z = num + z
  print "Running sum =",z
print "*** DONE ***"
print "Total = " , z
'''
''' improved code '''
numbers = [1, 2, 6, 4, 5, 6, 93]
total = sum( filter( lambda num: num % 2 == 0, numbers ) )
print numbers
print 'Total = ', total
print

print( '===========================' )
print( '      [[ Filter - 2 ]]')
print( '---------------------------' )
''' Found under 'SI 106 - Winter 2015 Final' Question 15 '''
''' Define a function f that takes a list of strings and returns a list 
containing the first letter of every word that contains the letter z.
Now define the same funtion without using manual accumulation. Instead
it should use some combination of map, filter, reduce, zip and list 
comprehension '''
L = ['whiz', 'success', 'in the zone','yep', 'not another pizza!']
def f( L ):
	return [ l[0] for l in filter( lambda l : 'z' in l, L )]
print L
print f(L)
print 

print( '===========================' )
print( '[[ List Comprehension - 1 ]]')
print( '---------------------------' )
''' Found under 'SI 106 - Winter 2015 Final' Question 9 '''
''' Write code to sort L in order based on the last two character in 
each string, so that 253 in first and 356 is last. '''
L = ['154', '253', '356', '455']
print L
print sorted(L, key=lambda l: int(l[-2:]))
print

print( '---------------------------' )
print( '[[ List Comprehension - 2 ]]')
print( '---------------------------' )
''' Found under 'SI 106 - Winter 2015 Final' Question 9 '''
''' Define a function sorted_by_keys that takes a dictionary as input
as input and returns of a list of its values, sorted in alphabetic 
order based on the keys that have those values.'''
def sorted_by_keys( d ):
	return [d[k] for k in sorted( d.keys() ) ]
d = { 'alpha':10, 'bravo':30, 'delta':20, 'charlie': 10 }
print d
print sorted_by_keys( d )
print

print( '===========================' )
print( '[[ Reduce - 1 ]]')
print( '---------------------------' )
''' Found under 'SI 106 - Winter 2015 Final' Question 11 '''
''' Define a function sleepiest that takes an input a list of strings
and returns as output the string that has the most 'z's in it '''
L = ['zany', 'pizza', 'zzzzz', 'longest']
def sleepiest( L ):
	return reduce( lambda x, y: x if x.count('z') > y.count('z') else y, L )
print L
print sleepiest( L )
print


