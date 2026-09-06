age_list = [22, 23, 24, 25, 26]
print("Original age_list:", age_list)

name_list = ["Dinu", "Arun", "Lakshmi", "Aswathy", "Divya"]
print("Original name_list:", name_list)

name_list.append("Yazhini")
print("\nAfter appending Yazhini:", name_list)

age_list.insert(2, 30)
print("After inserting 30 at index 2:", age_list)

name_list.remove("Yazhini")
print("After removing Yazhini:", name_list)

age_list.pop()
print("After popping the last element:", age_list)

age_list.extend([29, 30, 26])
print("After extending age_list:", age_list)

age_list.sort(reverse=True)
print("age_list in descending order:", age_list)

max_age = max(age_list)
min_age = min(age_list)
total_age = sum(age_list)
print("Maximum age:", max_age)
print("Minimum age:", min_age)
print("Sum of all ages:", total_age)

print("\nFirst element of name_list:", name_list[0])

print("Last element of name_list:", name_list[-1])

print("Elements from index 2 to index 4:", name_list[2:5])

print("name_list in reverse order:", name_list[::-1])

student_marks = {
    "Dinu": 92,
    "Arun": 78,
    "Lakshmi": 90,
    "Aswathy": 82,
    "Divya": 95
}
print("\nOriginal student_marks:")
print(student_marks)

print("\nMark of Dinu:", student_marks["Dinu"])

student_marks["Janani"] = 80
print("After adding Janani:")
print(student_marks)

student_marks["Arun"] = 82
print("After updating Arun's mark:")
print(student_marks)


print("\nAll Keys:")
print(student_marks.keys())

print("\nAll Values:")
print(student_marks.values())

print("\nAll Key-Value Pairs:")
print(student_marks.items())

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print("\nmy_set:", my_set)
# Sets do not allow duplicate values.Therefore, duplicate 'a' and 'i' are automatically removed.

try:
    my_set[4] = 's'
except TypeError:
    print("\nError: Set does not support indexing or item assignment.")
    print("Sets are unordered and their elements cannot be accessed using an index.")
    
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
print("\nSet 1:", set1)
print("Set 2:", set2)

print("Union of set1 and set2:", union_set)

print("Intersection of set1 and set2:", intersection_set)

score = float(input("\nEnter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent performance! Keep up the great work.")

elif score >= 4 and score <= 7:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")
