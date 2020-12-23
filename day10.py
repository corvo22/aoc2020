# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:49:42 2020

@author: Ky
"""

def main():
    
     file = open("day10_input.txt", "r")
     lineList = file.read().split("\n")
     adapterList = sorted(int(i) for i in lineList)
     print(adapterList)
     
     threeDif = 1
     oneDif = 1
     
     for i in range(len(adapterList)):
         if i+1 < len(adapterList):
             if adapterList[i+1] == adapterList[i] + 1 :
                 oneDif = oneDif + 1
             elif adapterList[i+1] == adapterList[i] + 3 and adapterList[i+1] != adapterList[i] + 2:
                 threeDif = threeDif + 1
     print(threeDif * oneDif)
     
     
if __name__ == "__main__":
    main()