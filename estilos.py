def solution(number):
     return sum(x for x in range(number))

print(solution(10))

def peso(cosa):
     return sum((x for x in cosa if x!=200))

cosa=[200,800,300]

print(peso(cosa))
