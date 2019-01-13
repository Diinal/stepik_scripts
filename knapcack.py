def knapsack(n, w, things):
    result = [0.0, 0.0]
    for thing in things:
        thing.append(thing[0]/thing[1])
    things.sort(key = lambda thing: thing[2], reverse = True)
    print(things)
    for thing in things:
        if w-result[1] >= 0:
            result[0] += thing[2] * min(w - result[1], thing[1])
            result[1] += min(w - result[1], thing[1])
    return result[0]


n = 3
w =  50
things = [[60, 20], [100, 50], [120, 30]]
print(knapsack(n, w, things))