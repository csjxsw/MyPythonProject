from itertools import *

rlt = imap(pow, [1, 2, 3], [1, 2, 3])

for num in rlt:
    print(num)

for m, n in product('abc', [1, 2]):
    print m, n

per = permutations('abc', 2)
for p in iter(per):
    print(p)
print ("--------------\n")
com = combinations('abc', 2)
for c in iter(com):
    print(c)
combinations_with_replacement('abc', 2) # 与上面类似，但允许两次选出的元素重复。即多了aa, bb, cc
