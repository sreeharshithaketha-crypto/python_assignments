#create a tuple of five names
t= ("harshi","aashi","parri","anu","teju")
print(type(t))

#create and print tuple of numbers listing 1 to 10
t1=(1,2,3,4,5,6,7,8,9,10)
for i in range(10):
    print(t1[i])

#create an empty tuple
t2=tuple()
print(t2)
print(type(t2))

#create a tuple with only one element
t3=tuple('H')
print(t3)

#print all elements in a tuple
print(t)

#find the length of the tuple
print(len(t1))

#finding the first element of tuple
print(t1[0])

#finding the last element of tuple
print(t1[-1])

#access the third elemnt of a tuple
print(t1[2])

#print the first four elements using slicing
print(t1[:3])

#create a tuple of ten numbers and print index 2 to index 6
print(t1[2:7])

#PRINT LAST THREE TUPLE ELEMENTS
print(t1[-3::])

#print all elements except the first element
print(t1[1::])

#print all elements except the last element
print(t1[0:-1])

#reverse a tuple using slicing method
print(t1[::-1])

#print alternate element of a tuple
print(t1[0:-1:2])

#print elements at even index positions
print(t1[::2])

#print elements at odd even positions
print(t1[1::2])

#find the index of a given element
print(t1.index(9))

#check whether value exists in tuple or not
print(3 in t1)

#create a tuple with repeated values and count
t4=(1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,5,5,5,5,5,6,6,6)
print(t4.count(6))

#find the index of python
t5=("python","java","c","c++")
print(t5.index("python"))

#count how many tens are in the tuple
t6=(10,10,10,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7)
print(t6.count(10))

#find the first occurence of a value using index
print(t1[0])

#check whether java is in tuple
print("java" in t5)

#concat of two tuples
t6=t1+t3
print(t6)

#repeat a tuple three times
print(t1*3)

#converrt a list into tuple
l=[1,2,3,4,5]
t7=tuple(l)
print(t7)
print(type(t7))

#add a new element to a tuple by creating a new tuple
t8=(1,5,6,7,8)
t9=tuple('A')
t10 = t8 + t9
print(t10)

t11=t+("yashu",)
print(t11)

#remove and element from tuple by converting into a list
li=(1,2,3,4,5,6,7,8,9,10,11)
li2=list(li)
li2.remove(2)
print(li2)

#replace a element in tuple by converting into a list
li3=list(li)
li3[4]=5

# Create a tuple from user input values
n = int(input("Enter n value: "))
li = []

for i in range(n):
    x = int(input("Enter value: "))
    li.append(x)

t1 = tuple(li)
print(t1)

# Create a tuple using tuple constructor
t2 = tuple((1,2,3,4,5))
print(t2)

# Create a tuple from a string
s = "harshi"
t3 = tuple(s)
print(t3)

# Find the maximum value in a tuple
t4 = (9,7,4,6,5,2)
print(max(t4))

# Find the minimum value in a tuple
print(min(t4))

# Find the sum of all values in a tuple
print(sum(t4))

# Find the average of numbers in a tuple
avg = sum(t4) / len(t4)
print(avg)

# Sort a tuple in ascending order
t5 = tuple(sorted(t4))
print(t5)

# Sort a tuple in descending order
t6 = tuple(sorted(t4, reverse=True))
print(t6)

#find the second largest number in a tuple
f=(9,6,7,4,8,2,5,3)
a=tuple(sorted(f,reverse=True))
print(a[1])

#count how many even and odd numbers are in a tuple
t8 = (1,2,3,4,5,6,7,8,9,10)
even = 0
odd = 0
for x in t8:
    if x % 2 == 0:
        even += 1
    else:
        odd+= 1
print("Even:", even)
print("Odd:", odd)

#create a tuple of students names and print them using for loop
students = ("harshi", "yashu", "teju", "anu")
for student in students:
    print(student)

#create a tuple marks and print marks only above 50
marks = (45, 67, 52, 38, 90)
for x in marks:
    if x > 50:
        print(x)

#create a tuple of numbers and print only even numbers
tup = (3, 4, 5, 6, 7, 8, 9, 1, 2, 10)
tup1=[x for x in tup if x % 2 == 0]
tup1=tuple(tup1)
print(tup1)

#create a tuple of numbers and print only odd numbers
tup2=[x for x in tup if x % 2 != 0]
tup2=tuple(tup2)
print(tup2)

#create a nested tuple containing marks and student details(name,course,marks)
students = (("harshi","python",95), ("anu","java",88), ("teju","c",76))
print(students)
for name, course, marks in students:
    print(name, course, marks)

