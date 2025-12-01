#181 Basic function
def hello(): print("Hello!")
hello()
#182 Return value
def add(a,b): return a+b
print(add(3,4))
#183 Default parameter
def show(n=5): print(n)
show()
#184 Multiple returns
def both(a,b): return a,b
print(both(2,3))
#185 Odd/Even
def check(n): return "Even" if n%2==0 else "Odd"
print(check(7))

#186 Factorial function
def fact(n):
    f=1
    for i in range(1,n+1): f*=i
    return f
print(fact(5))
#187 Prime function
def prime(n): return all(n%i for i in range(2,n))
print(prime(7))
#188 Max function
def maxi(l): return max(l)
print(maxi([1,5,3]))
#189 Count vowels
def vowels(s): return sum(ch in "aeiou" for ch in s)
print(vowels("apple"))
#190 Reverse string
def rev(s): return s[::-1]
print(rev("hello"))

#191 Lambda function
sq=lambda x:x*x; print(sq(4))
#192 *args
def total(*a): return sum(a)
print(total(1,2,3))
#193 **kwargs
def info(**k): print(k)
info(a=1,b=2)
#194 Function inside loop
for f in [lambda x:x*2, lambda x:x+2]: print(f(3))
#195 Positive filter
def pos(l): return [i for i in l if i>0]
print(pos([-1,2,3]))

#196 List sum using func
def s(l): r=0; 
for i in l: r+=i
print(r)
#197 Recursion factorial
def F(n): return 1 if n==0 else n*F(n-1)
print(F(5))
#198 map with lambda
print(list(map(lambda x:x+1,[1,2,3])))
#199 filter
print(list(filter(lambda x:x%2,[1,2,3,4])))
#200 Global variable
g=5
def show(): print(g)
show()

#201 Pass in function
def todo(): pass
todo()
#202 Area circle
def area(r): return 3.14*r*r
print(area(3))
#203 Square root
import math; print(math.sqrt(16))
#204 Celsius->Fahrenheit
def conv(c): return (c*9/5)+32
print(conv(10))
#205 Table function
def tab(n): 
    for i in range(1,6): print(n*i)
tab(3)

#206 Largest of 3
def big(a,b,c): return max(a,b,c)
print(big(5,9,2))
#207 Multiply list
def mul(l):
    p=1
    for i in l: p*=i
    return p
print(mul([2,3]))
#208 Armstrong
def arm(n):
    s=sum(int(d)**3 for d in str(n))
    return s==n
print(arm(153))
#209 Palindrome
def pal(s): return s==s[::-1]
print(pal("level"))
#210 Name greet
def g(n): print(f"Hi {n}")
g("Div")
