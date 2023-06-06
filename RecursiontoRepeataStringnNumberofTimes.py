def repetition(txt, n):
	#Base case: if n == 0, return an empty string
	if n == 0:
		return ''
	else:
		#Concatenate txt with the recursive case: function(txt, n-1)
		return txt + repetition(txt, n-1)
