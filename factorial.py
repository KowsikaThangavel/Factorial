#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      student
#
# Created:     21/07/2016
# Copyright:   (c) student 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 num = int(input("Enter a number: "))
 fact = 1
 if(num>0):
    for i in range(1,num + 1):
       fact = fact*i
    print"The factorial of",num,"is",fact



if __name__ == '__main__':
    main()
