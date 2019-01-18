import heapq
from collections import Counter, namedtuple

class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'

def encode(s):
    h = []  # инициализируем очередь с приоритетами
    for ch, freq in Counter(s).items(): # постоим очередь с помощью цикла, добавив счетчик, уникальный для всех листьев
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count1, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')

    encode_s = ''
    for sym in s:
        encode_s += code[sym]

    return code, encode_s
    
s = 'abacabad'
print(encode(s))