# l = ['a', 'b', 'c']
# l
# l[0] = 'A'
# l

# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)

# l = [1, 2, 3]
# l.append(4)
# print(l)

# l = [9, 1, -4, 3, 7, 11, 3]
# print(l.count(3))

# l = ['a', 'b', 'c', 'a']
# l.remove('a')
# print(l)

# l = [1, 2, 3]
# l.insert(0, 'A')
# print(l)

# l = [1, 2, 3]
# l.pop()
# print(l)

# l = [1, 2, 3]
# l.pop(0)
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort()
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort(reverse=True)
# print(l)

# l = [3, 1, 5, 4, 2]
# l.reverse()
# print(l)

# l = ['a', 'b', 'c', 'a']
# index = l.index('a')
# print(index)

l = []
while True:
    ans = input("add(e = exit):")
    if ans == 'e':
        break
    else:
        l.append(ans)
        print(l)

while True:
    ans = input('del(e=exit):')
    if ans == 'e':
        break
    else:
        while ans in l:
            l.remove(ans)
        print(l)
k = []
for i in l:
    if i in k:
        continue
    else:
        k.append(i)
for i in k:
    print(f'{i}有{l.count(i)}個')
