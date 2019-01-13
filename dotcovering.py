def get_prior(array):
    p = {}
    for i in range(len(array)):
        p[array[i][1]] = 0
        for j in range(len(array)):
            if array[j][0] <= array[i][1] <= array[j][1]:
                p[array[i][1]] += 1
    #print(p)
    return p
                    

def sortSecond(val): 
    return val[1]  


def cover(n, array):
    array.sort(key=sortSecond)
    priority = get_prior(array)
    #print('________________________')
    buffer = {}
    for i in range(n):
        array[i].append(-1)
        buffer[i] = array[i]
    priority[-1] = -1
    for i in range(n):
        #print(buffer)
        for j in range(n):
            if i != j:
                if buffer[j][0] <= buffer[i][1] <= buffer[j][1] and priority[buffer[i][1]] > priority[buffer[j][2]]:
                    buffer[j][2] = buffer[i][1]
                    buffer[i][2] = buffer[i][1]
    result = set()
    for i in range (n):
        if buffer[i][2] == -1:
            buffer[i][2] = buffer[i][1]
        result.add(buffer[i][2])
    #print(buffer)
    return result


def cover2(n, array):
    array.sort(key=sortSecond)
    array[0][0] = array[0][1]

    result = set()
    for i in range(n):
        if i+1 < n:
            if array[i+1][0] <= array[i][0] <= array[i+1][1]:
                array[i+1][0]  = array[i][0] 
            elif array[i+1][0] <= array[i][1] <= array[i+1][1]:
                array[i+1][0]  = array[i][1] 
            else:
                array[i+1][0] = array[i+1][1]

    for i in range(n):
        result.add(array[i][0])
    return result

def cover3(n, array):
    array.sort(key=sortSecond)
    i = 0
    result = set()
    key = array[0][1]
    result.add(key)
    while i<len(array):
        if not (array[i][0] <= key):
            key = array[i][1]
            result.add(key)
        i += 1
    return result

    
n = 3
array = [[1, 3], [2, 5], [3, 6]]
print(cover3(n, array))
print('__________________________')
n = 4
array = [[4, 7], [1, 3], [2, 5], [5, 6]]
print(cover3(n, array))
print('__________________________')
n = 6
array = [[3, 3], [3, 4], [2, 5], [5, 6], [4, 7], [6, 8]]
print(cover3(n, array), "= 3 6")
print('__________________________')
'''n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split(' '))))

result = cover(n, array)
print(len(result))
result = list(result)
result = str(result)[1:-1]
result = result.replace(',', '')
print(result)'''

