class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Maruti(Car):
    def __init__(self, make, model, year, door, roof):
        self.door = door
        self.roof = roof
        super().__init__(make, model, year)

class Toyota(Car):
    def __init__(self, make, model, year, seats):
        self.seats = seats
        Car.__init__(self, make, model, year)


maruti = Maruti('Omni', 'M', 1999, 4, True)
print(maruti.door)
print(maruti.make)
toyota = Toyota('Toyota', 'M', 1999, 9)
print(toyota.seats)
print(toyota.make)