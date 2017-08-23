"""Jake Kerswell"""


def main():
    name = get_name()
    interval = int(input('Input an interval'))
    print_name(name, interval)


def get_name():
    name = input("Input Name: ")
    while name == "":
        name = input("Input Name")
    return name


def print_name(name, interval):

    print(name[interval-1::interval])

if __name__ == '__main__':
    main()