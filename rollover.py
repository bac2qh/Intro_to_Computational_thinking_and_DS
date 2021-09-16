"""
score = ((60-(a+b+c+d+e))*F + a*ps1 + b*ps2 + c*ps3 + d*ps4 + e*ps5)

objective: 
    given values for F, ps1, ps2, ps3, ps4, ps5
    find values for a, b, c, d, e that maximize score 

constraints: 
    a, b, c, d, e, are each 10 or 0
    a + b + c + d + e >= 20
"""

import random 
import numpy as np 

F = random.randint(0, 9)
ps1 = random.randint(0, 9)
ps2 = random.randint(0, 9)
ps3 = random.randint(0, 9)
ps4 = random.randint(0, 9)
ps5 = random.randint(0, 9)

params = [F, ps1, ps2, ps3, ps4, ps5]

def bestBF(params): # brute force way 
    bestResult = 0
    base = [10, 10, 10, 10, 10]
    for i in range(2**len(base)):
        form = f'0{len(base)}b'
        ib = [int(i) for i in list(format(i, form))]
        if sum(ib) >= 2:
            coef = np.array(ib) * np.array(base)
            result = (
                (60-(sum(coef)))*params[0] +
                coef[0] * params[1] +
                coef[1] * params[2] +
                coef[2] * params[3] +
                coef[3] * params[4] +
                coef[4] * params[5]
            )
        else:
            continue
        if result > bestResult:
            bestResult = result
    return bestResult

print('brute forece result is ', bestBF(params))

# def bestScore(params, coef, x):
#     if x not in 
#     if bestScore(params, nodes[1:], withTake = True) > bestScore(params, nodes[1:], withTake = False):
#         return bestScore(params, nodes[1:]) 



def score(params, coef): # x being level 
    result = 60 * params[0] 
    for i in range(len(coef)):
        result += coef[i] * (params[i+1] - params[0])
    return result 


def bestScore(params, toConsider):
    if toConsider == []:
        result = 60 * params[0]
    else: 
        nextCoef = toConsider[0]
        i = len(params) - len(toConsider) - 1 # params is longer to begin with 
        # left branch
        take = bestScore(params, toConsider[1:])[0] + nextCoef * (params[i+1] - params[0])
        # right branch 
        notake = bestScore(params, toConsider[1:])[0]
        if take > notake: 
            result = notake 
        else: 
            result = take 
    return result, counter 


coef = [10, 10, 10, 10, 10]
print(bestScore(params, coef))
