from arithmetic import Calculator


# Greeting message for user, displays menu options
def greeting():
    print("Welcom to Eric's Calcualtor App\n", "-"*30)
    print("Here are the menu options: \n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")

# Takes in the user's selection
def user_input():
    selection = input("Enter the number of the operation you would like to perform: ")
    NUM_MENU_OPTIONS = 4

    # Checks for valid user selection
    if int(selection) not in range(NUM_MENU_OPTIONS + 1):
        print("Please choose a valid selection\n")
        user_input()
    else:
        print("Excellent Choice")
    
    return selection


def operation_selection(user_input):
    calculator = Calculator()

    if user_input == "1":
        solution = calculator.Addition()
    elif user_input == "2":
        solution = calculator.Subtraction()
    elif user_input == "3":
        solution = calculator.Multiplication()
    elif user_input == "4":
        solution = calculator.Division()

    return solution

def main():

    calc = Calculator()
    greeting()
    solution = operation_selection(user_input=user_input())
    print(solution)



main()


