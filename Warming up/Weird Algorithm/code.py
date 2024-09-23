# Consider an algorithm that takes as input a positive integer n. 
# If n is even, the algorithm divides it by two, 
# and if n is odd, the algorithm multiplies it by three and adds one.
# The algorithm repeats this, until n is one.
# import matplotlib.pyplot as plt
def Weird_Algo(n): 
    result = [n]
    while n != 1: 
        if n % 2 == 0: 
            n = n // 2 
        else: 
            n = n * 3 + 1 
        result.append(n)
    return result

if __name__ == '__main__':
    num = int(input())
    sequence = Weird_Algo(num)
    print(' '.join(str(i) for i in sequence))
    