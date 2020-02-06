"""Homework week 5. The objective is to read a text file in, print the number of words, as well as the number of unique
words. THen, findthe most common word and the number of times it appears, and the number of words which appeared the least
number of times.
Then compute the percentage thatthe word who showed up the least number of times is of the total unique words in the book"""
import re
with open('./land_time_forgot.txt') as f:
   full_lines = f.readlines()

words = []

for l in full_lines:
   line = re.sub('\s\s+', ' ', re.sub('[^a-zA-Z]', ' ', l))
   #list will contain all words
   words.extend(line.split())

#use a set to find unique instances in the words list
settle = set()

for i in words:
    word_out = i
    settle.add(i)

#prints the number of total words and the number of unique words
out_1 = "The book contains " + str(len(words)) + " words, out of which " + str(len(settle))  + " are unique." +"\n"
print(out_1)

word_counts = {}

for x in words:
    if x in word_counts:
        word_counts[x] = word_counts[x] + 1
    else:
        word_counts[x] = 1


#get the minimum and maximum values from word counts
max_val = (max(word_counts.values()))
min_val = (min(word_counts.values()))
#note the sum is the same as the length of the words list, for extra validation
sum_val = (sum(word_counts.values()))

#using the value, I will loop through the dictionary to find the coresponding key
for key, value in word_counts.iteritems():
    if value == max_val:
        max_key = key
#print the most used word and the number of times used
out_2 = "The most common word in the book is '" + max_key + "', which appears " + str(max_val) + " times." + "\n"
print(out_2)
#now I must get the number of words with the minimum value
#build a list to contain all values
min_list = []
for key, value in word_counts.iteritems():
    if value == min_val:
        min_list.append(key)
#print the number of words where the minimum number of words is
out_3 = "There were " + str(len(min_list)) + " words that appeared " + str(min_val) + " times in the book." + "\n"
print(out_3)

#get the percent of one use words are we using percent of all words or percent of unique words
one_pct = "{0:.2f}%".format((float(len(min_list)) / float(len(settle))) * 100)
out_4 = str(one_pct) + " of unique words in the book appear only " + str(min_val) + " times." + "\n"
print(out_4)
