list1 = [ [1,2,3], ['a','b'] ]

#soft copy of list 1 to list 2
list2 = list1
#Q1 I have created two copies of a list, the first item of the list contains [1,2,3], and the second item of the list contains['a','b']
print(id(list1),id(list2))
#Q2 the two lists take up the same place in memory
# setting an element to a new value
#this method should also change list2 since its a soft copy of list1
list1[0] = [5,6,7]
print(list2)
#Q3 as predicted above the 0 attribue of list2 was also changes with my alterations of list1

list2 = list1[:]
#Q4, the : copies the entire range of the list, this new list2 should be in a seperate place in memory since we already reassigned the variable
#once

list1[0] = [2,4,6]
print(list1[0])
print(list2[0])
print(id(list1),id(list2))
#Q5 The first element of list1 now contains 2,4,6, however the first element of list2 is still 5,6,7. This is likely because list1 and
#list2 no longer occupy the same place in memory, which the id above proves.


#q6 Note above that the 0 element of list1 was updated while first element of list 2 was not. Howver, when I run the below append of the
#element 1 it does change the element, since we have not yet touched that element a this point.
list1[1].append('c')
print(list1[1])
print(list2[1])