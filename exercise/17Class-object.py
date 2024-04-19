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

# Create a Car object
my_car = Car("Honda", "Civic")

# Call the display_info method to print car information
my_car.display_info()
