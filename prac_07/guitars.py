from prac_07.Guitar import Guitar

print('My Guitars')
guitars = []
name = input('Name: ')
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
while name != '':
    # year = int(input('Year: '))
    # cost = int(input('Cost: '))
    # guitars.append(Guitar(name, year, cost))
    print('{self.name} ({self.year}), worth ${self.cost:>,.2f} added.'.format(self=guitars[-1]))
    name = input('Name: ')
for i, guitar in enumerate(guitars):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"

    print(
        'Guitar {0}: {self.name} ({self.year}), worth ${self.cost:>,.2f} {1}'.format(i + 1, vintage_string, self=guitar))
