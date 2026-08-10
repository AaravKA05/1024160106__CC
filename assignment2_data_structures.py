"""
UCS420: Cognitive Computing
Assignment 2 - Python Data Structures (Lists, Tuples, Sets, Dictionaries)

Name   : Aarav
Roll No: 1024160106
Branch : CSE
"""

import random

ROLL_NUMBER = "1024160106"

print("=" * 60)
print("QUESTION 1 - LISTS")
print("=" * 60)

# Extract individual digits of the roll number and multiply each by 10
digits = [int(d) for d in ROLL_NUMBER]
L = [d * 10 for d in digits]

# i. Print L
print("i.  L =", L)

# ii. Add two numbers - one using append(), one using insert() at a
#     specific position
L.append(25)
# append() adds the new element (25) at the END of the list
print("ii. After append(25)      -->", L)

L.insert(3, 99)
# insert(3, 99) places 99 at index 3, shifting every element from
# index 3 onward one position to the right (list grows by 1 either way)
print("    After insert(3, 99)   -->", L)

# iii. Remove two elements - one using remove(), one using pop()
L.remove(99)
# remove(99) deletes the FIRST occurrence of the VALUE 99 from the list
print("iii. After remove(99)     -->", L)

popped = L.pop()
# pop() removes and returns the LAST element of the list (here: popped)
print(f"    After pop() (removed {popped}) -->", L)

# iv. Sort ascending, then descending
L_ascending = sorted(L)
print("iv. Ascending  -->", L_ascending)

L_descending = sorted(L, reverse=True)
print("    Descending -->", L_descending)

# v. Slicing - first three and last three elements
print("v.  First three elements -->", L[:3])
print("    Last three elements  -->", L[-3:])

# vi. List comprehension - elements greater than the average of L
avg_L = sum(L) / len(L)
above_avg = [x for x in L if x > avg_L]
print(f"vi. Average of L = {avg_L}")
print("    Elements above average -->", above_avg)


print("\n" + "=" * 60)
print("QUESTION 2 - TUPLES")
print("=" * 60)

# Tuple of 8 marks: first 8 values from the ORIGINAL list L (before
# the append/insert/remove/pop edits above), i.e. digit * 10
original_L = [d * 10 for d in digits]
scores = tuple(original_L[:8])
print("scores =", scores)

# i. Highest score + its index, lowest score + how many times it appears
highest = max(scores)
highest_index = scores.index(highest)
lowest = min(scores)
lowest_count = scores.count(lowest)
print(f"i.  Highest score = {highest} at index {highest_index}")
print(f"    Lowest score  = {lowest}, appears {lowest_count} time(s)")

# ii. Reverse the tuple, returned as a list
reversed_scores = list(scores[::-1])
print("ii. Reversed scores (as list) -->", reversed_scores)
# Tuples are immutable in Python - once created, their contents (and
# therefore their order) can never be changed in place, so reversing
# a tuple "in place" is impossible; we can only build a NEW sequence
# (here, a list) that holds the elements in reverse order.

# iii. Ask user for a score, find its first occurrence index (or say
#      it's not present)
user_score = int(input("iii. Enter a score to search for: "))
if user_score in scores:
    print(f"    {user_score} found at index {scores.index(user_score)}")
else:
    print(f"    {user_score} is not present in scores")

# iv. Attempt to change one element of the tuple directly
print("iv. Attempting scores[0] = 100 ...")
try:
    scores[0] = 100
except TypeError as e:
    print("    Error raised:", e)
    # Python raises a TypeError because tuples do not support item
    # assignment - they are immutable, unlike lists, where L[0] = 100
    # is perfectly legal because lists are mutable.

# v. Unpack into first, second, and the rest using *
first_score, second_score, *remaining_scores = scores
print("v.  first_score      -->", first_score)
print("    second_score     -->", second_score)
print("    remaining_scores -->", remaining_scores)


print("\n" + "=" * 60)
print("QUESTION 3 - RANDOM NUMBERS")
print("=" * 60)

random.seed(int(ROLL_NUMBER))  # reproducible but unique to this roll number

# i. Generate a list of 100 random numbers between 100 and 900 (inclusive)
random_list = [random.randint(100, 900) for _ in range(100)]
print("i.  Random list (100 numbers):")
print("   ", random_list)

# ii. Count and print all odd numbers
odds = [n for n in random_list if n % 2 != 0]
print(f"ii. Odd numbers   -> count = {len(odds)}")
print("    Odd numbers list  -->", odds)

# iii. Count and print all even numbers
evens = [n for n in random_list if n % 2 == 0]
print(f"iii. Even numbers -> count = {len(evens)}")
print("    Even numbers list -->", evens)


