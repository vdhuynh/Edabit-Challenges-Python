def mod(m, n):
	#use floor division
	quotient = m//n
	#calculate the product of the quotient and divisor
	product = quotient * n
	#calculate the remainder between the original number and product
	remainder = m - product
	return remainder
