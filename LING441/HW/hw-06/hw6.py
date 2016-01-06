#!/usr/bin/python
# Homework 6
# Zijie Ku

import nltk
from nltk import FreqDist
from nltk import ConditionalFreqDist
from math import log10

# Smoothed Language Model
class SmoothedLangModel:
	def __init__( self, text, epsilon ):
		self.text = text
		self.epsilon = epsilon
		self.N = len( text )
		self.n = len( set( text ) )
		self.n_ep = self.n * epsilon
		self.N_nnep = self.N + self.n_ep * self.n
		self.bigram = self.bigrams( self.text )
		self.fd = FreqDist( self.text )
		self.cfd = ConditionalFreqDist( self.bigram )

	def bigrams( self, l ):
		yield (l[-1], l[0])
		for i in range( ( len(l) - 1 ) ):
			yield ( l[ i ],l[ i + 1] )

	def uprob( self, x ):
		if( self.exists( x ) ):
			return ( self.fd[ x ] + self.n_ep ) / ( self.N_nnep )

	def biprob( self, x, y ):
		if( self.exists( x ) and self.exists( y ) ):
			return ( float( self.cfd[ x ][ y ] )  + self.epsilon ) / ( self.fd[ x ] + self.n_ep )

	def exists( self, x ):
		if( x in self.text ):
			return True
		else:
			raise Exception( 'Illegal word: {}'.format( x ) )

	def ucost( self, x ):
		return ( -log10( self.uprob( x ) ) )

	def bicost( self, x, y ):
		return ( -log10( self.biprob( x, y ) ) )

	def cost( self, text ):
		pairs = list( self.bigrams( text ) )
		total = sum( list( self.bicost( b[ 0 ], b[ 1 ] ) for b in pairs[ 1 : ] ) ) + self.ucost( text[ 0 ] );
		return total / len( text )


# Unigram Language Model
class UnigramLangModel:
	def __init__( self, text ):
		self.fd = FreqDist( text )

	def ucost( self, x ):
		return ( -log10( self.fd.freq( x ) ) )

	def cost( self, text ):
		return sum( list( self.ucost(t) for t in text ) ) / len( text )

# 4. Define a function named split_text that takes two arguments: a text and a proportion 
# p between 0.0 and 1.0. The proportion p indicates how much of the text to use as 
# training; the remainder is used for testing. The return value is a pair (train, test), 
# in which train and test are token lists. For example:
# >>> split_text(list('abcdefgh'), .75)
# (['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h'])
def split_text( text, p ):
	separate = int( len(text) * p )
	return ( list( text[ : separate ] ), list( text[ separate : ] ) )


from nltk.corpus import gutenberg
# print( gutenberg.fileids() )

mobydick = gutenberg.words( 'melville-moby_dick.txt' )
( mtrain, mtest ) = split_text( mobydick, 0.9 )

# 5.
class FreqFilter:
	def __init__( self, text, n ):
		self.text = list( t.lower() for t in text )
		self.fd = FreqDist( self.text )
		self.n = n
		self.vocabulary = set( t for t in self.fd if self.fd[ t ] >= self.n )

	def apply( self, text ):
		text = list( t.lower() for t in text )
		return list( t if t in self.vocabulary else 'UNK' for t in text )

# 6.
mfilt = FreqFilter( mtrain, 2)
fmtrain = mfilt.apply( mtrain )
fmtest = mfilt.apply( mtest )

slm = SmoothedLangModel( fmtrain, 0.5 )
slm_cost = slm.cost( fmtest )

ulm = UnigramLangModel( fmtrain )
ulm_cost = ulm.cost( fmtest )

slm01 = SmoothedLangModel( fmtrain, 0.01 )
slm01_cost = slm01.cost( fmtest )

# 7.
emma = gutenberg.words( 'austen-emma.txt' )
persuation = gutenberg.words( 'austen-persuasion.txt' )
sense_sensibility = gutenberg.words( 'austen-sense.txt' )
brown = gutenberg.words( 'chesterton-brown.txt' )
thursday = gutenberg.words( 'chesterton-thursday.txt' )

mfilt_new = FreqFilter( emma, 2 )
mftrain_new = mfilt_new.apply( emma )

slm_emma = SmoothedLangModel( mftrain_new, 0.01 )

slm_cost_persuation = slm_emma.cost( mfilt_new.apply( persuation ) )
slm_cost_sense_sensibility = slm_emma.cost( mfilt_new.apply( sense_sensibility ) )
slm_cost_brown = slm_emma.cost( mfilt_new.apply( brown ) )
slm_cost_thursday = slm_emma.cost( mfilt_new.apply( thursday ) )
scores = [ slm_cost_persuation, slm_cost_sense_sensibility, slm_cost_brown, slm_cost_thursday ]

