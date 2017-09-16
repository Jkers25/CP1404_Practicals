import datetime
current_year = int(datetime.datetime.now().year)


class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return current_year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __str__(self):
        return '{} ({}) : ${:.2f}'.format(self.name, self.year, self.cost)