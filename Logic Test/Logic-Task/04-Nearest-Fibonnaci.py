arr = [15, 1, 3]

def find_nearest_fibonacci(arr):
    # initialize the Fibonacci sequence with the first two numbers
    fib_seq = [1, 1]
    # loop through the sequence until the sum is greater than or equal to the target sum
    while fib_seq[-1] < sum(arr):
        # add the next number to the sequence by adding the two previous numbers
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    # find the two Fibonacci numbers that are closest to the target sum
    a, b = fib_seq[-2], fib_seq[-1]
    if sum(arr) - a < b - sum(arr):
        return abs(sum(arr) - a)
    else:
        return abs(b - sum(arr))
        
print(find_nearest_fibonacci(arr))