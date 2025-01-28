//Implement Extended Euclidean algorithm//
# Function to implement the Extended Euclidean Algorithm
def extended_euclidean(a, b):
    # Base case: if b is 0, the GCD is a, and the coefficients are 1 and 0
    if b == 0:
        return a, 1, 0
    else:
        # Recursively call the function
        gcd, x1, y1 = extended_euclidean(b, a % b)
        
        # Update the coefficients based on the recursive call
        x = y1
        y = x1 - (a // b) * y1
        
        return gcd, x, y

# Example usage
a = 30
b = 20

gcd, x, y = extended_euclidean(a, b)

print(f"GCD of {a} and {b}: {gcd}")
print(f"Coefficients x and y: x = {x}, y = {y}")


//Sample Output//
GCD of 30 and 20: 10
Coefficients x and y: x = -1, y = 2
