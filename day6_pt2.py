# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:40:54 2020

@author: Ky
"""
def main():
    file = open("day6_test.txt", "r")
    lineList = file.read().split("\n\n")
    num = 0
    total = 0
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    containList = []
    for i in range(len(lineList)):
        lineList[i] = lineList[i].split("\n")
    
    print(lineList)

    for item in lineList:
        if len(item) == 1:
            total = total + 1
        for string in item:
            if string in alpha:
    print(total)
if __name__ == "__main__":
    main()
