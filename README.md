# Z3 Solver

## Introduction

### What is Z3?

- By microsoft

### SAT Solving

A propositional logical formula applies boolean operators like "and", "or",
"implies", and "not" on boolean variables. A formula can be evaluated by
assigning values (true/false) to those variables.
Using those assignments, we can evaluate the formula to determine if the whole
thing evaluates to true or false. A common question about a formula is to know
whether there exists an assignment of variables that makes the formula evaluate
to true.
If this is possible, then the formula is "satisfiable". Evaluating a given
solution to a formula is easy, just evaluate it with the given solution.
Finding the solution, however, is difficult. The SAT problem falls into the NP
complexity class. The most straightforward way to solve SAT problems is to try
out every possible combination the variables can take on. However, this method
becomes infeasible very quickly. SAT solver approach the problem in a smarter
way, they reduce and search the solution space efficiently by trying to deduce
and propagate information in combination with techniques such as
[backjumping](https://en.wikipedia.org/wiki/Conflict-driven_clause_learning).

### SMT solving

SMT solvers combine the boolean logic structures from a pure SAT solver, and
combine it with domain specific structure about integers, reals and other
datatypes. Domain specific facts, like the constraint $x+y \leq 42$ are
treated like a single boolean variable $p$. Then the techniques of the SAT
solver are applied and solutions that are #todo

### Which problems can be solved with Z3?

### What can Z3 not do?

- Prime factorization of large numbers
- sin/cos/tan

## Installation

´pip install z3-solver´

(not 'z3', that is a different package)

## Basic Usage

3 Steps:

1. Declare your variables
2. Add constraints to the problem
3. Solve

### Sorts

Basic : Bool, Int, Real, Bit-vector

Composite : Arrays, Tuples, Records, Enumerations

User Defined Sorts

Algebraic Data Types (ADT) (Recursive data structures)

### Expressions

### Constraints

## Examples

```python
x = Real('x')
y = Real('y')
s = Solver()
s.add(x + y > 5, x > 1, y > 1)
print(s.check())
print(s.model())
```



### Sudoku Solver

## References

[Programming Guide - Microsoft](https://z3prover.github.io/papers/programmingz3.html)

[Python Tutorial - Microsoft](https://microsoft.github.io/z3guide/programming/Z3%20Python%20-%20Readonly/Introduction)

[Z3 - Github](https://github.com/Z3Prover/z3)
