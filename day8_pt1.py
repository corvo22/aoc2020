# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:10:09 2020

@author: Ky
"""

def main():
    acc = 0
    alreadyBeenList = []
    file = open("day8_test.txt", "r")
   
    lineList = file.read().split("\n")
    print(lineList)
    index = 0
    for item in lineList:
        if index not in alreadyBeenList or index == 0:
            alreadyBeenList.append(index)
            if item[0:3] == "acc":
                if item[4] == "+":
                    acc = acc + int(item[5:])        
                    print(acc)
                elif item[4] == "-":
                    acc = acc - int(item[5:])
                    print(acc)
            if item[0:3] == "jmp":
                
          
    print(acc)
if __name__ == "__main__":
    main()
