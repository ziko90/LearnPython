a = {1 : 'a', 2 : 'c', 'b' : 232}

for key, value in a.items():
    print(key,value)

b = [ i**2 for i in range(0,6) if i%2 > 0]
print(b)

f = lambda: [4, 5, 6][[1, 2, 3][-2]]
print(f())

c = 123153253254645645988797893544454353487945434324543
numb = str(c)

while len(numb) > 1:
    numb = str(sum([int(x) for x in numb]))
    print(numb)

la = [1, 2, 3]
lb = [5, 4, 8]

for x, y in zip(la, lb):
    print(x, y)
print(list(zip(la,lb)))

for i, x in enumerate(lb):
    print(i, x)

for key in a.keys():
    print(key)

for key, value in a.items():
    print(key, value)

for value in a.values():
    print(value)

xx = {x for x in range(10)}
print(xx)
print(type(xx))
print(isinstance(xx, set))

bb = [1, 1, 1, 2, 3, 4, 5, 4, 5, 6]
print(bb)
print(set(bb))

ge = (x for x in range(10))
print(range(10))

2


def firstn(n):

    num = 0
    while num < n:
        print(num)
    yield num
    num += 1





dict = {x:x**2 for x in range(10) if x%2==0}
print(dict)

# print(a.get('1', None))

z=((lambda x: 2*x*x)(5))
print(z)

print((lambda a, b: a+b)(2,3))
print(range(10))
print(type(z))

print(a.get('a', 'no a in dict'))

print(a is b)

for k, z in zip(la,lb):
    print(k,z)

tta = 'abdasdsa sadsa dsadsa'
print(tta.split())

square = lambda x: x**2

print(square(8))

xxx=zip(la,lb)
#print(xxx)
for x, y in xxx:
    print(x, y)
print('******************')
for key, value in a.items():
    print(key,value)

for x in range(10):
    print(True if x > 5 else False)

testowa = [1, 2, 3, 4, 1, 8, 10]
print(testowa)
print(testowa[2])
print(testowa[-1])
print(testowa[2:6])