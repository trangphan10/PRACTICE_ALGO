'''
Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
Output
Print the missing number.
'''
def find_missing(arr):
    ls = [(i+1) for i in range(len(arr)+1)]
    return sum(ls) - sum(arr)

if __name__ == '__main__': 
    inp = int(input())
    arr = list(map(int,input().split()))
    miss_number = find_missing(arr)
    print(miss_number)
    
    