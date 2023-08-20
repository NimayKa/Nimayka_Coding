def Fibonacci(n):
    # Base case: If n is 0, return 0
    if n <= 1:
        return 1
    # Recursive case: Compute Fibonacci(n) by summing Fibonacci(n-1) and Fibonacci(n-2)
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def FibonacciSequence(n):
    sequence = [Fibonacci(i) for i in range(n)]
    return sequence

num = int(input("Enter Number for Fibonacci:"))
output_sequence = FibonacciSequence(num)
print("Sequence: ",output_sequence)
