# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:18:40 2020

@author: Ky
"""

def main():
    
    file = open("day2_pt1_input.txt", "r")
    passwords = file.read()
    passwordList = passwords.split("\n")
    file.close()
    
    PasswordList = list(x.split(":") for x in passwordList)
    
    #print(splitPasswordList)
    
    splitPasswordList = [x for l in PasswordList for x in l]
    sumval = 0
    for i in range(len(splitPasswordList)):
        if i % 2 == 0:
            count = 0
            string = splitPasswordList[i]
            character = string[len(string)-1]
            stringList = string.split("-")
            stringList[1] = stringList[1][:-2]
            pos1 = int(stringList[0])
            pos2 = int(stringList[1])
        if i % 2 == 1:
            string = splitPasswordList[i]
            
            
                
            if ((string[pos1] == character and string[pos2] != character) or (string[pos1] != character and string[pos2] == character)):
                sumval = sumval + 1
                print(sumval)    
            
         
if __name__ == "__main__":
    main()
