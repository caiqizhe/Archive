#!/usr/bin/python
# Homework 8
# Zijie Ku

from nltk import CFG
from nltk import ChartParser
from nltk.tokenize import word_tokenize
import sys

class GDev:
	# 1. We will create a grammer development tool.
	# Define a class caledd GDev. The __init__ method should take a 
	# name (a string) as input, and store it in the member name.
	def __init__( self, name ):
		self.name = name
		return

	# 2. Define a method called load_grammar. It takes no arguments.
	# It expects the file name.cfg to exist, where name is the GDev name.
	# It loads a grammer from the file and stores it in the member grammer.
	def load_grammar( self ):
		s = open( self.name + '.cfg' ).read()
		self.grammar = CFG.fromstring(s)
		return

	# 3. Define a method called reload. It should call the method 
	# load_grammar, even if the grammar has already been loaded before.
	# Then it should create a chart parser from the loaded grammar, and
	# store the parser in the member parser. 
	def reload( self ):
		self.load_sents()
		self.load_grammar()
		self.parser = ChartParser( self.grammar )
		return

	# 4. Define a method called parse. It should take one argument, a string.
	# It should call word_tokenize on the sentence, and pass the result to 
	# the parser. The parse method should return a single tree. If the parser
	# returns more than one tree, then parse should return just the first one.
	# If the parser does not return any tress, then parse should return None.
	def parse( self, s ):
		try:
			return list( self.parser.parse( word_tokenize( s ) ) )[0]
		except:
			return None

	# 5. Define a method called load_sents. It takes no arguments. It expects
	# the file name.sents to exist. The file should contain one sentence per 
	# line. Each sentence is either good or bad—good sentences are ones that 
	# the grammar ought to generate, and bad sentences are ones that the 
	# grammar should not generate. If the first character on the line is ’*’, 
	# the sentence is bad, and otherwise it is good. The load_sents method 
	# should produce a list of pairs (good, s) where good is True for good 
	# sentences and False for bad ones, and s is the sentence itself (not 
	# including the ’*’). The list of pairs should be stored in the member 
	# sents. Create a file g1.sents containing the sentences Bob warbled, the 
	# dog ate my telescope, and *Bob cat.
	def load_sents( self ):
		self.sents = [ ( True, line.rstrip('\r\n') ) \
						if line[0] != '*' \
						else (False, line.rstrip('\r\n')[1:]) \
						for line in open(self.name + '.sents') ]
		# print( self.sents )


	# 6. Define a method called parses. It should take no arguments. 
	# It should iterate through the pairs (g,s) in sents, and it should 
	# call parse on each sentence s in turn. For each sentence, it should
	# print an empty line, then the sentence, then the result of calling parse.
	def parses( self ):
		for s in self.sents:
			print( '\n' + s[1] )
			print( self.parse( s[1] ) )

	# 7. Write a method called regress that takes no arguments. It should go 
	# through the pairs (good, s) in sents. For each, it should call parse on s.
	# Define the prediction to be True if parse returns a tree, and False otherwise.
	# If the prediction equals good, then the prediction is correct, and otherwise
	# the prediction is wrong. For each pair, print out one line of output. The output
	# line should start with '!!' if the prediction is wrong and '  ' (two spaces) 
	# it is correct. Then print out a space. Then print '*' if good is False, and a 
	# space if good is True. The output line ends with the sentence s.
	def regress( self ):
		prediction = False
		for s in self.sents:
			if self.parse( s[1] ) is not None: 
				prediction = True
			else:
				prediction = False
			if prediction != s[0]:
				print( '!!' + ' ' , end = '')
			else:
				print( '  ' + ' ' , end = '')
			if s[0] == False:
				print( '*' , end = '')
			else:
				print( ' ' , end = '')
			print( s[1] )

	# 8. Finally, the __call__ method should simply call reload and regress.
	# The idea is to use the set of example sentences to drive grammar development.
	# One adds sentences, calls gd() to see which ones are being handled correctly
	# or not, and then one edits the grammar to fix the prediction errors. After
	# each file edit, one needs merely call gd() to see the revised grammar's 
	# predictions on the sentences. (Making sure that new revisions do not break 
	# things that previously worked correctly is known as regression testing.)
	def __call__( self ):
		self.reload()
		self.regress()





