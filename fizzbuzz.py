#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Select a number between 1 and 100"
number = raw_input("Add number: ")

number = int(number)

for num in range(1, number+1):
    if num % 3 == 0 and num % 5 == 0:
        print "fizzbuzz"
    elif num % 3 == 0:
        print "fizz"
    elif num % 5 == 0:
        print "buzz"
    else:
        print num

