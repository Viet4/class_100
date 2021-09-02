class Car(object):
    def __init__(self, color, model, seats, brand, speed):
        self.color = color
        self.model = model
        self.seats = seats
        self.brand = brand
        self.speed = speed

    def start(self):
        print("start the "+ self.color +" car")

    def stop(self):
        print("STOPPPPPPPPPPPPPPPPP")

tesla = Car("white", "y", "7", "tesla", "1234567890")

print(tesla.start())
print(tesla.speed)