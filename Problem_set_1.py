# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:23:52 2023

@author: FANKA
"""

"""
Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if 
s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

s = 'azcbobobegghakl'

numb = 0

vowels = "aeiou"

for vowel in s:
    if vowel in vowels:
        numb += 1
print("Number of vowels: " + str(numb))
#%%
"""
Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
s = 'azcbobobegghakl'

bob = "bob"
numbobs = 0
for bobs in range(len(s)):
    if s[bobs: bobs+3] == bob:
        numbobs += 1
print(numbobs)
#%%
"""
Problem 3
15.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your
 program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If 
you've spent more than a few hours on this problem, we suggest that you move 
on to a different part of the course. If you have time, come back to this 
problem after you've had a break and cleared your head.
"""

s = 'azcbobobegghakl'

r = ''
c = ''
for char in s:
    if (c == ''):
        c = char
    elif (c[-1] <= char):
        c += char
    elif (c[-1] > char):
        if (len(r) < len(c)):
            r = c
            c = char
        else:
            c = char
if (len(c) > len(r)):
    r = c
print('Longest substring in alphabetical order is: ' + str(r))
#%%

    


















