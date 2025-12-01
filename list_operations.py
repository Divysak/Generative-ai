#1 Create list
lst = [1,2,3]
print(lst)

#2 Access first element
lst = [10,20,30]
print(lst[0])

#3 Negative index
lst = [5,6,7]
print(lst[-1])

#4 Update element
lst = [1,2,3]
lst[1] = 10
print(lst)

#5 Length of list
lst = [4,5,6]
print(len(lst))

#6 Append
lst = [1,2]
lst.append(3)
print(lst)

#7 Insert at index
lst = [1,3]
lst.insert(1,2)
print(lst)

#8 Remove element
lst = [1,2,3]
lst.remove(2)
print(lst)

#9 Pop last
lst = [1,2,3]
print(lst.pop())

#10 Pop index
lst = [10,20,30]
print(lst.pop(1))

#11 Extend list
a = [1,2]
b = [3,4]
a.extend(b)
print(a)

#12 Check element exists
print(2 in [1,2,3])

#13 Count element
print([1,1,2,3].count(1))

#14 Index of element
print([4,5,6].index(5))

#15 Copy list
lst = [1,2,3]
c = lst.copy()
print(c)

#16 Full slice
lst = [1,2,3,4]
print(lst[:])

#17 First 3 elements
lst = [1,2,3,4]
print(lst[:3])

#18 Last 2 elements
lst = [1,2,3,4]
print(lst[-2:])

#19 Slice step
print([1,2,3,4,5][::2])

#20 Reverse list
print([1,2,3][::-1])

#21 Middle slice
print([10,20,30,40,50][1:4])

#22 Replace slice
lst = [1,2,3,4]
lst[1:3] = [20,30]
print(lst)

#23 Skip slice
print([1,2,3,4,5][1::2])

#24 Clear list
lst = [1,2,3]
lst.clear()
print(lst)

#25 Copy slice
lst = [4,5,6]
print(lst[:])

#26 Sort ascending
lst = [5,2,9]
lst.sort()
print(lst)

#27 Sort descending
lst = [5,2,9]
lst.sort(reverse=True)
print(lst)

#28 Sorted without modify original
lst = [3,1,2]
print(sorted(lst))

#29 Min value
print(min([2,8,4]))

#30 Max value
print(max([2,8,4]))

#31 Sum
print(sum([1,2,3]))

#32 Multiply list items
lst = [2,3]
print(lst*3)

#33 Remove duplicates
print(list(set([1,1,2,3])))

#34 Count even numbers
print(sum(i%2==0 for i in [1,2,3,4]))

#35 List comprehension
print([x*x for x in [1,2,3]])

#36 Filter even numbers
print([x for x in range(10) if x%2==0])

#37 Find index of max
lst = [1,4,2]
print(lst.index(max(lst)))

#38 Map: square numbers
print(list(map(lambda x:x*x,[1,2,3])))

#39 Zip two lists
print(list(zip([1,2],[3,4])))

#40 Enumerate in loop
for i,v in enumerate([10,20]): print(i,v)
#41 Simple for loop
for i in range(5): print(i)

#42 While loop
i = 1
while i <= 3: print(i); i += 1

#43 Break usage
for i in range(5):
    if i == 3: break
    print(i)

#44 Continue usage
for i in range(5):
    if i == 2: continue
    print(i)

#45 Pass usage
for _ in range(3): pass
print("Done")

#46 Loop through list
for x in ["a","b","c"]: print(x)

#47 Sum in loop
s = 0
for i in [1,2,3]: s+=i
print(s)

#48 Reverse loop
for i in reversed([1,2,3]): print(i)

#49 Nested loop
for i in range(2):
    for j in range(2):
        print(i,j)

#50 Loop break on condition
for i in [5,7,9]:
    if i>6: print("Found"); break

#51 Function to print list
def show(lst): print(lst)
show([1,2])

#52 Sum of list
def add(lst): return sum(lst)
print(add([1,2,3]))

#53 Max in list
def get_max(lst): return max(lst)
print(get_max([4,8]))

#54 Count even
def evens(lst): return sum(i%2==0 for i in lst)
print(evens([1,2,3,4]))

#55 Reverse list
def rev(lst): return lst[::-1]
print(rev([9,8,7]))

#56 Remove last element
def rem(lst): lst.pop(); return lst
print(rem([2,3,4]))

#57 Check existence
def check(x,l): return x in l
print(check(2,[1,2,3]))

#58 Multiply by 2
def mul(lst): return [i*2 for i in lst]
print(mul([1,2]))

#59 Index of element
def find(lst,x): return lst.index(x)
print(find([5,6,7],6))

#60 Merge lists
def merge(a,b): return a+b
print(merge([1],[2,3]))

