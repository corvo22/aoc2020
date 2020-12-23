# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:43:24 2020

@author: Ky
"""
def main():
    
    file = open("santaExpenseReport.txt", "r")
    expense = file.read()
    expenseList = expense.split("\n")
    file.close()
    
    expenseList = [int(i) for i in expenseList]
    list2020 = list(2020 - x for x in expenseList)
    
    
    for i in range(len(expenseList)):
        x = list2020[i]
        for j in range(len(expenseList)):
            if x == expenseList[j]:
                print((2020-x)*expenseList[j])
    
if __name__ == "__main__":
    main()
