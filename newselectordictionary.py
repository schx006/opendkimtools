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



def newSelectorDictionnary():
    domain = readList('/root/domainList.txt')
    for dn in domain:
        print(dn)           # INTRUMENTATION
        match dn:
            case 'decadent.art':
                nameList = '/root/us-state-capitals.txt'
            case 'schoepfer.nom.fr':
                nameList = '/root/fr-regional-capitals.txt'
            case _:
                nameList = '/root/eu-capitals.txt'
        print(nameList)     # INTRUMENTATION
        #print(getPublicKey())
        selector = newSelectors(readList(nameList))
        print(newSelector)  # INSTRUMENTATION


def main():
    newSelectorDictionnary()



if __name__ == '__main__':
	main()
    
