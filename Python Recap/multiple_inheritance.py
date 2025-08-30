class Maruti:
    def __init__(self, make, model, door, roof):
        self.make = make
        self.model = model
        self.door = door
        self.roof = roof

class Toyota:
    def __init__(self, make, model, seats):
        self.make = make
        self.model = model
        self.seats = seats

class Hybrid1(Maruti, Toyota):
    def __init__(self, make, model, door, roof, seats, dashboard):
        super().__init__(make, model, door, roof)
        super().__init__(make, model, seats) # This will fail because of MRO (Method Resolution Order)
        self.dashboard = dashboard

class Hybrid2(Maruti, Toyota):
    def __init__(self, make, model, door, roof, seats, ambient):
        Maruti.__init__(self, make, model, door, roof)
        Toyota.__init__(self, make, model, seats)
        self.ambient = ambient


demo1 = Hybrid1("Demo1", "R1", 4, True, 4, True)
print(demo1.make)
print(demo1.dashboard)
demo1 = Hybrid2("Demo2", "X1", 6, False, 9, "Led")
print(demo1.make)
print(demo1.ambient)
