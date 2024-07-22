Color, (red, green, blue) = EnumSort('Color', 
	('red', 'green', 'blue'))


print (simplify(green == blue)) # False

c = Const('c', Color)
solve(c != green, c != blue) # [c = red]