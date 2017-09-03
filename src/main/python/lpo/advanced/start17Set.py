print(set("my name is Eric and Eric is my name".split()))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a)
print(b)

print(a.intersection(b))
print(b.intersection(a))

# attended only one of the events
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))

# exercise

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

print(set(a).difference(set(b)))
