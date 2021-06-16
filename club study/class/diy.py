class Card:
    def __init__(self, number, kind):
        if 1 > number or 13 < number:
            print(f'number 값 경고: {number}')
        self.number = number

        if kind != 'heart' and kind != 'diamond' and kind != 'club' and kind != 'spade':
            print(f'kind 값 경고: {kind}')
        self.kind = kind

    def show(self):
        print(self.number, self.kind)

c = Card(1, 'dd')
c.show()
