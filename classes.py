class Person:
    def __init__(self, name, city="Roorkee", *args):
        self.name = name
        self.city = city
        #work =[]
        #i = 0
        if bool(args):
            self.work = args

    def show(self):
        print(f"My name is {self.name} and my current city is {self.city}")
