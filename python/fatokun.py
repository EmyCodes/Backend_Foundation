#!/usr/bin/python3.11
import pulp

# Create a linear programming problem
problem = pulp.LpProblem("ServerOptimization", pulp.LpMinimize)

"""
try:
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    x3 = int(input("Enter x3: "))
    x4 = int(input("Enter x4: "))
except (TypeError, ValueError):
    print("x1, x2, x3 and x4 must be an int data type")
"""
# Define decision variables
x1 = pulp.LpVariable("x1", lowBound=0, cat=pulp.LpInteger)
x2 = pulp.LpVariable("x2", lowBound=0, cat=pulp.LpInteger)
x3 = pulp.LpVariable("x3", lowBound=0, cat=pulp.LpInteger)
x4 = pulp.LpVariable("x4", lowBound=0, cat=pulp.LpInteger)

# Define the objective function
problem += x1 + x2 + x3 + x4, "Total Servers"

# Add constraints
problem += x4 + x1 >= 6, "Shift 1 Constraint"
problem += x1 + x2 >= 14, "Shift 2 Constraint"
problem += x2 + x3 >= 10, "Shift 3 Constraint"
problem += x3 + x4 >= 4, "Shift 4 Constraint"

# Solve the problem
problem.solve()

# Print the results
if pulp.LpStatus[problem.status] == "Optimal":
    print("Optimal Solution:")
    print(f"x1 = {x1.varValue}")
    print(f"x2 = {x2.varValue}")
    print(f"x3 = {x3.varValue}")
    print(f"x4 = {x4.varValue}")
    print(f"Total Servers (Minimum) = {pulp.value(problem.objective)} servers")
else:
    print("No optimal solution found.")
