# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:31:03 2019

@author: Asus
"""

npm = input("NPM: ")

val = int(npm[4])
val2 = int(npm[5])
val3 = int(npm[6])

subs = val + val2 + val3

print("Input: "+npm)
print("Output: ")

while subs > 0:
    print("Hallo, "+npm[4:7]+" Apa Kabar?")
    subs = subs - 1