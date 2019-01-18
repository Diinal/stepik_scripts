import math

queue_max = []

def insert(x):
    queue_max.append(x)
    shift_up(len(queue_max) - 1)
    return x

def extract_max():
    m = queue_max[0]
    if len(queue_max) > 1:
        queue_max[0] = queue_max.pop()
        shift_down(0)
    return m

def shift_up(i):
    while queue_max[i] > queue_max[(i - 1) // 2] and (i-1) // 2 > -1:
        queue_max[i], queue_max[(i - 1) // 2] =   queue_max[(i - 1) // 2], queue_max[i]
        i = (i - 1) // 2

def shift_down(i):
    while i*2 + 1 < len(queue_max):
        left, right = 2*i+1, 2*i+2
        j = left
        if right < len(queue_max) and queue_max[right] > queue_max[left]:
            j = right
        if queue_max[i] >= queue_max[j]:
            break
        queue_max[i], queue_max[j] = queue_max[j], queue_max[i]
        i = j
'''
n = int(input())
result = []
for i in range(n):
    command = list(input().split(' '))
    if 'Insert' in command:
        insert(int(command[1]))
    elif 'Extract' in command[0]:
        result.append(extract_max())
for number in result:
    print(number)
'''
result = []
with open('input_queue_commands', 'r') as text:
        for line in text:
                command = list(line.split(' '))
                if 'Insert' in command:
                        insert(int(command[1]))
                elif 'Extract' in command[0]:
                        result.append(extract_max())
                print(queue_max, command)
for number in result:
    print(number)