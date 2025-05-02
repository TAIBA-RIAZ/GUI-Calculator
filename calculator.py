from tkinter import * 

# fOUR FUNCTIONALITY, ADDITION, SUBTRACTION, MULTIPLICATION AND DIVISION, CLEARING THE SCREEN, AND EQUALS FUNCTIONALITY, DIGITS ITSELF

# Operators code: +, -, *, /
first_number=second_number=operator=None
# Digit code: 0-9
# For digit buttons, we will use lambda function to pass the digit to the function get_digit
def get_digit(digit): # function to get digit
    current = result_label['text'] # get current value of label
    new = current +str(digit) # add digit to current value
    result_label['text'] = new # set new value to label

# Clear code: C
def clear(): # function to clear label
    result_label.config(text = '' ) # set label to empty string

def get_operator(op): # function to get operator
    global first_number, operator # declare global variables
    first_number = int(result_label['text']) # set first number to current value of label
    operator = op # set operator to passed operator, stored in variable operator
    result_label.config(text = '') # set label to empty string

# Equals code: =
def get_result(): # function to get result
    global first_number, second_number, operator # declare global variables
    second_number = int(result_label['text']) # set second number to current value of label
    if operator == '+': # if operator is +, add first and second number
        result = first_number + second_number 
    elif operator == '-': # if operator is -, subtract first and second number
        result = first_number - second_number 
    elif operator == '*': # if operator is *, multiply first and second number
        result = first_number * second_number 
    elif operator == '/': # if operator is /, divide first and second number
        result = first_number / second_number 
    result_label.config(text = str(round(result))) # set label to result


# CALCULATOR USING PYTHON GUI TKINTER
root = Tk()
root.title('Calaculator') # name
root.geometry('280x380') # size of window 
root.resizable(0,0) # fix size
root.config(bg='Grey') # background color 

result_label = Label(root, text='', bg='Grey', fg='white') # label to show result
result_label.grid(row=0, column=0, columnspan=5, pady=(50,25), sticky='w') # grid manager responsible to place items on window
result_label.config(font=('Arial', 20, 'bold')) # font of label

btn7 = Button(root, text='7', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(7)) # button 7
btn7.grid(row=1, column=0, padx=4, pady=4) # grid manager responsible to place items on window
btn7.config(font=('Arial', 20, 'bold')) # font of button 7

btn8 = Button(root, text='8', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(8)) # button 8
btn8.grid(row=1, column=1, padx=4, pady=4) # grid manager responsible to place items on window
btn8.config(font=('Arial', 20, 'bold')) # font of button 8

btn9 = Button(root, text='9', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(9)) # button 9
btn9.grid(row=1, column=2, padx=4, pady=4) # grid manager responsible to place items on window  
btn9.config(font=('Arial', 20, 'bold')) # font of button 9

btn_add = Button(root, text='+', width=3, height=1, bg='#f54281', fg='white', command= lambda :get_operator('+')) # button add
btn_add.grid(row=1, column=3, padx=4, pady=4) # grid manager responsible to place items on window  
btn_add.config(font=('Arial', 20, 'bold')) # font of button add

btn4 = Button(root, text='4', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(4)) # button 4
btn4.grid(row=2, column=0, padx=4, pady=4) # grid manager responsible to place items on window  
btn4.config(font=('Arial', 20, 'bold')) # font of button 4

btn5 = Button(root, text='5', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(5)) # button 5   
btn5.grid(row=2, column=1, padx=4, pady=4) # grid manager responsible to place items on window
btn5.config(font=('Arial', 20, 'bold')) # font of button 5

btn6 = Button(root, text='6', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(6)) # button 6
btn6.grid(row=2, column=2, padx=4, pady=4) # grid manager responsible to place items on window  
btn6.config(font=('Arial', 20, 'bold')) # font of button 6

btn_sub = Button(root, text='-', width=3, height=1, bg='#f54281', fg='white', command= lambda :get_operator('-')) # button sub
btn_sub.grid(row=2, column=3, padx=4, pady=4) # grid manager responsible to place items on window
btn_sub.config(font=('Arial', 20, 'bold')) # font of button sub

btn1 = Button(root, text='1', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(1)) # button 1   
btn1.grid(row=3, column=0, padx=4, pady=4) # grid manager responsible to place items on window
btn1.config(font=('Arial', 20, 'bold')) # font of button 1

btn2 = Button(root, text='2', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(2)) # button 2
btn2.grid(row=3, column=1, padx=4, pady=4) # grid manager responsible to place items on window
btn2.config(font=('Arial', 20, 'bold')) # font of button 2

btn3 = Button(root, text='3', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(3)) # button 3
btn3.grid(row=3, column=2, padx=4, pady=4) # grid manager responsible to place items on window
btn3.config(font=('Arial', 20, 'bold')) # font of button 3

btn_mul = Button(root, text='*', width=3, height=1, bg='#f54281', fg='white', command= lambda :get_operator('*')) # button mul
btn_mul.grid(row=3, column=3, padx=4, pady=4) # grid manager responsible to place items on window   
btn_mul.config(font=('Arial', 20, 'bold')) # font of button mul

btn_clr = Button(root, text='C', width=3, height=1, bg='#f54281', fg='white', command = lambda :clear()) # button clear
btn_clr.grid(row=4, column=0, padx=4, pady=4) # grid manager responsible to place items on window
btn_clr.config(font=('Arial', 20, 'bold')) # font of button clear

btn0 = Button(root, text='0', width=3, height=1, bg='#f54281', fg='white', command = lambda :get_digit(0)) # button 0
btn0.grid(row=4, column=1, padx=4, pady=4) # grid manager responsible to place items on window
btn0.config(font=('Arial', 20, 'bold')) # font of button 0

btn_equals = Button(root, text='=', width=3, height=1, bg='#f54281', fg='white', command= get_result) # button equal
btn_equals.grid(row=4, column=2, padx=4, pady=4) # grid manager responsible to place items on window
btn_equals.config(font=('Arial', 20, 'bold')) # font of button equal

btn_div = Button(root, text='/', width=3, height=1, bg='#f54281', fg='white', command= lambda :get_operator('/')) # button div
btn_div.grid(row=4, column=3, padx=4, pady=4) # grid manager responsible to place items on window
btn_div.config(font=('Arial', 20, 'bold')) # font of button div

root.mainloop()