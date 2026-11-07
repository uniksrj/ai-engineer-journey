s = "suraj"
# print(s[0:3])

whitespacing = " hi Suraj you are the great "
# print(whitespacing)
# print(whitespacing.strip())


newText = "hi this is text."
converted = newText.replace("hi", "")
# print(f"I'm Suraj or {converted.strip()}")


myList = [10,20,30,40,50]

myList.append(60)

myList.insert(0, 5)
myList.extend([70, 80, 90])

myList.remove(30)
myList.pop()
# print(myList)

tuppleData = ("suraj")

print(tuppleData[0])

setData = {10, 20, 30, 40, 50}
setData.add(60)
setData.update([70, 80, 90])
setData.remove(30) # remove will throw error if the element is not found in the set
if 30 in setData:
    setData.remove(30)
else:
    print("30 not found in set")

setData.discard(30) # discard will not throw error if the element is not found in the set
print(setData)

newSet1 = {100, 200, 300}
newSet2 = {200, 300, 400}
print(newSet1 | newSet2)  # Union we also use newSet1.union(newSet2)
print(newSet1 & newSet2) # Intersection we also use newSet1.intersection(newSet2)
print(newSet1 - newSet2) # Difference we also use newSet1.difference(newSet2)
print(newSet2 ^ newSet1) # Symmetric Difference we also use newSet1.symmetric_difference(newSet2)


# testing

a = {"a": 1, "b": 2}
b = a

a = {"c" : 3}
print(b)

no = 0 

if no > 0:
    print("this is a positive number")
elif no == 0:
    print("this is a zero")
else:
    print("this is a negative number")


value1 = int(input("Enter value 1 :"))
value2 = int(input("Enter value 2 :"))

if value1 > value2:
    print("value 1 is greater")

elif value1 < value2:
    print("value 2 is greater")

else:
    print("value is same")



# write a program to print table of a number

userInput = int(input("Enter the value :"))

for i in range(1, 11):
    print(f"{userInput} * {i} = {userInput * i}")