def mycount( inList ):
	freq = {}
	maxKey = ''
	maxValue = 0
	for strEle in inList:
		for charEle in strEle:
			if( charEle not in freq ):
				freq[charEle] = 1
			else:
				freq[charEle] += 1
			if(freq[charEle] > maxValue):
				maxKey = charEle
				maxValue = freq[charEle]
	return maxKey

inList = ['aaa', 'bbbbb', 'ccccccccccc','d']

print( mycount(inList) )


