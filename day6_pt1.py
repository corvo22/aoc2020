# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:16:31 2020

@author: Ky
"""

def main():
    file = open("day6_input.txt", "r")
    lineList = file.read().split("\n\n")
    num = 0
    total = 0
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(len(lineList)):
        lineList[i] = lineList[i].replace('\n','')
        for char in alpha:
            if char in lineList[i]:
                num = num + 1
            total = total + num
            num = 0
    print(lineList)
    print(total)
if __name__ == "__main__":
    main()