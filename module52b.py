import re
with open('./land_time_forgot.txt') as f:
   full_lines = f.readlines()

list_of_words = []

for l in full_lines:
   line = re.sub('\s\s+', ' ', re.sub('[^a-zA-Z]', ' ', l))
   list_of_words.extend(line.split())
print('Total number of words is {0:6,d}.'.format(len(list_of_words)))

first_line_data = full_lines[0].split(", by")
project_and_title = first_line_data[0].strip().split("'s")
author = first_line_data[1].strip()
project = project_and_title[0]
title = project_and_title[1]

print('The author: {0:s}. The title: {1:s}. The project: {2:s}.'.format(author,title,project))

count_of_words = {}
for word in list_of_words:
   if count_of_words.get(word) is None:
       count_of_words[word] = 1
   else:
       count_of_words[word] += 1

max_key = max(count_of_words, key=lambda k: count_of_words[k])
max_count = count_of_words[max_key]
print('The word that appears most frequently is "{0:s}" ({1:5,d} times)'.format(
    max_key,max_count))





