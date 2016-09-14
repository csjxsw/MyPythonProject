import math
import random

print (math.e)
print (math.pi)
a = random.choice(range(9))
print(a)
b = random.sample(range(9),6)
print(b)



all_people = ['Tom', 'Vivian', 'Paul', 'Liya', 'Manu', 'Daniel', 'Shawn']
random.shuffle(all_people)
for i,name in enumerate(all_people):
    print(i,':'+name)