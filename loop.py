#151 Range loop
for i in range(5): print(i)
#152 Even numbers
for i in range(0,10,2): print(i)
#153 Backwards
for i in range(5,0,-1): print(i)
#154 While countdown
i=5
while i>0: print(i); i-=1
#155 find number
for i in [5,7,9]:
    if i==7: print("found")

#156 break
for i in range(5):
    if i==3: break
    print(i)
#157 continue
for i in range(5):
    if i==2: continue
    print(i)
#158 Nested loop
for i in range(2):
    for j in range(2): print(i,j)
#159 Sum 1–10
s=0
for i in range(1,11): s+=i
print(s)
#160 Multiplication table
for i in range(1,6): print(i*3)

#161 Square numbers
print([i*i for i in range(6)])
#162 Occurrence loop
count=0
for i in "banana":
    if i=="a": count+=1
print(count)
#163 Pass
for i in range(3): pass
print("done")
#164 Factorial
n=5; f=1
for i in range(1,n+1): f*=i
print(f)
#165 Loop + else
for i in range(3): print(i)
else: print("done")

#166 Reverse loop
for i in reversed([1,2,3]): print(i)
#167 enumerate
for i,v in enumerate("abc"): print(i,v)
#168 While break
i=1
while True:
    print(i)
    if i==3: break
    i+=1
#169 Continue while skip even
i=0
while i<5:
    i+=1
    if i%2==0: continue
    print(i)
#170 Nested continue
for i in range(3):
    for j in range(3):
        if j==1: continue
        print(i,j)

#171 Sum digits
n="12345"; print(sum(int(i) for i in n))
#172 Prime check
n=7
print("Prime" if all(n%i for i in range(2,n)) else "Not")
#173 Fibonacci
a,b=0,1
for _ in range(5): print(a); a,b=b,a+b
#174 Power table
for i in range(5): print(i,i**2)
#175 Odd numbers list
print([i for i in range(10) if i%2])

#176 Count vowels
print(sum(ch in "aeiou" for ch in "hello"))
#177 Find max in loop
m=0
for i in [4,8,1]: 
    if i>m: m=i
print(m)
#178 Reverse string manually
s="abc"; r=""
for i in s: r=i+r
print(r)
#179 Sum list loop
l=[1,5,9]; t=0
for i in l: t+=i
print(t)
#180 ASCII print
for i in "AB": print(ord(i))
