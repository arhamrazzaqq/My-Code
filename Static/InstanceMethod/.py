#STATIC METHOD

class Employee:

    def __init__(self, name, position):
     self.name = name
     self.posotion = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    staticmethod
    def is_valid_position(position):
       valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
       return position in valid_positions
    
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("SquadWard", "Cashier")
employee3 = Employee("SpongeBob", "Janitor")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())