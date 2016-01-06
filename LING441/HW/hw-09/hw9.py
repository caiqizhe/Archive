#!/usr/bin/python
# Homework 9
# Zijie Ku

from nltk import Nonterminal as NT
from nltk import CFG
from chart import Chart, Node, Edge

class Parser():
	# 1.a. Define a class Parser. The constructor should take a filename
	# as argument, and do the following. Load a CFG from the file and 
	# store it in the member grammar. Create a chart and store it in 
	# the member chart
	def __init__( self, fname ):
		f = open( fname ).read()
		self.grammar = CFG.fromstring( f )
		self.chart = Chart()
		self.chart.trace = True
		return

	# 1.b. Also define the method reset. It takes a sentence (a list of tokens)
	# as input, and stores it in the member words. It also resets the chart, 
	# and sets the value of the memebr todo to the empty list.
	def reset( self, tokens ):
		self.chart = Chart()
		self.words = tokens
		self.todo = []
		return

	# 2. Implement create_node and create_edge. They take the same arguments
	# as the corresponding Chart methods. Each should simply call the 
	# corresponding Chart method, and append the resulting node or edge to 
	# the todo list. (However, do not append None to the todo list.)
	def create_node(self, start, category, end, expansion):
		node = self.chart.create_node(start, (category), end, expansion)
		if node:
			self.todo.append(node)
		return

	def create_edge(self, edge_or_rule, child):
		edge = self.chart.create_edge(edge_or_rule, child)
		if edge:
			self.todo.append(edge)
		return

	# 3. Implement the shift method. Contrary to the handout, its argument
	# should be the index of the word to shift, i, and it should create nodes
	# spanning positions i to i + 1. Create one node for each part of speech
	# that the grammar assigns to words[i]. You may assume that the members
	# grammar, chart, and words are all appropriately set. 

	def shift(self, i):
		foo = []
		for rule in self.grammar.productions():
			if(rule.rhs()[0] == self.words[i]):
				foo.append(rule.lhs())
		j = i + 1
		for bar in foo:
			self.create_node(i, bar, j, self.words[i])

		return

	# 4. Implement the bu_predict method. It takes a Node as input. Let
	# X be the node's category. For each rule r whose righthand side begins
	# with X, call create_edge on r and the node
	def bu_predict(self, node):
		rules = self.grammar.productions(rhs=node.cat)
		for rule in rules:
			self.create_edge(rule, node)
		return

	# 5. Implement the extend_edges method. It takes a Node as input. It 
	# iterates through the edge e taht end where the node begins, and if 
	# the node's category is the same as the category after the dot in e,
	# then a new edge is created that combines e and the node. (Use create_edge.)
	def extend_edges(self, node):
		for e in self.chart.get_edges_at(node.i):
			if e.after_dot() == node.cat:
				self.create_edge(e, node)
		return

	# 6. Implement the complete method. It takes an Edge as input. For
	# safety, it should signal an error if the dot is not at the end. Create
	# a node corresponding to the lefthand side of the rule, with the edge as
	# its expansion, covering the same span as the edge.
	def complete(self, edge):
		if not edge.dot_at_end():
			raise ValueError('Dot not at the end')
		else:
			self.create_node(edge.i, edge.rule.lhs(), edge.j, edge)

	# 7. The method next_task takes no input. It expects todo to be non-empty.
	# It removes the last item from todo and process it. If the item is a node, 
	# it calls bu_predict and extend_edges on it, and if the item is an edge,
	# and the dot is at the end, it calls complete on it.
	def next_task(self):
		while len(self.todo) > 0:
			item = self.todo.pop()
			if type(item) == Node:
				self.bu_predict(item)
				self.extend_edges(item)
			elif type(item) == Edge and item.dot_at_end():
				self.complete(item)
		return

	# 8. Implement the method fill_chart. It should call shift for each word,
	# and after each time it calls shift, it should call next_task repeatedly
	# until the todo list is empty
	def fill_chart(self):
		for num in range(len(self.words)):
			self.shift(num)
			while self.todo != []:
				self.next_task()

	# 9. Make the parser callable. When it is called as a function, it should take
	# a sentence ( that is, a list of tokens ) as input. It should call reset and
	# fill_chart. Then, if there is a node that spans the whole sentence and whose
	# category is the grammar's start symbol, it should return an iteration over the
	# tree of that node. Otherwise, it should return an empty iteration. Note: if
	# a method calls yield for some inputs but not others, the result will be an
	# empty iteration for the inputs where it never calls yield.
	def __call__(self, sentence):
		self.reset(sentence)
		self.fill_chart()
		new = self.chart.get_node(0, self.grammar.start(), 6).unwind()
		return new
