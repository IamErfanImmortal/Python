class Car:
  """
  This class represents a car with a make and model.
  """

  def __init__(self, make, model):
    """
    This method initializes a Car object with the given make and model.

    Args:
        make: The make of the car (e.g., "Toyota").
        model: The model of the car (e.g., "Camry").
    """
    self.make = make
    self.model = model

  def display_info(self):
    """
    This method prints the make and model of the car.
    """
    print(f"Car Info:\n  Make: {self.make}\n  Model: {self.model}")

# Create Car objects for three different cars
car1 = Car("Ford", "Mustang")
car2 = Car("Honda", "Civic")
car3 = Car("Tesla", "Model S")

# Call the display_info method for each car
car1.display_info()
print("\n")  # Add a blank line for better separation
car2.display_info()
print("\n")  # Add a blank line for better separation
car3.display_info()
