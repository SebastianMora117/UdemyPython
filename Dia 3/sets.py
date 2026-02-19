sets = set([1,2 , 3, 4, 5])

print(type(sets))
print(sets)
#############################################
s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1.union(s2))  # Union of s1 and s2
#############################################
s1.add(6)
print(s1)
#############################################
s1.remove(2)
s1.discard(2)
print(s1)