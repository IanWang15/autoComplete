import sys
import nltk
import re
#nltk.download('punkt')

class mapper2:
	def lgModel(self):
	        for line in sys.stdin:
			words, count = line.strip().split()
			wordList = words.strip().split("@")
			key = ''
			for num in range(len(wordList) - 1):
				key = key + '@' + wordList[num]
			count = wordList[-1] + '=' + count
			print "%s\t%s" % (key[1:],count)
			





#			word = ''
#			word = [word+''+words[i] for i in range(gramNum)]
#		for word in words[:-gramNum]:
#			print "%s\t%s" % (word[1:],1)
			#print '??', re.sub('[^A-Za-z0-9]+', '', word)

t = mapper2()
t.lgModel()

