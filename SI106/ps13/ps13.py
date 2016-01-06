import test106 as test

### PROBLEM 1.
# We have provided test cases for the first function, as an example. 
# Write at least two test cases each for the next three functions

def letter_freqs(word_list):
    letter_freq_dict = {}
    for w in word_list:
        for l in w:
            if l not in letter_freq_dict:
                letter_freq_dict[l] = 1
            else:
                letter_freq_dict[l] = letter_freq_dict[l] + 1
    return letter_freq_dict

test.testEqual(type(letter_freqs(["hello", "goodbye"])), type({}))
test.testEqual(letter_freqs(["good", "bad", "indifferent"]), {'a': 1, 'b': 1, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 2, 'o': 2, 'n': 2, 'r': 1, 't': 1})
test.testEqual(letter_freqs(["good"]), {'g':1, 'o':2, 'd':1})
test.testEqual(letter_freqs([]), {})
    

 

def key_with_biggest_value(diction):    
    most_freq_letter = diction.keys()[0]
    for item in diction.keys():
        if diction[item] > diction[most_freq_letter]:
            most_freq_letter = item
    return most_freq_letter

print( 'Tests for key_with_biggest_value' )
print( '------------------------------' )   
mydict = {'a':1,'b':2}
test.testEqual(key_with_biggest_value(mydict), 'b', 'test correctness of function')
test.testEqual(type( key_with_biggest_value(mydict) ), type(''), 'test correctness of return type')
mydict = {'a':1,'b':1}
test.testEqual( key_with_biggest_value(mydict), 'a', 'test special case if two values are the same, first one should be returned' )
print 
print



def most_frequest_letter(word_list):
    return key_with_biggest_value(letter_freqs(word_list))

print( 'Tests for most_frequest_letter' )
print( '------------------------------' )    
mystring = [ "hello" ]
test.testEqual( most_frequest_letter(mystring), 'l', 'test correctness of function')
test.testEqual(type( most_frequest_letter(mystring) ), type(''), 'test correctness of return type')
mystring = [ "abc" ]
test.testEqual( most_frequest_letter(mystring), 'a', 'test special case if two values are the same, first one should be returned'  )
print
print

def popular_keys(diction):
    pop_keys = []
    for k in diction:
        if diction[k] > 3:
            pop_keys.append(k)
    return pop_keys

print( 'Tests for popular_keys' )
print( '------------------------------' )
mydict = {'a':10,'b':10}
test.testEqual( type( popular_keys(mydict) ), type([]), 'test correctness of return type' )
test.testEqual( popular_keys({}), [], 'test corner case with empty input')
test.testEqual( popular_keys(mydict), ['a','b'], 'test special case if two values are the same, first one should be returned' )

### PROBLEM 2. 
#Define test cases for the Car class below that will make you confident that all three of the methods 
# are operating correctly. 
#For each of your tests, include a comment stating whether it's a return-value test or a side-effect test. 

# (Note: we never showed any examples in class of explicitly calling the __str__ method, but you can. 
    # If x is an instance of the class Car, x.__str__() can be invoked just as x.move_forward() can. 
    # Indeed, __init__ can also be invoked this way, too, but in practice you would not want do it; 
    # __init__ gets called automatically when a new instance is created, and that's normally the only 
    # time it gets called.)
    
class Car:
    def __init__(self,color,wheels=4,size="compact",make=None):
        self.color = color
        self.wheels = wheels
        self.size = size
        self.make = make
        self.wheels_with_uhaul = wheels + 4
        self.dist_from_origin = 0.0

    def __str__(self):
        s = "A %s car:\n" % (self.color)
        if self.make:
            s = s + "Make: %s\n" % (str(self.make))
        s = s + "Has %d wheels\n" % (self.wheels)
        s = s + "Current distance from origin: %.02f miles" % (self.dist_from_origin)
        return s

    def move_forward(self,miles=1):
        self.dist_from_origin = self.dist_from_origin + miles
        return "Moved forward %.02f miles" % (miles)

print( 'Test for Car class')
print( '------------------------------' )
mycar = Car(color = 'black', size = 'SUV')
test.testEqual( type(mycar), type(Car(color = 'black')), 'test for type' )
print
print

test.testEqual(mycar.color, 'black', 'test if object is correctly initialized' )
print
print

print( '------------------------------' )
mycar.move_forward()
test.testEqual( mycar.dist_from_origin , 1.0, 'test if object is able to move forward with no parameters')
mycar.move_forward(3)
test.testEqual( mycar.dist_from_origin , 4.0, 'test if object is able to move forward with parameters' )
print
print

print( 'Test __str__ of the object')
print( '------------------------------' )
print( mycar )









