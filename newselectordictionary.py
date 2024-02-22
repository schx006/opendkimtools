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


