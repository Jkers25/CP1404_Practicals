name_input = input('Enter name: ')
name_file_w = open('Name.txt','w')
print(name_input, file=name_file_w)
name_file_w.close()

name_file_r = open('Name.txt', 'r')
print('Your name is ', name_file_r.read())
name_file_r.close()

total = 0
numbers = open('numbers.txt','r')
for i in numbers.readlines():
    total += int(i)
print(total)
numbers.close()
