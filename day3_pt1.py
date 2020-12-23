# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:37:18 2020

@author: Ky
"""

def main():
    total = 0
    file = open("day4_pt1_input.txt", "r")
    temp = file.read()
    passportList = temp.split("\n\n")
    
    #splitList = list(x.split(":") for x in passportList)
    print(passportList)
    for lis in passportList:
    
        
        if (("byr" in lis) and ("iyr" in lis) and ("eyr" in lis) and ("hgt" in lis) and ("hgt" in lis)
            and ("hcl" in lis) and ("ecl" in lis) and ("pid" in lis)):
            total = total + 1
    print(total)
if __name__ == "__main__":
    main()

