# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:20:43 2020

@author: Ky
"""



def main():
    treeCount = 0
    treeCount2 = 0
    treeCount3 = 0
    treeCount4 = 0
    treeCount5 = 0
    pos = 0
    even = 0
    file = open("day3_pt1_input.txt", "r")
    lineList = file.readlines()
    
    for x in lineList:
        if pos >= len(x)-1:
            pos = pos - (len(x)-1)
            
        if x[pos] == '#':
            treeCount = treeCount + 1
            print(str(treeCount) + " hit " + str(pos) + "  " + str(x)) 
        
        else:
            print("miss" + "  " + str(pos) + "  " + str(x))
        pos = pos + 3
    pos = 0
    for x in lineList:
        if pos >= len(x):
            pos = pos - len(x)
        if x[pos] == '#':
            treeCount2 = treeCount2 + 1
            print(str(treeCount2) + " hit " + str(pos) + "  " + str(x)) 
        
        else:
            print("miss" + "  " + str(pos) + "  " + str(x))
        pos = pos + 1
    pos = 0
    for x in lineList:
        if pos >= len(x)-1:
            pos = pos - (len(x)-1)
        
        
        if x[pos] == '#':
            treeCount3 = treeCount3 + 1
            print(str(treeCount3) + " hit " + str(pos) + "  " + str(x)) 
    
        
        else:
            
            print("miss" + "  " + str(pos) + "  " + str(x))
        
        pos = pos + 5
    pos = 0
    for x in lineList:
        if pos >= len(x):
            pos = pos - (len(x)+1)
        
        
        if x[pos] == '#':
            treeCount4 = treeCount4 + 1
            print(str(treeCount4) + " hit " + str(pos) + "  " + str(x)) 
    
        
        else:
            
            print("miss" + "  " + str(pos) + "  " + str(x))
        
        pos = pos + 7
    pos = 0
    for x in lineList:
        if pos >= len(x):
            pos = pos - len(x)
        if even % 2 == 1:
            if x[pos] == "#":
                 treeCount5 = treeCount5 + 1
                 print(str(treeCount5) + " hit " + str(pos) + "  " + str(x)) 
        even = even + 1
    print(treeCount * treeCount2 * treeCount3 * treeCount4 *treeCount5)
    print(str(treeCount) + " " + str(treeCount2)+ " " + str(treeCount3) + " " + str(treeCount4) + " " + str(treeCount5))
    
    # print(len(lineList[1]))
if __name__ == "__main__":
    main()

