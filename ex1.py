import cmath

a = float(input())
b = float(input())
c = float(input())

discriminant = (b**2)-(4*a*c)
equation1 = (-b-cmath.sqrt(discriminant))/(2*a)
equation2 = (-b+cmath.sqrt(discriminant))/(2*a)

print("Equations are: ")
print(equation1)
print(equation2)