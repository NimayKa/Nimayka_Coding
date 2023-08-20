def Fibonacci(n):
    if n <= 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def FibonacciSequence(n):
    sequence = [Fibonacci(i) for i in range(n)]
    return sequence

num = int(input("Enter Number for Fibonacci:"))
output_sequence = FibonacciSequence(num)
print("Sequence: ",output_sequence)
