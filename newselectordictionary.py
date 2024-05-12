#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# Copyright (C) 2024 Xavier Schoepfer
# GNU GENERAL PUBLIC LICENSE Version 3



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
	myDomainList = readList('assets/domains.txt')
	# For each domain, choose a list of words from which
	# the names of the selectors are randomly drawn.
	for dn in myDomainList:
		print(dn)	# INTRUMENTATION
		match dn:
			case 'example.com':
				myRefList = 'assets/us-state-capitals.txt'
			case 'example.net':
				myRefList = 'assets/fr-regional-capitals.txt'
			case _:
				myRefList = 'assets/eu-capitals.txt'
	print(myRefList)		# INTRUMENTATION
	# Create a list of selector names
	mySelectorList = newSelectors(readList(myRefList))
	print(mySelectorList)	# INSTRUMENTATION



def main():
	newSelectorDictionnary()



if __name__ == '__main__':
	main()
