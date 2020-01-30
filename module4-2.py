names = ['ryan', 'mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl', 'luke', 'mark', 'robert', 'joseph', 'carl', 'michael', 'mark', 'henry', 'matthew']

names.extend(['stacy','ruth','amanda','kitty','ruth'])


list1 = {}
for x in names:
    if x in list1:
        list1[x] = list1[x] + 1
    else:
        list1[x] = 1

#get the maximum value
mv = max(list1.values())
#print the number of times the most common name occurs
print(mv)
for key, value in list1.items():
    if value == max(list1.values()):
        mk = key
#print the name of of the most common occurance
print(mk)


