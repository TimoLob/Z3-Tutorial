# A is an array mapping from integer to integer
A = Array("A", IntSort(), IntSort())
x = Int('x')

Store(A, x, 10)
Select(A, x) # = A[x]

