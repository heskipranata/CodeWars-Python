# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

def reversed_seq(n):
    result = []
    for x in range(n, 0, -1):
        result.append(x)
    return result

print(reversed_seq(5))
    
