# Question 2
# For this challenge, create a cone class that has two attributes:
# *R=Radius
# *h=Height
# And two methods
# Volume = π r2 * (h/3)
# Surface area : base = π r2, side = π r sqrt(r2+h2)
# Make only one class with functions, as in where required import Math¶


import math as m


class Cone:
    def __init__(self):
        self.radius = 0
        self.height = 0
        self.set_parameters()
        self.calc_Volume()
        self.calc_TSA()

    def set_parameters(self):
        radius = float(input("Enter the Radius: "))
        self.radius = radius

        height = float(input("Enter the Height: "))
        self.height = height

    def calc_Volume(self):
        r = self.radius
        h = self.height
        volume = m.pi * m.pow(r, 2) * (h / 3)
        print("\nVolume : %0.2f" % volume)

    def calc_TSA(self):
        r = self.radius
        h = self.height
        base = m.pi * m.pow(r, 2)

        side = m.pi * r * m.sqrt(m.pow(r, 2) + m.pow(h, 2))

        print("\nSurface Areas")
        print("Base  : %0.2f" % base)
        print("Side  : %0.2f" % side)
        print("Total : %0.2f" % (base + side))



c1 = Cone()
