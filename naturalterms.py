import time

def get_natural_terms(n):
    result = []
    sum_result = 0
    if n <= 2:
        return [n]
    
    i = 1
    while sum_result < n:
        if sum_result < n:
            if sum_result + i <= n:
                result.append(i)
                sum_result += i
            else:
                sum_result = sum_result -  result[-1] + i
                result[-1] = i
        i += 1
    return  result

def gnt2(n):
    i = 1
    numbers = []
    while n > 2*i:
        n -= i
        numbers.append(i)
        i += 1

    numbers.append(n)
    return numbers

n = 567269
s = time.time()
get_natural_terms(n)
print(time.time()-s)

s = time.time()
n = 567269
gnt2(n)
print(time.time()-s)

