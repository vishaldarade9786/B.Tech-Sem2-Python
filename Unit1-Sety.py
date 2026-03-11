
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print("Set A:", set_a)
print("Set B:", set_b)


set_a.add(70)
print("After add:", set_a)

set_a.update([80, 90])
print("After update:", set_a)


set_a.remove(20)
print("After remove:", set_a)

set_a.discard(100)
print("After discard:", set_a)


removed_element = set_a.pop()
print("Removed element using pop():", removed_element)
print("After pop:", set_a)


union_set = set_a.union(set_b)
print("Union:", union_set)

print("Union using | :", set_a | set_b)



intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)


print("Intersection using & :", set_a & set_b)


difference_set = set_a.difference(set_b)
print("Difference (A - B):", difference_set)

print("Difference using - :", set_a - set_b)


temp_set = {1, 2, 3}
temp_set.clear()
print("After clear:", temp_set)
