#81 Create dict
d={"a":1,"b":2}; print(d)
#82 Access
print(d["a"])
#83 Add key
d["c"]=3; print(d)
#84 Modify
d["a"]=10; print(d)
#85 Delete key
del d["b"]; print(d)

#86 Keys
print(d.keys())
#87 Values
print(d.values())
#88 Items
print(d.items())
#89 get()
print(d.get("x",0))
#90 len()
print(len(d))

#91 Loop keys
for k in d: print(k)
#92 Loop items
for k,v in d.items(): print(k,v)
#93 Pop item
print(d.pop("a")); print(d)
#94 Clear
d.clear(); print(d)
#95 Update
d={"x":1}; d.update({"y":2}); print(d)

#96 Dict from list
print(dict([[1,2],[3,4]]))
#97 Dict comprehension
print({x:x*x for x in range(3)})
#98 Check key
print("x" in d)
#99 Default value
d.setdefault("z",5); print(d)
#100 Copy
d2=d.copy(); print(d2)

#101 Merge
a={"a":1}; b={"b":2}; a.update(b); print(a)
#102 Remove last
print(a.popitem())
#103 Convert tuple list
print(dict([(1,"A"),(2,"B")]))
#104 Max value lookup
d={1:10,2:5}; print(max(d,key=d.get))
#105 Nested dict
d={"a":{"b":2}}; print(d["a"]["b"])

#106 Count frequency
s="abba"; freq={}
for i in s: freq[i]=freq.get(i,0)+1
print(freq)

#107 Swap keys & values
d={"a":1,"b":2}; print({v:k for k,v in d.items()})
#108 Create dict from two lists
print(dict(zip(["a","b"],[1,2])))
#109 Filter dict
d={1:10,2:3,3:6}
print({k:v for k,v in d.items() if v>5})
#110 Sort by key
print(dict(sorted({3:"c",1:"a"}.items())))

#111 Sort by value
print(dict(sorted(d.items(), key=lambda x:x[1])))
#112 Remove specific
d={1:2,3:4}; d.pop(3); print(d)
#113 Dictionary to list
print(list({"a":1}.items()))
#114 Invert boolean mapping
print({True:False,False:True})
#115 All keys uppercase
d={"a":1,"b":2}
print({k.upper():v for k,v in d.items()})

#116 Unique dict
keys=["a","b","c"]; vals=[1,1,2]
print(dict.fromkeys(keys,0))
#117 Max key
print(max({5:"A",1:"B"}))
#118 Remove duplicates values
d={1:2,2:2,3:3}
out={}
for k,v in d.items():
    if v not in out.values(): out[k]=v
print(out)
#119 Safe remove
print(d.pop("x",None))
#120 Nested loop
d={1:[2,3]}
for k in d:
    for v in d[k]: print(k,v)
