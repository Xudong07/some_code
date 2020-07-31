#-*-coding:utf-8 -*-
import os
import sys
'''
input
'''
try:
    while(1):
        a = input().split()
        if(not a) :
            break
        print(a)
finally:
    print('over')

try:
    while(1):
        a = sys.stdin.readline().strip().split()
        if(not a) :
            break
        print(a)
finally:
    print('over')


with open(sys.argv[1], 'r') as fin:
    while(1):
        a = fin.readline()
        if(not a):
            break
        a = a.split()
        print(a)

