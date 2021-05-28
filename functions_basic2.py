# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: cuntdown(5) should return [5, 4, 3, 2, 1].
def countDown(num):
    list = []
    for x in range(num, -1, -1):
        list.append(x)
    return list
print(countDown(5))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1, 2]) should print 1 and return 2.
def printReturn(list):
    print(list[0])
    return(list[1])
printReturn([1, 2])

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (firstvalue: 1 + length: 5).
def firstPlusLen(list):
    first = list[0]
    length = len(list)
    return first + length
print(firstPlusLen([1,2,3,4,5,6,7,8,9,10]))

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False.
def greaterSecond(list):
    newList = []
    count = 0
    for x in range(0, len(list), 1):
        if list[x] > list[1]:
            newList.append(list[x])
            count += 1
    print(count)
    if count < 2:
        return False
    else:
        return newList

print(greaterSecond([5, 2, 3, 2, 1, 4, 6, 8, 1, 1, 9]))

# 5. This Length, That Value - Write a function that accets two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4, 7) should return [7,7,7,7].
# Example: length_and_value(6, 2) should return [2,2,2,2,2,2].
def lenValue(size, value):
    list = []
    for x in range(0, size, 1):
        list.append(value)
    return list
print(lenValue(2, 1))
print(lenValue(4, 7))
print(lenValue(6, 2))
print(lenValue(8, 3))
print(lenValue(10, 5))