#!/usr/bin/env python
#
# Project Euler Problem 8
# https://projecteuler.net/problem=8

digit = '731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907131051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

maxproduct = 1

def product(n):
	p = 1
	for d in list(n):
		p = p * int(d)
	return p


digit_length = len(digit)
pos = 0
d = digit[pos:13]
maxproduct = product(d)

while pos < (digit_length-13):
	pos = pos + 1
	d = digit[pos:pos+13]
	p = product(d)
	if p > maxproduct:
		maxproduct = p


print 'greatest product equals {} '.format(maxproduct) 

# $ time python problem8.py
# greatest product equals 23514624000

# real    0m0.129s
# user    0m0.031s
# sys     0m0.031s

