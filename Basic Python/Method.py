#Creating a method - a function within a class

class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

study_room = Room()

study_room.length = 5.4
study_room.breadth = 20.3

study_room.calculate_area()

bathroom = Room()

bathroom.length = 123.2
bathroom.breadth = 144.6

bathroom.calculate_area()