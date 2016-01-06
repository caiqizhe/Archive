#!/usr/bin/python
# Homework 7
# Zijie Ku

from hmm import *

class Tagger(object):
	# __init__ takes an HMM model as input
	# save it in the member model. 
	def __init__ (self, hmm):
		self.model = hmm
		self.nodes = []
		return

	def reset (self, wordlist):
		# take a list of words and store them in the member words
		# sets the member nodes to the empty list
		self.words = wordlist
		self.nodes = []
		return

	def new_node (self, i, word, pos, prev_nodes):
		# takes four argument: i, word, pos, and prev_nodes
		# create a new Node instance and append it to the tagger's list of nodes
		index = len( self.nodes ) # get the current index
		node = Node(index, i, word, pos, prev_nodes) 
		self.nodes.append( node ) 
		return node

	def build_graph(self):
		# it takes a sentence( a list of word tokens) as input
		self.nodes = [] # reset nodes
		# first, it creates the left boundary node, which should always have index 0
		left_bound = self.new_node(-1, '', '', [])
		prevs = [left_bound]

		for i in range(len(self.words)):
			# for each word, it uses the model to get the list of possible parts of speech.
			parts = self.model.parts( self.words[i] )
			temp_prevs = []
			# for each part of speech, it creates a separate node
			for p in parts:
				self.new_node( i, self.words[i], p, prevs )
				temp_prevs.append( self.nodes[-1]  )
			prevs = temp_prevs
		# after creating nodes for all words in the sentence,
		# it creates the right boundary node, which should always be the last node in tagger.nodes.
		right_bound = self.new_node( len(self.words), '', '', [self.nodes[-1]] )
		return

	def edge_score(self, prev, next):
		# next.i == prev.i + 1
		# assume that prev.score is known, next.score is unknown
		model = self.model
		if prev.pos == '':
			score = prev.score + model.tcost( None, next.pos)
		else:
			score = prev.score + model.ecost( prev.pos, prev.word ) + \
					model.tcost(prev.pos, next.pos)
		if next.pos == '':
			score = prev.score + model.tcost(prev.pos, None)
		return score

	def score_node(self, node):
		# assume that the score has already been computed for all nodes in node.prev_nodes.
		# set node.score to the score of the best path leading to node and 
		# set node.best_prev to the predecessor that the best path passes through
		best_score = float('inf')
		best_prev = None
		for n in node.prev_nodes:
			curr_score = self.edge_score(n, node)
			if  curr_score < best_score:
				best_score = curr_score
				best_prev = n
		node.best_prev = best_prev
		node.score = best_score
		return
		
	def score_graph(self):
		for node in self.nodes:
			if node.i == -1:
				node.score = 0.0
			else:
				self.score_node(node)
		return

	def unwind(self):
		# takes no input
		# returns the list of tags in the path through the graph
		# start at the right boundary node and follow best_rev links 
		# backward through the graph.
		# return the resulting list of tags
		result = []
		curr_node = self.nodes[-1]
		while curr_node.best_prev.i != -1:
				result.append( curr_node.best_prev.pos )
				curr_node = curr_node.best_prev
		return list(reversed(result))

	def __call__(self, sentence):
		self.reset( sentence )
		self.build_graph()
		self.score_graph()
		tag_list = self.unwind()
		return list( zip(sentence, tag_list) )

