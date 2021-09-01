#!/usr/bin/env python
#
# Project Euler Problem 2
# https://projecteuler.net/problem=2

s = 0

def sum(x,y):
	return x + y

x = 1
y = 2

while True:
	tmp = sum(x,y)
	x = y
	y = tmp
	if x > 4000000 or y > 4000000:
		break
	print tmp
	if tmp % 2 == 0:
		s = s + tmp

print 'sum of even numbers is {}'.format(s + 2) # sum of even numbers is 4613732
