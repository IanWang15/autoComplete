import sys
import nltk
import re
import codecs
#nltk.download('punkt')

reload(sys)  
sys.setdefaultencoding('utf8')

print sys.getdefaultencoding()

class mapper:
	def splitSentence(self):
	# read sentence by sentence instead of line by line
		f = open("./log", "w")
        	lastLine = ''
	        for line in sys.stdin:
		# loop around standard input gives a line at a time
        	        data = nltk.sent_tokenize(lastLine+' '+line)
			# combine last term in previous line and current line
			if len(data) < 1:
				continue
			lastLine = data[-1]

                        for sentence in data[:-1]:
			# [:-1] used to remove period.
#	                        if len(sentence[:].split()) < 2:
#				# 1-gram moves to log
#        	                        f.write(sentence)
#					continue
				self.nGram(3,sentence)
		f.close()

	def nGram(self, gramNum, sentence):
		words = sentence[:-1].strip().split()
		for loc in range(len(words) - gramNum + 1):
			word = ''
			for i in range(gramNum):
				word = word+'@'+words[loc + i]
			print "%s\t%s" % (word[1:],1)


t = mapper()
t.splitSentence()

