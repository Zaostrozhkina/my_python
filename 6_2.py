class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, weight=25, thickness=5):
        print(
            f'Масса асфальта = длина ({self._length} м) * ширина ({self._width} м) *'
            f' масса асфальта, толщиной в 1 см ({weight} кг) * толщина полотна ({thickness} см) ='
            f' {(self._length * self._width * weight * thickness) / 1000} тонн')


weight_road = Road(300, 200)
weight_road.mass_of_asphalt()
