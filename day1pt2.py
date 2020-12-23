# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:43:16 2020

@author: Ky
"""
def main():
    
    file = open("santaExpenseReport.txt", "r")
    expense = file.read()
    expenseList = expense.split("\n")
    file.close()
    
    expenseList = [int(i) for i in expenseList]
    expenseList2 = [int(i) for i in expenseList]
    expenseList3 = [int(i) for i in expenseList]
    
    for i in range(len(expenseList)):
        x = expenseList[i]
        for i in range(len(expenseList)):
            y = expenseList[i]
            for i in range(len(expenseList)):
                z = expenseList[i]
                if((x + y + z) == 2020):
                    print(x*y*z)

if __name__ == "__main__":
    main()

