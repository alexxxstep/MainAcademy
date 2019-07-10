import random

class Flower:
    NAME = ''
    COLORS = ['white', 'yellow', 'blue', 'red', 'green', 'black', 'brown', 'azure', 'ivory', 'teal', 'silver', 'purple',
              'navy blue', 'pea green', 'gray', 'orange', 'maroon', 'charcoal', 'aquamarine', 'coral', 'fuchsia',
              'wheat', 'lime', 'crimson', 'khaki', 'hot pink', 'magenta', 'olden', 'plum', 'olive', 'cyan']
    count = 0

    def __init__(self, color='', price=0, days=0):
        self._color = color
        self._price = price
        self._days = days

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, n_color):
        if n_color in self.COLORS:
            self._color = n_color
        else:
            self._color = self.COLORS[random.randint(0, len(self.COLORS) - 1)]

    @property
    def price(self):
        n_price = self._price
        if self.days >= 10:
            n_price = self._price * 0.5
            # print('* price of {} changed -50% from {} to {}'.format(self.NAME, self._price, n_price))
            return n_price
        elif 5 < self.days < 10:
            n_price = self._price * 0.75
            # print('* price of {} changed -25% from {} to {}'.format(self.NAME, self._price, n_price))
            return n_price
        else:
            return n_price

    @price.setter
    def price(self, n_price):
        if n_price > 0:
            self._price = n_price
        else:
            self._price = 0

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, n_days):
        if n_days > 0:
            self._days = n_days
        else:
            self._days = 0


class Rose(Flower):
    NAME = 'Rose'
    COLORS = ['white', 'yellow', 'blue', 'red', 'green', 'black', 'brown', 'azure', 'ivory', 'teal', 'silver', 'purple']

    def __init__(self, color='', price=0, days=0, throns=True):
        self.throns = throns
        super().__init__(color, price, days)


class Astra(Flower):
    NAME = 'Astra'
    COLORS = ['navy blue', 'pea green', 'gray', 'orange', 'maroon', 'charcoal', 'aquamarine', 'coral', 'fuchsia']


class Tulpan(Flower):
    NAME = 'Tulpan'
    COLORS = ['wheat', 'lime', 'crimson', 'khaki', 'hot pink', 'magenta', 'olden', 'plum', 'olive', 'cyan']


class Bouquet:
    def __init__(self, *flowers):

        self.flowers = []
        for flower in flowers:
            self.add_flower(flower)

    def add_flower(self, flower):
        if isinstance(flower, Flower):
            self.flowers.append(flower)

    def get_prise(self):
        sum = 0
        for f in self.flowers:
            sum += f.price
        return sum

    def add_new_flowers(self, class_name, count):
        while count > 0:
            flw = globals()[class_name]()
            flw.color = Flower.COLORS[random.randint(0, len(Flower.COLORS) - 1)]
            flw.price = random.randint(10, 100)
            flw.days = random.randint(0, 20)
            self.add_flower(flw)
            count -= 1


n_flowers = [random.randint(1, 5) for i in range(3)]
print(n_flowers)

flrs = sum(n_flowers)
print(flrs)

new_bouquet = Bouquet()

print('* Roses - {}'.format(n_flowers[0]))
print('* Astrases - {}'.format(n_flowers[1]))
print('* Tulpans - {}'.format(n_flowers[2]))

new_bouquet.add_new_flowers('Rose', n_flowers[0])
new_bouquet.add_new_flowers('Astra', n_flowers[1])
new_bouquet.add_new_flowers('Tulpan', n_flowers[2])

n = 1
for f in new_bouquet.flowers:
    print('* {}.{} : color - {}, price - {}, days - {}'.format(n, f.NAME, f.color, f.price, f.days))
    n += 1
print(new_bouquet.get_prise())
