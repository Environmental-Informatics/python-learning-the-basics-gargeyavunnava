'''
Created on Wed Jan 22 11:51:27 2020
@author: vvunnava
Assignment_01, Exrecise_3.2, script for part 4 of the question
Program description: Creating functions to run a function twice and print an argument twice
'''


def do_twice(f, arg):  #runs a function twice,f=function,arg=argument passed to f
    f(arg)
    f(arg)
    
def print_twice(arg): #prints a printable argument twice
    print(arg)
    print(arg)
    
do_twice(print_twice,'spam') #runs print_twice twice with string argument passed to print_twice

