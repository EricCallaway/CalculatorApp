class Calculator:
    def __init__(self):
        pass
        

    def Addition(self):
        first_operand = input("First number: ")
        try:
            float(first_operand)
        except ValueError:
            print("Enter a valid number")
            self.Addition()

        
        second_operand = input("Second number: ")
        try:
            float(second_operand)
        except ValueError:
            print("Enter a valid number")
            self.Addition()
        
        add_solution = float(first_operand) + float(second_operand)
        return add_solution

    def Subtraction(self):
        first_operand = input("First number: ")
        try:
            float(first_operand)
        except ValueError:
            print("Enter a valid number")
            self.Subtraction()

        
        second_operand = input("Second number: ")
        try:
            float(second_operand)
        except ValueError:
            print("Enter a valid number")
            self.Subtraction()
        
        sub_solution = float(first_operand) - float(second_operand)
        return sub_solution

    def Multiplication(self):
        first_operand = input("First number: ")
        try:
            float(first_operand)
        except ValueError:
            print("Enter a valid number")
            self.Division()

        
        second_operand = input("Second number: ")
        try:
            float(second_operand)
        except ValueError:
            print("Enter a valid number")
            self.Multiplication()

        self.solution = float(first_operand) * float(second_operand)
        return self.solution

    def Division(self):
        first_operand = input("First number: ")
        try:
            float(first_operand)
        except ValueError:
            print("Enter a valid number")
            self.Division()

        
        second_operand = input("Second number: ")
        try:
            float(second_operand)
        except ValueError:
            print("Enter a valid number")
            self.Division()

        self.solution = float(first_operand) / float(second_operand)
        return self.solution
