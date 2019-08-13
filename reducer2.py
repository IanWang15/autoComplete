#!/usr/bin/python
import sys
 
class reducer():
	def collect(self):
		oldWord = None
		countTotal = 0
		for line in sys.stdin:
			line = line.strip().split("\t")
			if len(line) != 2:
				continue
			thisWord, count = line
			if oldWord and oldWord != thisWord:
				print "%s\t%s" % (oldWord, countTotal)
				countTotal = 0
			oldWord = thisWord
			countTotal += int(count)
		if oldWord != None:
			print "%s\t%s" % (oldWord, countTotal) 


t = reducer()
t.collect()


#!/usr/bin/python
import sys

class reducer2():
	def collect(self):
		oldWord  = None
		oldValue = None
		countTotal = 0
		for line in sys.stdin:
			line = line.strip().split("\t")
			if len(line) != 2:
				continue
			thisWord, count = line
			second = count.strip().split("=")
			if len(second) != 2:
				continue
			thisValue, prob = second
			if oldWord and (oldWord != thisWord) or (thisValue != oldValue):
				print "%s\t%s\t%s" % (oldWord, oldValue, countTotal)
				countTotal = 0
			oldWord = thisWord
			oldValue = thisValue
			countTotal += int(prob)
		if oldWord != None:
			print "%s\t%s\t%s" % (oldWord, oldValue, countTotal)
			# print last line if not Null

t = reducer2()
t.collect()


