"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import time

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
FORMAT = 'cv'
word_format = ""
start_time = time.time()
word_length = random.randint(2, 8)
for i in range(word_length):
    word_format += random.choice(FORMAT)
# word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
counter = 0
dog_counter = 0
jake_counter = 0
trey_counter = 0
while word != 'quizzed':
    counter += 1
    if word == 'dog':
        dog_counter += 1
        print("Dogs" ,dog_counter)
    if word == 'jake':
        jake_counter += 1
        print('Jakes' ,jake_counter)
    if word == 'trey':
        trey_counter +=1
        print('Trey' ,trey_counter)
    word_format = ""
    word_length = random.randint(2, 8)
    for i in range(word_length):
        word_format += random.choice(FORMAT)
    # word_format = "ccvcvvc"
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
            # print(word)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print(counter)



