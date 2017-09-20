from prac_07.Guitar import Guitar

guitars = []
count = -1
name = input('Name: ')
while name != '':
    count += 1
    # year = input('Year: ')
    # cost = int(input('Cost: '))
    # temp_guitar = Guitar(name, year, cost)
    # guitars.append(temp_guitar)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print('{self.name} ({self.year}), worth ${self.cost:>,.2f}'.format(self=guitars[count]))
    name = input('Name: ')
for i,guitar in enumerate(guitars):
    if guitar.is_vintage() is False:
        print('Guitar {}: {self.name} ({self.year}), worth ${self.cost:>,.2f}'.format(i, self=guitar))
    else:
        print('Guitar {}: {self.name} ({self.year}), worth ${self.cost:>,.2f} (vintage)'.format(i, self=guitar))

