'''
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
Input
The only input line contains a string of n characters.
Output
Print one integer: the length of the longest repetition.
'''
def repetition(string): 
    max_re = 1
    for i in range(len(string)): 
        if string[i] == string[i+1]: 
            max_re +=1
        else: 
            
    return max(dis.values())

if __name__ == '__main__': 
    inp = input()
    max_v = repetition(inp)
    print(max_v)