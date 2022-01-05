class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        # if self.open_seats() == 0
        # python not逻辑操作数字，not 0 为ture, not 2 为false
        # not 对于空值为False, 实值为True
        if not self.open_seats():
            return False
        else:    
            self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)    

flight = Flight(3)
people = ["Harry", "Ron", "Herminoe", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Add {person} to flight successfully")
    else:
        print(f"No avaliable seats for {person}")    

