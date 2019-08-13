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

