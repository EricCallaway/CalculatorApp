from arithmetic import Calculator
from tkinter import Tk, Label, Button, Frame, StringVar, font
from tkinter import ttk



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

    root = Tk()
    root.title("Basic Calculator")
    root.geometry("400x600")
    root.maxsize(400, 600)
    root.minsize(400, 600)

    # Defining the column architecture of the grid
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    
    # Defining the row architecture of the grid
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)



    

    WIDTH = 10

    myFont = font.Font(size=30)

    equation_label = StringVar()

    display = Label(root, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2).grid(row=0, column=0, columnspan=4, sticky='nswe')

    zero = Button(root, width=WIDTH*2, text="0", font=myFont).grid(row=6, column=0, columnspan=2, sticky='nswe')
    one = Button(root, width=WIDTH, text="1", font=myFont).grid(row=5, column=0, sticky='nswe')
    two = Button(root, width=WIDTH, text="2" , font=myFont).grid(row=5, column=1, sticky='nswe')
    three = Button(root, width=WIDTH, text="3", font=myFont).grid(row=5, column=2, sticky='nswe')
    four = Button(root, width=WIDTH,text="4", font=myFont).grid(row=4, column=0, sticky='nswe')
    five = Button(root, width=WIDTH, text="5", font=myFont).grid(row=4, column=1, sticky='nswe')
    six = Button(root, width=WIDTH, text="6", font=myFont).grid(row=4, column=2, sticky='nswe')
    seven = Button(root, width=WIDTH, text="7", font=myFont).grid(row=3, column=0, sticky='nswe')
    eight = Button(root, width=WIDTH, text="8", font=myFont).grid(row=3, column=1, sticky='nswe')
    nine = Button(root, width=WIDTH, text="9", font=myFont).grid(row=3, column=2, sticky='nswe')
    decimal = Button(root, width=WIDTH, text=".", font=myFont).grid(row=6, column=2, sticky='nswe')

    divide = Button(root, width=WIDTH, text="/", font=myFont).grid(row=2, column=3, sticky='nswe')
    multiply = Button(root, width=WIDTH, text="X", font=myFont).grid(row=3, column=3, sticky='nswe')
    subtract = Button(root, width=WIDTH, text="-", font=myFont).grid(row=4, column=3, sticky='nswe')
    add = Button(root, width=WIDTH, text="+", font=myFont).grid(row=5, column=3, sticky='nswe')
    equal = Button(root, width=WIDTH, text="=", font=myFont).grid(row=6, column=3, sticky='nswe')

    clear = Button(root, width=WIDTH, text="C" , font=myFont).grid(row=2, column=0, sticky='nswe')
    pos_neg = Button(root, width=WIDTH, text="+/-", font=myFont).grid(row=2, column=1, sticky='nswe')
    percentage = Button(root, width=WIDTH, text="%", font=myFont).grid(row=2, column=2, sticky='nswe')

  
    
    
    root.mainloop()

    

    # calc = Calculator()
    # greeting()
    # solution = operation_selection(user_input=user_input())
    # print(solution)



main()


