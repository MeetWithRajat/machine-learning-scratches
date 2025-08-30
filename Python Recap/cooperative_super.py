class Maruti:
    def __init__(self, code=0, make=None, model=None, door=None, roof=None, **kwargs):
        print(Maruti)
        super().__init__(**kwargs)   # Passes control to Toyota
        self.code = code+2
        self.make = make
        self.model = model
        self.door = door
        self.roof = roof

class Toyota:
    def __init__(self, code=0, make=None, model=None, seats=None, **kwargs):
        print(Toyota)
        super().__init__(**kwargs)   # Passes control to object
        self.code = code+1
        self.make = make
        self.model = model
        self.seats = seats

class Hybrid(Maruti, Toyota):
    def __init__(self, code=0, make=None, model=None, door=None, roof=None, seats=None, dashboard=None, **kwargs):
        print(Hybrid)
        super().__init__(code=code, make=make, model=model, door=door, roof=roof, seats=seats, **kwargs)
        self.dashboard = dashboard

demo = Hybrid(1, "Demo", "R1", 4, "Panoramio", 5, "Digital")
print(demo.code)
print(demo.dashboard)
print(demo.seats)
print(demo.roof)
print(demo.make)