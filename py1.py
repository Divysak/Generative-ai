#61 Create tuple
t = (1, 2, 3)
print(t)

#62 Tuple with different types
t = (1, "hi", 3.5)
print(t)

#63 Single element tuple
t = (5,)
print(t)

#64 Access element
t = (10, 20, 30)
print(t[1])

#65 Negative index
print((4,5,6)[-1])

#66 Length of tuple
print(len((7, 8, 9)))

#67 Tuple slicing
t = (1,2,3,4)
print(t[1:3])

#68 Check element exists
print(3 in (1,2,3))

#69 Tuple repetition
print((1,2)*3)

#70 Concatenate tuples
print((1,2)+(3,4))
#71 Convert list to tuple
print(tuple([1,2,3]))

#72 Convert tuple to list
print(list((4,5,6)))

#73 Count elements
print((1,1,2,3).count(1))

#74 Index of value
print((5,6,7).index(6))

#75 Max & Min
print(max((9,2,5)), min((9,2,5)))
#76 Attempting modification (shows immutability concept)
t = (1,2,3)
# t[1] = 10  # Error (Cannot change tuple)

#77 Tuple inside tuple
t = (1, (2,3))
print(t)

#78 Nested tuple indexing
t = (1, (10,20))
print(t[1][0])

#79 Packing tuple
a = 10, 20, 30
print(a)

#80 Unpacking tuple
a, b, c = (5, 6, 7)
print(a, b, c)

#81 Swap using tuple unpacking
x, y = 3, 8
x, y = y, x
print(x, y)

#82 Tuple iteration
for i in (1,2,3): print(i)

#83 Tuple comprehension using list workaround
print(tuple(x*x for x in (1,2,3)))

#84 Return multiple values
def info(): return 1,2
print(info())

#85 Join strings using tuple conversion
print("-".join(("A","B","C")))
#86 Sorted tuple (returns list)
print(sorted((3,1,2)))

#87 Reverse tuple
print((1,2,3)[::-1])

#88 Tuple from set
print(tuple({5,6,7}))

#89 Find occurrences of value
print((1,2,1,3).count(1))

#90 Convert string to tuple of characters
print(tuple("hello"))

#91 Tuple as dictionary key
d = {(1,2): "OK"}
print(d[(1,2)])

#92 Check all values true
print(all((True,1,5)))

#93 Check any value true
print(any((0,0,2)))

#94 Multiply numbers inside tuple
t = (2,3,4)
res = 1
for i in t: res *= i
print(res)

#95 Tuple length in loop
t = (10,20)
for i in range(len(t)): print(t[i])

#96 Min using loop
t = (3,8,1)
m = t[0]
for i in t:
    if i < m: m = i
print(m)

#97 Convert integers to strings
print(tuple(str(i) for i in (1,2,3)))

#98 Pair list into tuple
print(list(zip([1,2],[3,4])))

#99 Replace element (convert → modify → convert back)
t = (1,2,3)
lst = list(t)
lst[1] = 10
t = tuple(lst)
print(t)

#100 Duplicate check
t = (1,2,1)
print(len(t) != len(set(t)))

