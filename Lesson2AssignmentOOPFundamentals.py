# Lesson 2: Assignment | OOP Fundamentals
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

# 1. City Infrastructure Management System
# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
#     class Vehicle:
#         def __init__(self, reg_num, type, owner):
#             self.registration_number = reg_num
#             self.type = type
#             self.owner = owner
# Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.


class Vehicle:
  """
  A class representing a vehicle with registration number, type, and owner.
  """
  def __init__(self, reg_num, type, owner):
    self.registration_number = reg_num
    self.type = type
    self.owner = owner

  def update_owner(self, new_owner):
    """
    Updates the owner of the vehicle.
    """
    self.owner = new_owner

# Create some Vehicle objects
car = Vehicle("ABC123", "Car", "John Doe")
bike = Vehicle("DEF456", "Motorcycle", "Jane Smith")

# Print the initial owners
print(f"Car owner: {car.owner}")
print(f"Bike owner: {bike.owner}")

# Update the owners
car.update_owner("Mary Smith")
bike.update_owner("David Lee")

# Print the updated owners
print(f"Car owner (after update): {car.owner}")
print(f"Bike owner (after update): {bike.owner}")



# Task 2: Event Management System Enhancement

# Problem Statement: Use the existing Event class by adding an instance attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
#     class Event:
#         def __init__(self, name, date):
#             self.name = name
#             self.date = date


class Event:
  """
  A class representing an event with a name, date, and participant count.
  """
  def __init__(self, name, date):
    self.name = name
    self.date = date
    self.participant_count = 0  # Initialize participant count to 0

  def add_participant(self):
    """
    Increases the participant count by 1.
    """
    self.participant_count += 1

  def get_participant_count(self):
    """
    Returns the current number of participants.
    """
    return self.participant_count

# Create an event
event = Event("Coding Workshop", "2024-07-10")

# Add some participants
event.add_participant()
event.add_participant()
event.add_participant()

# Get the participant count
num_participants = event.get_participant_count()

print(f"Event: {event.name}")
print(f"Date: {event.date}")
print(f"Number of Participants: {num_participants}")