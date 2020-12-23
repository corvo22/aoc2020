# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 20:50:53 2020

@author: Ky
"""

def main():
    low = 10000000000000000000
    file = open("day13.txt", "r")
    lineList = file.read().replace("\n", "").split(",")
    
    timestamp = int(lineList[0])
    print(timestamp)
    busList = lineList[1:]
    seriesList = lineList[1:]
    busList = [i for i in busList if i != "x"]
    busList = [int(i) for i in busList] 
    
    unaltered = busList
    
    busList = [(int(timestamp / i) + 1) for i in busList]
    
    for i in range(len(busList)):
        busList[i] = busList[i] * unaltered[i] - timestamp
        if busList[i] < low:
            low = busList[i]
    print(busList)
    print(unaltered)
    
    print(unaltered[busList.index(low)] * low)

if __name__ == "__main__":
    main()
