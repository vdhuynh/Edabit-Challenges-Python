def years_in_one_house(age, moves):
	return age if moves == 0 else round(age/(moves + 1))
