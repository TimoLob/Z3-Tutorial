s = Solver()
x = Real("x")

s.add(3*x + 6 == 0)

if s.check() == sat:
	m = s.model()
	x = m.evaluate(x)

	print(f"{x=}") # x=-2
else:
	print(s.check())