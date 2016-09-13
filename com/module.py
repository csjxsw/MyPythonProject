import test

for i in range(2):
    test.laugh()

def func(*name):
    print type(name)
    print name

func(1,4,6)
func(5,6,7,1,2,3)

def func(a):
    if a > 100:
        return True
    else:
        return False

print filter(func,[10,56,101,500])

print reduce((lambda x,y: x+y),[1,2,5,7,9])

re = iter(range(5))

try:
    for i in range(100):
        print re.next()
except StopIteration:
    print 'here is end ', i

print 'HaHaHaHa'