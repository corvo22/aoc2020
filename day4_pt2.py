# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:41:12 2020

@author: Ky
"""


def main():
    byr = 0
    iyr = 0
    eyr = 0
    hgt = ""
    hcl = ""
    ecl = ""
    pid = ""
    tf = True
    total = 0
    file = open("day4_pt1_input.txt", "r")
    temp = file.read()
    div = 0
    passportList = temp.split("\n")
    test = "hello world"
    test.replace(" ",":")
    
    for lis in passportList:
        s = lis.replace(" ", ":",)
        split = s.split(":")
        print(split)
        
        if (("byr" in split) and ("iyr" in split) and ("eyr" in split) and ("hgt" in split) and
            ("hcl" in split) and ("ecl" in split) and ("pid" in split)):
            
            for x in range(len(split)):
                if split[x] == "byr":
                    byr = int(split[x+1])
                    div = div + 1
                if split[x] == "iyr":
                    iyr = int(split[x+1])
                    div = div + 1
                if split[x] == "eyr":
                    eyr = int(split[x+1]) 
                    div = div + 1
                if split[x] == "hgt":
                    hgt = split[x+1]
                    div = div + 1
                if split[x] == "hcl":
                    hcl = split[x+1]
                    div = div + 1
                if split[x] == "ecl":
                    ecl = split[x+1]
                    div = div + 1
                if split[x] == "pid":
                    pid = (split[x+1])
                    div = div + 1
                if ((byr >= 1920 and byr <= 2002) and (iyr >= 2010 and iyr <= 2020) and (eyr >= 2020 and eyr <= 2030)):
                    if(hgt != "" and ((hgt[-1] == "n" and hgt[-2] == "i" and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76) or 
                                      (hgt[-1] == "m" and hgt[-2] == "c" and int(hgt[:-2]) >=150 and int(hgt[:-2]) <= 193))):
                         if(ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth"):
                            if(len(pid) == 9):
                                for z in hcl:
                                    if not(not(z in "0123456789abcdef")):
                                        div = 1
                                    else:
                                        div = 0
                                if div == 1:
                                    total = total + 1   
                                    
    
    print(total)
if __name__ == "__main__":
    main()