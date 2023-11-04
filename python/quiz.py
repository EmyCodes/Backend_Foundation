#!/usr/bin/node
#  you can write to stdout for debugging purposes, e.g.
print("this is a debug message")

def solution(S):
    # Implement your solution here
    result = S
    for _ in result:
        result = result[1:] + result[0]
        print(result)
solution("abbaa")
