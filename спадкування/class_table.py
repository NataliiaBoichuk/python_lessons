class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class KitchenTable(Table):
    # доповнення батьківського конструктора
    def __init__(self, l, w, h, p):
        # old write
        # Table.__init__(self, l, w, h)
        super(KitchenTable, self).__init__(self, l, w, h)
        self.places = p

    def setPlaces(self, p):
        self.places = p


class DeskTable(Table):
    def square(self):
        return self.width * self.length


# Полное переопределение метода надкласса
class ComputerTable(DeskTable):
    def square(self, e):
        return self.width * self.length - e

# Дополнение, оно же расширение, метода
# class ComputerTable(DeskTable):
#    def square(self, e):
#        return DeskTable.square(self) - e


t1 = KitchenTable(2, 2, 0.7)
t2 = DeskTable(1.5, 0.8, 0.75)
t3 = KitchenTable(1, 1.2, 0.8)
t4 = Table(1, 1, 0.5)

print(t2.square())

# AttributeError
# print(t4.square())
