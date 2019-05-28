
class Car:
    def __init__(self, brand, run_distance):
        self.brand = brand
        self._mileage = None
        self.mileage = run_distance

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, run_distance):
        self._mileage = int(round(run_distance, -1))

    def __repr__(self):
        _repr = self.__class__.__name__ + '(' + self.brand + ', ' + str(self._mileage) + ')'
        return _repr


if __name__ == '__main__':
    MyCar_1 = Car('Opel', 12)
    MyCar_2 = Car('Volvo', 18)

    print('MyCar_1 brand: {brand}, MyCar_1 mileage: {mileage}'
          .format(brand=MyCar_1.brand, mileage=MyCar_1.mileage))
    print('MyCar_2 brand: {brand}, MyCar_2 mileage: {mileage}'
          .format(brand=MyCar_2.brand, mileage=MyCar_2.mileage))
    print('* * * * * * * * * *')

    MyCar_1.mileage += 42
    print('MyCar_1 brand: {brand}, MyCar_1 mileage: {mileage}'
          .format(brand=MyCar_1.brand, mileage=MyCar_1.mileage))


# Check repr in console, just enter the instance name
