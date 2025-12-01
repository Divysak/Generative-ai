#121 String indexing
s="python"; print(s[0])
#122 Negative index
print(s[-1])
#123 Slice
print(s[1:4])
#124 Step
print(s[::2])
#125 Reverse
print(s[::-1])

#126 Length
print(len(s))
#127 Upper
print(s.upper())
#128 Lower
print(s.lower())
#129 Replace
print(s.replace("py","PY"))
#130 Split
print("a,b,c".split(","))

#131 Join
print("-".join(["x","y","z"]))
#132 Count
print("banana".count("a"))
#133 Starts with
print("hello".startswith("he"))
#134 Ends with
print("hello".endswith("lo"))
#135 isdigit
print("123".isdigit())

#136 Loop characters
for ch in s: print(ch)
#137 strip
print(" hi ".strip())
#138 find
print("apple".find("p"))
#139 Format
a,b=5,10; print(f"Sum={a+b}")
#140 Swap case
print("HeLLo".swapcase())

#141 Title case
print("hello world".title())
#142 Check alpha
print("abc".isalpha())
#143 Check alnum
print("abc1".isalnum())
#144 Multiply string
print("ha"*3)
#145 Replace multiple
print("a b c".replace(" ",""))

#146 Check substring
print("py" in "python")
#147 Convert to list
print(list("abc"))
#148 Ord/chr
print(ord('A'), chr(65))
#149 Center
print("hi".center(10,"-"))
#150 min/max char
print(min("dbca"), max("dbca"))
