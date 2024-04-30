import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "The roots are real and distinct: {:.2f} and {:.2f}".format(root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return "The root is real and repeated: {:.2f}".format(root)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return "The roots are complex: {:.2f} + {:.2f}i and {:.2f} - {:.2f}i".format(real_part, imaginary_part, real_part, imaginary_part)

# Test the function
print(solve_quadratic(1, -3, 2))  # Example usage
