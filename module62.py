def main_fun(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        word_list = []
        for line in lines:
            word_list.extend(line.strip().split(" "))

        return(word_list)

def word_set(word_list):
        word_set = set(word_list)
        print("There are {} words in the book and {} of them are unique".format(
            len(word_list), len(word_set)))
        word_count = {}
        for word in word_list:
            if word in word_count:
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1

        max_word = max(word_count, key=word_count.get)
        wc = word_count[max_word]
        min_word = min(word_count.values())

        min_words = []
        for word, cnt in word_count.items():
            if cnt == min_word:
                min_words.append(word)

        min_word_ct = min_word

        return(max_word, wc, min_words, min_word_ct)

def max_word(max_word, word_count, min_words, min_word_count):
        print("The word that occurs most is '{}' with count {}".format(
            max_word, word_count))

        print("The lowest word count is {} and there are {} words "
              "in the book with that word_count".format(
            min_word_count, len(min_words)))


#call the main function

if __name__ == '__main__':
    file_name = "./land_time_forgot.txt"
    lo = main_fun(file_name)
    ws = word_set(lo)
  #  print(ws)
    ws0 = ws[0]
    ws1 = ws[1]
    ws2 = ws[2]
    ws3 = ws[3]
    mw = max_word(ws0,ws1, ws2, ws3)




