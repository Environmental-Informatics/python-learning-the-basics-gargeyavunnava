"""
Created on Wed Jan 22 13:48:13 2020
@author: vvunnava
Assignment_01, Exrecise_3.3, script for parts 1 & 2
"""

#Excersie 3.3, Part 1


def do_twice(f):  #runs function twice
    f()
    f()
    
def do_four(f): #runs the function do_twice twice
    do_twice(f)
    do_twice(f)


def print_2x2_grid():  #function to print 2x2 grid   
    
    def print_vertical_lines():  #function prints '|' symbols
        print('|         '*2,end='') #'*2' used to repeat pattern twice
        print('|')
    
    def print_plus_minus(): #function prints '+' & '-' symbols
        print('+ - - - - '*2,end='')
        print('+')
        
    def print_grid_symbols():  #function arranges symbols & prints in grid form
        print_plus_minus()
        do_four(print_vertical_lines)
        
    do_twice(print_grid_symbols) #function calls the print grid function twice
    print_plus_minus()           # add the bottom most line pattern

print('_______________'*3) #'__' used to demarcate Part 1 and Part 2
print('Excersie 3.3, Part 1: 2x2 grid')   
print_2x2_grid()
print('_______________'*3)

#Excersie 3.3, Part 2

def print_4x4_grid():  #function to print 4x4 grid 
    
    def print_vertical_lines():
        print('|         '*4,end='') #'*4' used to repeat pattern 4 times
        print('|')
    
    def print_plus_minus():
        print('+ - - - - '*4,end='')
        print('+')
        
    def grid_symbols():
        print_plus_minus()
        do_four(print_vertical_lines)
        
    do_four(grid_symbols)
    print_plus_minus()
    
print('Excersie 3.3, Part 2: 4x4 grid') 
print_4x4_grid()
print('_______________'*3)
