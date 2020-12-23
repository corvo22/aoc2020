# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:18:49 2020

@author: Ky
"""
string = ""
character = ""
count = 0

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
            minimum = int(stringList[0])
            maximum = int(stringList[1])
        if i % 2 == 1:
            string = splitPasswordList[i]
            
            for x in string:
                
                if x == character:
                    count = count+1
                    
            #print(minimum)
             
            if(count >= minimum and count <= maximum):
                sumval = sumval + 1
                print(sumval)
            
if __name__ == "__main__":
    main()