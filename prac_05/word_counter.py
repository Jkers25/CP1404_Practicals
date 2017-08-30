word_and_counts = {}
text = 'this is a collection of words of nice words this is a fun thing it is'
split_text = text.split()
for word in split_text:
    word_and_counts[word] = word_and_counts.get(word, 0) + 1
max_len_word = 0

sorted_words = []
for word in word_and_counts:
    sorted_words.append(word)
    sorted_words.sort()

    # temp_len = len(word)
    # if temp_len > max_len_word:
    #     max_len_word = temp_len
max_len_word = max((len(word)) for word in word_and_counts)
# print([len(word) for word in word_and_counts])

for word in sorted_words:
    print('{:{}} : {}'.format(word, max_len_word, word_and_counts[word]))
