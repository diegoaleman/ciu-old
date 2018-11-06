# Properties
# 1. elements cannot be duplicates
# 2. elements are immutable, but set is mutable
# 3. indexing and slicing is not supported

# create set
days = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
months = {"Jan","Feb","Mar"}

# cannot access individual values, can access whole set
for d in days:
    print(d)

# add element to set
months.add("Apr")

# remove element from set
months.discard("Apr")

# Operations
s1 = {"Jan","Feb","Mar","Apr","Jun","Jul","Aug"}
s2 = {"Jan","Feb","Mar"}
s3 = {"Sept","Oct","Nov","Dic"}
s4 = {"Aug","Sept","Oct"}

# Union
union = s1 | s3

# Intersection
intersection = s3 & s4

# Difference
difference = s3 - s4

# Subset or Superset
subset = s2 <= s1
