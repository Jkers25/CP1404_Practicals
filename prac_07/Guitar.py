import datetime

current_year = int(datetime.datetime.now().year)


class Guitar:
    def __init__(self, name='', year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return '{} ({}) : ${:.2f}'.format(self.name, self.year, self.cost)

    def get_age(self):
        return current_year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False


if __name__ == '__main__':
    gibson = Guitar('Gibson', 1922, 16035.4)
    other_guitar = Guitar('Other Guitar', 2012, 4124.2)
    print('{} get age() - expected 95 got {}'.format(gibson.name, gibson.get_age()))
    print('{} get age() - expected 95 got {}'.format(other_guitar.name, other_guitar.get_age()))
    print('{} is_vintage() - expected True got {}'.format(gibson.name, gibson.is_vintage()))
    print('{} is_vintage() - expected False got {}'.format(other_guitar.name, other_guitar.is_vintage()))
