import tkinter as tk

# making window and editing it a bit
window = tk.Tk()
window.title("Calculator")
window.geometry("300x350")

# displaying result of operation as well as number user clicks
result = tk.Label(window, text = "0",font=("Arial", 40) ,width = 14)
result.pack() # aligns result label propperly with other elements
# variables needed for calculating
first_number = 0 # first number user clicked
second_number = 0 # second number user clicked
is_plus = 0 # will be true if user clicks plus and false if user clicks minus

# functions
def error():
    if len(str(first_number)) >= 5 or len(str(second_number)) >= 5:
        window.destroy()
        print("Number can't be greater than 9999.")
        print("Press enter to stop the program.")
    else:
        return
            

def one():
    result.config(text = "1") # changes result label text to "1"
    # telling function that we want it to use global variables
    global first_number
    global second_number
    # if first number already changed we will change second number else
    # we will change first number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "1")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "1")
            result.config(text = str(second_number))
        else:
            second_number = 1
    else:
        first_number = 1
    error()
# we repeat same proccess for every number
def two():
    result.config(text = "2")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "2")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "2")
            result.config(text = str(second_number))
        else:
            second_number = 2
    else:
        first_number = 2
    error()
def three():
    result.config(text = "3")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "3")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "3")
            result.config(text = str(second_number))
        else:
            second_number = 3
    else:
        first_number = 3
    error()
def four():
    result.config(text = "4")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "4")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "4")
            result.config(text = str(second_number))
        else:
            second_number = 4
    else:
        first_number = 4
    error()
def five():
    result.config(text = "5")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "5")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "5")
            result.config(text = str(second_number))
        else:
            second_number = 5
    else:
        first_number = 5
    error()
def six():
    result.config(text = "6")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "6")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "6")
            result.config(text = str(second_number))
        else:
            second_number = 6
    else:
        first_number = 6
    error()
def seven():
    result.config(text = "7")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "7")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "7")
            result.config(text = str(second_number))
        else:
            second_number = 7
    else:
        first_number = 7
    error()
def eight():
    result.config(text = "8")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "8")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "8")
            result.config(text = str(second_number))
        else:
            second_number = 8
    else:
        first_number = 8
    error()
def nine():
    result.config(text = "9")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "9")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "9")
            result.config(text = str(second_number))
        else:
            second_number = 9
    else:
        first_number = 9
    error()
def zero():
    result.config(text = "0")
    global first_number
    global second_number
    if first_number != 0:
        if is_plus == 0:
            first_number = int(str(first_number) + "0")
            result.config(text = str(first_number))
        elif is_plus != 0:
            second_number = int(str(second_number) + "0")
            result.config(text = str(second_number))
        else:
            second_number = 0
    else:
        first_number = 0
    error()
def plus():
    result.config(text = "+")
    global is_plus
    is_plus = True # changing is_plus to true so that function enter() knows that we wanna add numbers and not substract them
def minus():
    result.config(text = "-")
    global is_plus
    is_plus = False # opposite of 4 lines before
def enter():
    global first_number
    res1 = first_number + second_number
    res2 = first_number - second_number
    global is_plus
    if is_plus == True:
        result.config(text = str(res1))
    elif is_plus == False:
        result.config(text = str(res2))
    first_number = int(result.cget("text"))
# reseting everything as it started
def reset():
    global enter_clicked
    global first_number
    global second_number
    global is_plus
    first_number = 0
    second_number = 0
    is_plus = 0
    result.config(text = "0")
    

# buttons that call functions
b1 = tk.Button(window, text = "1", font=("Arial", 20), command = one)
b1.place(x = 30, y = 80)
b2 = tk.Button(window, text = "2", font=("Arial", 20), command = two)
b2.place(x = 95, y = 80)
b3 = tk.Button(window, text = "3", font=("Arial", 20), command = three)
b3.place(x = 160, y = 80)

b4 = tk.Button(window, text = "4", font=("Arial", 20), command = four)
b4.place(x = 30, y = 145)
b5 = tk.Button(window, text = "5", font=("Arial", 20), command = five)
b5.place(x = 95, y = 145)
b6 = tk.Button(window, text = "6", font=("Arial", 20), command = six)
b6.place(x = 160, y = 145)

b7 = tk.Button(window, text = "7", font=("Arial", 20), command = seven)
b7.place(x = 30, y = 210)
b8 = tk.Button(window, text = "8", font=("Arial", 20), command = eight)
b8.place(x = 95, y = 210)
b9 = tk.Button(window, text = "9", font=("Arial", 20), command = nine)
b9.place(x = 160, y = 210)

b0 = tk.Button(window, text = "0", font=("Arial", 20), width = 10, command = zero)
b0.place(x = 30, y = 275)

enter = tk.Button(window, text = "Enter", font=("Arial", 10), height = 6, command = enter)
enter.place(x = 225, y = 210)

plus = tk.Button(window, text = "+", font=("Arial", 20), width = 2, command = plus)
plus.place(x = 225, y = 145)

minus = tk.Button(window, text = "-", font=("Arial", 20), width = 2, command = minus)
minus.place(x = 225, y = 80)

reset = tk.Button(window, text = "C", font=("Arial", 20), width = 2, command = reset)
reset.place(x = 225, y = 15)
