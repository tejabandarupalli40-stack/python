"""
#comparison operation
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)



#age eliglibity
age = int(input("enteryour age:"))

print("eligibity:", age>=18) 

#pass or fail checker
marks = int(input("Enter marks"))

print("passed:", marks >=40)


#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

print(username == correct_username )
print(password == correct_password )


#logical operators
age = 25
citizen = True
print(age >= 18 and citizen == True)

age = 16
citizen = True

print(age >= 16 and citizen == True)

has_card = False
has_cash = True

print(has_card or has_cash)

is_logged_in = True
print(not is_logged_in)


#atm eligibility checker
balance = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)


#student scholarship eligibility checker
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

eligible = marks >=85 and attendance >= 75
print("scholarship Eligible:", eligible)


#identity operator 
a = None

print(a is None)
print(a is not None)


#bitwise operators
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)

#electronic store discount calculator
units = int(input("Enter number of units : "))

rate = 6

bill=units*rate

#travel expense calculator
travel = float(input(" travel expense: "))
food = float(input("food expense: "))
hotel = float(input("hotel expense: "))

total = travel + food + hotel

print("total expense:", total)
#aZ list in python :
#accessing element in the list:
marks = [80 ,90 ,75 ,85 ]
print(marks[0])        #output = 80
print(marks[1])        #output=90	
print(marks[3])        #output=85

#change element in list
makes = [80, 90, 75]

makes[1] = 95

print(makes)

#add element to a list
makes = [80, 90, 75]

makes.append(85)

print(makes)
#remove element from a list
makes = [80, 90, 75]

makes.remove(90)

print(makes)
#remove element from a list 
makes = [80, 90, 75]

makes.remove(90)
print(makes)

#insert element in a list
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)

numbers = [10, 20, 30]

numbers.clear()
print(numbers)

numbers = [10, 20, 30,40]

print(numbers.index(10))
numbers = [10, 20,20, 30, 20]
print(numbers.count(20))

numbers = [ 40, 10, 30, 20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers = [ 10, 20 ,30,40]
numbers.reverse()
print(numbers)

a = [1, 2, 3]

b = a.copy()
print(b)

numbers = [10, 20, 30, 40,50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:5])
print(numbers[::-1])

#tuples in python
#tuple is a collection of value that is ordered and cannot be changed
student = ("chandra sekher", 98, "python")
print(student[0])

#access value in a tuple
student = ("chandra sekher", 21,85.5)
print(student[0])
print(student[1])
print(student[2])

#imutable natural of tuple
student = ("chandra sekher", 21, 85.5)

print(student[0])

#tuple are immutable, meaning you cannot change be after
numbers = (10, 20, 40, 30, )


numbers = (10, 20,  30, 40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#set is a collection of unique values that is unordered and mutable
numbers = {10, 20, 30, 20, 10}
print(numbers)

total_minutes = int(input("Enter total number of minutes: "))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60
total_seconds = total_minutes * 60

print(f"Hours: {hours}")
print(f"Remaining Minutes: {remaining_minutes}")
print(f"Total Seconds: {total_seconds}")
"""
# program 8: power calculator
# read user input
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
# calculate the power of and print the result
print(base ** exponent)

# program 9: average of three numbers
# taking 3 numbers as input from the user
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
# find the total
total = n1 + n2 + n3
# find the average
average = total / 3 # division operator / --> always give
# print the average
print(average)
