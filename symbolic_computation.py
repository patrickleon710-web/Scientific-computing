from sympy import *

A = Matrix([[1,2],[3,4]])
print(A)

# QUESTION 1

x = symbols('x')
loss = 3*x**2 + 2*x - 5
gradient = diff(loss, x)
print(gradient)
solution = solveset(Eq(gradient, 0), x)
solution2 = solveset(gradient - 0, x)
solution3 = solveset(gradient, x)
print(solution)
print(solution2)
print(solution3)
grad_prime = diff(gradient, x)
if grad_prime > 0:
    print("Minimum")
else:
    print("Maximum")
print(grad_prime)


# QUESTION 2

A = Matrix([[2, 1], [1, 3]])

det_A = A.det()
print(f"Determinant of A: {det_A}")

eigenvalues = A.eigenvals()
print(f"Eigenvalues of A: {eigenvalues}")

char_poly = A.charpoly()
print(f"Characteristic polynomial of A: {char_poly.as_expr()}")

for eigenvalue in eigenvalues:
    verification = char_poly.as_expr().subs(x, eigenvalue)
    print(f"Verification for eigenvalue {eigenvalue}: {verification}")

 # QUESTION 3
    
s = symbols('s')
H = 1 / (s**2 + 3*s + 2)

denominator_factors = factor(s**2 + 3*s + 2)
print(f"Factored denominator: {denominator_factors}")

t = symbols('t')
h_t = inverse_laplace_transform(H, s, t)
print(f"Inverse Laplace Transform h(t): {h_t}")

poles = solve(s**2 + 3*s + 2, s)
print(f"Poles of the system: {poles}")

# QUESTION 4

C = 5*x**3 - 10*x**2 + 4*x + 3

C_prime = diff(C, x)
print(f"First derivative (gradient) of C(x): {C_prime}")

optimal_x_C = solve(C_prime, x)
print(f"Optimal solution (x when gradient is zero): {optimal_x_C}")

C_double_prime = diff(C_prime, x)
for sol in optimal_x_C:
    second_derivative_at_sol = C_double_prime.subs(x, sol)
    if second_derivative_at_sol > 0:
        print(f"x = {sol} is a minimum.")
    else:
        print(f"x = {sol} is a maximum.")
        
# QUESTION 5

P, e, N = symbols('P e N')
C = P**e % N
print(f"Symbolic encryption function C = P^e % N: {C}")

P_val = 7
e_val = 3
N_val = 33
C_val = pow(P_val, e_val, N_val)
print(f"Ciphertext C for P=7, e=3, N=33: {C_val}")

P_inverse = mod_inverse(P_val, N_val)
print(f"Modular inverse of P=7 mod N=33: {P_inverse}")

decrypted_message = (C_val * P_inverse) % N_val
print(f"Decrypted message: {decrypted_message}")