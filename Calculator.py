from tkinter import *
#Refik
def button_click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))

def clear_entry():
    entry.delete(0, END)

def perform_operation(operator):
    global first_num
    global current_operation
    current_operation = operator
    first_num = float(entry.get())
    entry.delete(0, END)

def calculate_result():
    second_num = float(entry.get())
    entry.delete(0, END)

    if current_operation == "addition":
        result = first_num + second_num
    elif current_operation == "subtract":
        result = first_num - second_num
    elif current_operation == "product":
        result = first_num * second_num
    elif current_operation == "divide":
        result = first_num / second_num
    else:
        result = 0

    entry.insert(0, result)

# Create the main window
root = Tk()
root.title("Calculator")

# Create the entry widget
entry = Entry(root, width=35, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create number buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"]
]

i = 0
while i < len(buttons):
    j = 0
    while j < len(buttons[i]):
        button = Button(root, text=buttons[i][j], padx=35, pady=20, command=lambda num=buttons[i][j]: button_click(num))
        button.grid(row=i+1, column=j)
        j += 1
    i += 1

# Create operation buttons
operation_buttons = ["+", "-", "*", "/"]

for i in range(len(operation_buttons)):
    button = Button(root, text=operation_buttons[i], padx=35, pady=20, command=lambda op=operation_buttons[i]: perform_operation(op))
    button.grid(row=i+1, column=3)

# Create equal button
equal_button = Button(root, text="=", padx=35, pady=20, command=calculate_result)
equal_button.grid(row=len(operation_buttons)+1, column=3)

# Create clear button
clear_button = Button(root, text="C", padx=35, pady=20, command=clear_entry)
clear_button.grid(row=len(operation_buttons)+1, column=0)

# Start the main event loop
root.mainloop()
