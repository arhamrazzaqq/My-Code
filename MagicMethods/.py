class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa > other.gpa
    
    def __it__(self, other):
        return self.gpa < other.gpa
    
    def __add__(self, other):
        return self.gpa + other.gpa
    
    def __contains__(self, keyword):
        return keyword in self.name
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key =="gpa":
            return self.gpa
        else:
            return f"key '{key}' was not found"
