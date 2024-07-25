# importing tkinter
from tkinter import *
# importing tkk
from tkinter import ttk

# creating instance of Tk class
main_window= Tk()
main_window.title("My Simple Calculator")

# adding four columns to main window
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)

text =StringVar()
# creating a text field using Entry class
text_field=ttk.Entry(main_window,textvariable= text, width=55)
# attaching label to first row and second column
text_field.grid(row=0, column=0,columnspan=4,padx=5,pady=5)

expression_string=""
def press_button(num):
    # access the global expression_string
    global expression_string
    # add new text to the existing expression_string
    expression_string=expression_string+str(num)
    # update the text field with expression_string
    text.set(expression_string)

def press_equal_button():
    try:
        # access the global expression_string
        global expression_string
        # evaluate the text in expression_string
        result =str(eval(expression_string))
        # display the result in the text field
        text.set(result)
        # update expression_string to an empty string
        expression_string=""
    except:
        # show error in case of exception
        text.set(" error ")
        # update expression_string to an empty string
        expression_string=""

def clear():
    # update expression_string to an empty string
    expression_string=""
    # update text field to an empty string
    text.set("")

# creating a themed button for digit 1 and attaching it to the main window
my_button1 =ttk.Button(main_window, text ="1", command
=lambda:press_button(1))
my_button1.grid(row=1, column=0,padx=5,pady=5)
# creating a themed button for digit 2 and attaching it to the main window
my_button2 =ttk.Button(main_window, text ="2", command
=lambda:press_button(2))
my_button2.grid(row=1, column=1,padx=5,pady=5)
# creating a themed button for digit 3 and attaching it to the main window
my_button3 =ttk.Button(main_window, text ="3", command
=lambda:press_button(3))
my_button3.grid(row=1, column=2,padx=5,pady=5)
# creating a themed button for sign + and attaching it to the main window
my_button_plus=ttk.Button(main_window, text ="+", command
=lambda:press_button("+"))
my_button_plus.grid(row=1, column=3,padx=5,pady=5)

# creating a themed button for digit 4 and attaching it to the main window
my_button4 =ttk.Button(main_window, text ="4", command
=lambda:press_button(4))
my_button4.grid(row=2, column=0,padx=5,pady=5)# creating a themed button for digit 5 and attaching it to the main window
my_button5 =ttk.Button(main_window, text ="5", command
=lambda:press_button(5))
my_button5.grid(row=2, column=1,padx=5,pady=5)
# creating a themed button for digit 6 and attaching it to the main window
my_button6 =ttk.Button(main_window, text ="6", command
=lambda:press_button(6))
my_button6.grid(row=2, column=2,padx=5,pady=5)
# creating a themed button for sign - and attaching it to the main window
my_button_minus=ttk.Button(main_window, text ="-",
command=lambda:press_button("-"))
my_button_minus.grid(row=2, column=3,padx=5,pady=5)

# creating a themed button for digit 7 and attaching it to the main window
my_button7 =ttk.Button(main_window, text ="7", command
=lambda:press_button(7))
my_button7.grid(row=3, column=0,padx=5,pady=5)
# creating a themed button for digit 8 and attaching it to the main window
my_button8 =ttk.Button(main_window, text ="8", command
=lambda:press_button(8))
my_button8.grid(row=3, column=1,padx=5,pady=5)
# creating a themed button for digit 9 and attaching it to the main window
my_button9 =ttk.Button(main_window, text ="9", command
=lambda:press_button(9))
my_button9.grid(row=3, column=2,padx=5,pady=5)# creating a themed button for sign x and attaching it to the main window
my_button_mul=ttk.Button(main_window, text ="x", command
=lambda:press_button("*"))
my_button_mul.grid(row=3, column=3,padx=5,pady=5)

# creating a themed button for digit 0 and attaching it to the main window
my_button0 =ttk.Button(main_window, text ="0", command
=lambda:press_button(0))
my_button0.grid(row=4, column=0,padx=5,pady=5)
# creating a themed button for a dot and attaching it to the main window
my_button_dot=ttk.Button(main_window, text =".", command
=lambda:press_button("."))
my_button_dot.grid(row=4, column=1,padx=5,pady=5)
# creating a themed button for clear and attaching it to the main window
my_button_clr=ttk.Button(main_window, text ="clear", command = clear)
my_button_clr.grid(row=4, column=2,padx=5,pady=5)
# creating a themed button for sign / and attaching it to the main window
my_button_div=ttk.Button(main_window, text ="/", command
=lambda:press_button("/"))
my_button_div.grid(row=4, column=3,padx=5,pady=5)

# creating a themed button for sign = and attaching it to the main window
my_button_eqls=ttk.Button(main_window, text ="=", width=55, command
=press_equal_button)
my_button_eqls.grid(row=5, column=0,columnspan=4,padx=5,pady=5)

# displaying the main window
main_window.mainloop()