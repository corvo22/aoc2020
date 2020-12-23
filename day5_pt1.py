# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:02:44 2020

@author: Ky
"""
import math 
def main():
    
    upper = 127
    lower = 0
    colUp = 7
    colLow = 0
    seatRow = 0
    high = 0
    file = open("day5_input.txt", "r")
    lineList = file.read().split("\n")
    
    print(lineList)

    for item in lineList:
        rowList = list(range(0,128))
        colList = list(range(0,7))
        
        for char in item:
            if char == "F":
               upper = math.floor(upper - (upper-lower)/2)
            elif char == "B":
                lower = math.ceil(lower + (upper - lower)/2)
            elif char =='L':
                colUp = math.floor(colUp - (colUp-colLow)/2)
            elif char == 'R':
                colLow = math.ceil((colLow + (colUp-colLow)/2))
                
        seatId = 8 * upper + colUp
        if seatId > high:
            high = seatId
        #print(str(colLow) + "," + str(colUp) + "   " + str(lower) + "," + str(upper) + "   " + str(seatId))
        colUp = 7
        colLow = 0
        upper = 127
        lower = 0
    print(high)
if __name__ == "__main__":
    main()
