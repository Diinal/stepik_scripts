queue = []
code = {}

def extract_min():
    m = float('inf')
    res = 0
    for i in range(len(queue)):
        if not queue[i][2]:
            if queue[i][1] < m:
                m = queue[i][1]
                res  = i
    queue[res][2] = True
    return res


def up(tree, node):
    if node == -1:
        return ''

    next = tree[node][0]

    if node not in code:
        code[node] = up(tree, next) + tree[node][1]
    
    return code[node]

def coder(s):
    encode_s = ''
    tree = {}
    d = {}
    for sym in s:
        if sym not in d:
            d[sym] = ['']
            d[sym].append(1)
        else:
            d[sym][1] += 1

    if len(d) == 1:
        code.update({s[0]: '0'})
        #print(code_table)
        return d, '0'

    for sym in d:
        queue.append([sym, d[sym][1], False])
        tree[sym] = [-1, '1']
    
    for k in range(len(queue), 2 * len(queue) - 1):
        i = extract_min()
        j = extract_min()
        new_node = queue[i][1] + queue[j][1]
        queue.append([new_node, new_node, False])
        tree[new_node] = [-1, '']
        tree[queue[i][0]] = [new_node, '0']
        tree[queue[j][0]] = [new_node, '1']
        #print(new_node, i, j)

    print('queue = ',queue)
    print('tree = ',tree)

    for sym in d:
        up(tree, sym)
    
    print('code table = ', code)

    for sym in s:
        encode_s += code[sym]

    return d, encode_s


s = 'abcdef'
uniq_w_d, encode_s = coder(s)
print(len(uniq_w_d), len(encode_s))

parse_code = []
for letter in code:
    if letter in uniq_w_d:
        parse_code.append([letter, code[letter]])

parse_code.sort(key = lambda x: x[1])
for pair in parse_code:
    print(pair[0] + ':', pair[1])
print(encode_s)