def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# iv. Count and print all prime numbers, build list via comprehension
primes = [n for n in random_list if is_prime(n)]
print(f"iv. Prime numbers -> count = {len(primes)}")
print("    Prime numbers list -->", primes)

# v. Number that occurs most frequently, and how many times
most_common = max(set(random_list), key=random_list.count)
most_common_count = random_list.count(most_common)
print(f"v.  Most frequent number = {most_common}, "
      f"occurs {most_common_count} time(s)")


print("\n" + "=" * 60)
print("QUESTION 4 - SETS")
print("=" * 60)

# Same 8 digits of the roll number from Q1, BEFORE multiplying by 10
first_8_digits = digits[:8]
A = {d * 7 for d in first_8_digits}
B = {d * 9 for d in first_8_digits}
print("Set A (digit x 7) -->", A)
print("Set B (digit x 9) -->", B)

# vi. Union - all unique values across both sets
print("vi.   Union(A, B)        -->", A.union(B))

# vii. Intersection - values common to both
print("vii.  Intersection(A, B) -->", A.intersection(B))

# viii. Difference A-B and B-A separately
print("viii. A - B -->", A.difference(B))
print("      B - A -->", B.difference(A))
# difference() is a ONE-WAY (asymmetric) comparison - A - B only keeps
# elements unique to A, while symmetric_difference() combines BOTH
# "A only" and "B only" elements into a single result.

# ix. Symmetric difference of A and B
print("ix.   Symmetric difference(A, B) -->", A.symmetric_difference(B))

# x. Subset / superset checks
print("x.    Is A a subset of B?   -->", A.issubset(B))
print("      Is B a superset of A? -->", B.issuperset(A))

# xi. Discard a user-given value from set A
X = int(input("xi. Enter a value X to discard from set A: "))
A.discard(X)
print(f"    Set A after discard({X}) -->", A)
# discard() is safer than remove() because discard() does nothing if
# the value is not present in the set, while remove() raises a
# KeyError - so discard() avoids a crash when we're not sure the
# value actually exists in the set.


print("\n" + "=" * 60)
print("QUESTION 5 - DICTIONARIES")
print("=" * 60)

my_dict = {
    "name": "Aarav",
    "roll_no": "1024160106",
    "branch": "CSE",
    "age": 20,
    "city": "Shimla",
}
print("Original dictionary -->", my_dict)

# i. Rename key "city" to "location" without changing its value,
#    without hand-recreating the dictionary (works for ANY dictionary)
my_dict["location"] = my_dict.pop("city")
print("i.   After renaming city -> location -->", my_dict)

# ii. Add a new key "cgpa"
my_dict["cgpa"] = 7.89
print("ii.  After adding cgpa -->", my_dict)

# iii. Update "age" by increasing it by 1
my_dict["age"] += 1
print("iii. After updating age -->", my_dict)

# iv. Delete "branch" key using two different methods on two SEPARATE
#     copies of the dictionary
dict_copy_pop = my_dict.copy()
popped_branch = dict_copy_pop.pop("branch")
print("iv.  Copy after pop('branch')  -->", dict_copy_pop)
print("     pop() returned the removed value -->", popped_branch)

dict_copy_del = my_dict.copy()
del dict_copy_del["branch"]
print("     Copy after del dict['branch'] -->", dict_copy_del)
# pop("branch") REMOVES the key and RETURNS its value (useful if you
# need that value afterwards), while del just deletes the key-value
# pair and returns nothing at all.

# v. Iterate using .items() and print "key -> value"
print("v.   Iterating with .items():")
for key, value in my_dict.items():
    print(f"     {key} -> {value}")

# vi. Safely check for a key that doesn't exist ("email")
print("vi.  Checking for 'email' key:")
if "email" in my_dict:
    print("     Email -->", my_dict["email"])
else:
    print("     No 'email' key found for this user.")

# vii. Create a second dictionary with the same 5 original keys but a
#      friend's (fictional) details, then merge with **dict1, **dict2
friend_dict = {
    "name": "Rohan",
    "roll_no": "1024160199",
    "branch": "ECE",
    "age": 21,
    "city": "Manali",
}
merged_dict = {**my_dict, **friend_dict}
print("vii. friend_dict -->", friend_dict)
print("     Merged ({**my_dict, **friend_dict}) -->", merged_dict)
# When both dictionaries share a key, the value from the dictionary
# listed LAST in the merge wins - here friend_dict was unpacked
# second, so friend_dict's values overwrite my_dict's values for any
# shared key (name, branch, age, etc.).

# viii. Dictionary comprehension - only key-value pairs where the
#       value is a string
string_only_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("viii. String-valued entries only -->", string_only_dict)
