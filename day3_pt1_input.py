# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:28:46 2020

@author: Ky
"""
def main():
    treeCount = 0
    pos = 0
    file = open("day3_pt1_test.txt", "r")
    lineList = file.readlines()
   
    for x in lineList:
        if pos >= len(x):
            pos = pos - (len(x)+1)
        
        
        if x[pos] == '#':
            treeCount = treeCount + 1
            print(str(treeCount) + " hit " + str(pos) + "  " + str(x)) 
            
        
        else:
            
            print("miss" + "  " + str(pos) + "  " + str(x))
        
        pos = pos + 7
    print(treeCount)
    #print(len(lineList[1]))
if __name__ == "__main__":
    main()
