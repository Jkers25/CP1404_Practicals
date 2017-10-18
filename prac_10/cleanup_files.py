"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for dir_name, dirs_files, files in os.walk('..'):
        for filename in files:
        # ignore directories, just process files
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                print(new_name)

                # Option 1: rename file to new name - in place
                # os.rename(filename, new_name)

                # Option 2: move file to new place, with new name
                # shutil.move(filename, 'temp/' + new_name)

                # Processing subdirectories using os.walk()

                # os.chdir('..')  # .. means "up" one directory
                # for dir_name, subdir_list, file_list in os.walk('.'):
                #     print("In", dir_name)
                #     print("\tcontains subdirectories:", subdir_list)
                #     print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    is_previous_space = False
    number_of_spaces = 0
    temp_list = []
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    for i, char in enumerate(filename):
            if char.isupper() and i > 0 and not is_previous_space:
                temp_list.append('_')
                number_of_spaces += 1
                is_previous_space = False

            elif char == '_':
                is_previous_space = True

            if i > 0 and(temp_list[i-1 + number_of_spaces] == '_'):
                temp_list.append(char.upper())
            elif i == 0 and char.islower():
                temp_list.append(char.upper())
            else:
                temp_list.append(char)



    new_name = ''.join(temp_list)
    # TODO: step-by-step, consider the problem cases and solve them

    return new_name


main()