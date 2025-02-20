import tkinter as tk
from tkinter import font

#step 1 : create the main window

root = tk.Tk()
root.title("Built By Safdar")
root.geometry("300x450")
root .configure(bg="black")
# custom font for buttons and display
button_font = font.Font(family ="Arial", size =20)
display_font =font.Font(family = "Arial", size=24)

# Step 2: ceate the display
display= tk.Entry(root, font=display_font, justify = "right", bd=10, relief="ridge", bg="white", fg= "black")
display.grid(row =0, column=0,columnspan=4, padx =10, pady=10)

# step 3: Define button click function
def append_to_display(symbol):
    current= display.get()
    display.delete(0, tk.END)
    display.insert(0, current+symbol)

# step 4: Define clear function
def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()  # Get the current text from the display
    display.delete(0, tk.END)  # Clear the display
    display.insert(0, current[:-1])

def on():
    display.config(state="normal")  # Enable the display
    display.delete(0, tk.END) 

def off():
    display.config(state="disabled")
    for button in buttons :
        button.configue(state= "disabled")


# step 5: Define calculate function

def calculate():
    try:
        expression = display.get()
        result = eval(expression)  # Safe evaluation of expressions
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# step 6: create buttons
buttons =[
    ('C', 1, 0), ('←', 1,1 ), ('=', 1, 2), ("ON",1,3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('OFF',5,3)
]

# Add buttons to the window
for (text, row, col) in buttons:    
    if text == "=":
        btn = tk.Button (root, text=text, font=button_font, bg ="#f44336", fg="#ffffff", command= calculate)
    elif text =="C":
            btn = tk.Button(root, text =text, font=button_font, bg="#f44336", fg= "#ffffff", command= clear)
    elif text =='←':
        btn = tk.Button(root, text=text, font=button_font, bg="#f44336", fg="#ffffff", command=backspace)
    elif text == "ON":
        btn = tk.Button (root, text =text, font=button_font , bg="green", fg ="white", command =on)
    elif text == "OFF":
        btn= tk.Button(root, text=text, font =button_font,bg ="dark red", fg="white", command= off)
   
    else:
         btn = tk.Button(root, text=text, font=button_font, bg="#e0e0e0", fg="#000000", command=lambda value=text: append_to_display(value))
   
    btn.grid(row=row, column= col, padx=5, pady=5, sticky ="nsew")

# step 7: configrure grid layoput for responsiveness
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight =1)

#step 8: Run the application
root.mainloop()