#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8



import re, random


# Read a list of words in a file.
def readList(myNameList):
	with open(myNameList, encoding="utf-8") as f:
	myList = f.readlines()
	for i in range(len(myList)):
		myList[i] = re.sub(r'\n', '', myList[i])
		return(myList)


# Randomly return 3 items from a list.
def newSelectors(myList):
	return(random.sample(myList, 3))


# Create a dictionary structure for domain names and
# a list of their selectors.
def newSelectorDictionnary():
	# Read the list of domain names.
	domain = readList('assets/domainList.txt')
	# For each domain, choose a list of words from which
	# the names of the selectors are randomly drawn.
	for dn in domain:
		print(dn)	# INTRUMENTATION
		match dn:
			case 'decadent.art':
				nameList = 'assets/us-state-capitals.txt'
			case 'schoepfer.nom.fr':
				nameList = 'assets/fr-regional-capitals.txt'
			case _:
				nameList = 'assets/eu-capitals.txt'
	print(nameList)		# INTRUMENTATION
	# Create a list of selector names
	selector = newSelectors(readList(nameList))
	print(newSelector)	# INSTRUMENTATION



def main():
	newSelectorDictionnary()



if __name__ == '__main__':
	main()
