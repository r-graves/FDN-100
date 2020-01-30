# -*- coding: UTF-8 -*-

s1 = str("For  instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man — for precisely the same reasons.")
s2 = str("The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the message was this: So long and thanks for all the fish.")

s1_split = set(s1.split(' '))
s2_split = set(s2.split(' '))
#s21 = str(s1_split[1])
count = 0

len1 = len(s1_split)
len2 = len(s2_split)
print(len1)
print(len2)


ints = len(s1_split.intersection(s2_split))

print(ints)
