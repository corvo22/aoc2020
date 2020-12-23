# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:18:57 2020

@author: Ky
"""
def main():
    
    ew = 0
    ns = 0
    direction = 0
    w_ew = 10
    w_ns = 1
    file = open("day12.txt", "r")
   
    lineList = file.read().split("\n")
    #print(lineList)
    for item in lineList:
        if item[0] == "E" or (item[0] == "F" and direction == 0):
            ew = ew + int(item[1:])
        elif item[0] == "N" or (item[0] == "F" and direction == 90):
            ns = ns + int(item[1:])
        elif item[0] == "W" or (item[0] == "F" and direction == 180):
            ew = ew - int(item[1:])
        elif item[0] == "S" or (item[0] == "F" and direction == 270):
            ns = ns - int(item[1:])
        elif item[0] == "L": 
            direction = direction + int(item[1:])
            if direction >= 360:
                direction = direction - 360
        elif item[0] == "R":
            direction = direction - int(item[1:])
            if direction < 0:
                direction = direction + 360
                
    print(abs(ew) + abs(ns))
    ew = 0
    ns = 0
    direction = 0 
    
    for item in lineList:
        if item[0] == "E":
            w_ew = w_ew + int(item[1:])
        elif item[0] == "N" :
            w_ns = w_ns + int(item[1:])
        elif item[0] == "W" :
            w_ew = w_ew - int(item[1:])
        elif item[0] == "S" :
            w_ns = w_ns - int(item[1:])
        elif item[0] == "L" or item[0] == "R": 
            if item[0] == "L":
                direction = 360 - int(item[1:])
                
            elif item[0] == "R":
                direction = int(item[1:])
               
            if direction == 90:
                temp = w_ew
                w_ew = w_ns
                w_ns = -1 * temp
     
            elif direction == 180:
                w_ew = -1 * w_ew
                w_ns = -1 * w_ns
            elif direction == 270:
                temp = w_ew
                w_ew = -1 * w_ns
                w_ns = temp
        elif item[0] == "F":
            mult = int(item[1:])
            ew = ew + w_ew * mult
            ns = ns + w_ns * mult
           
    print(abs(ew) + abs(ns))
if __name__ == "__main__":
    main()

