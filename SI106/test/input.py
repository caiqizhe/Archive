# prompt user for input, exit when inputis ''
lst = []
sentence = raw_input('-->')
while sentence != '':
	lst.append(sentence)
	sentence = raw_input('-->')
	print sentence
