class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для ручки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для карандаша {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для маркера {self.title}')


stationery = Stationery('фломастер')
stationery.draw()

pen = Pen('паркер')
pen.draw()

pencil = Pencil('комус серый')
pencil.draw()

handle = Handle('Attache')
handle.draw()
