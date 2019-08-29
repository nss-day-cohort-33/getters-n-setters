# Object properties are not private. Oh no!
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"The {self.name} costs ${self.price}"

# car = Product("Mustang", 100)
# car.price = "fish"
# print(car)


# But we can make it harder to access them:
class Product:

  def __init__(self, name):
    self.name = name

  @property
  def price(self):
    try:
      return self.__price
    except AttributeError:
      return 0

  @price.setter
  def price(self, price):
    if isinstance(price, float):
      self.__price = price
    else:
      print("Gotta use a float, dummy")

  def __str__(self):
    return f"The {self.name} costs ${self.price}"


car = Product("Mustang")
print(car.name)
car.price = "monkey"
car.price = 500.00
print(car)
