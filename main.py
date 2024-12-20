import tkinter

window=tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=20,pady=20)

def calculator():
    weight=weight_entry.get()
    height=height_entry.get()
    if height=="" or weight=="":
        result_label.config(text="Enter both weight and height")
    else:
        try:
            result_value=float(weight)/((float(height)/100)**2)
            output_text(result_value)
        except ValueError:
            result_label.config(text="Enter a valid number")

def output_text(result_value):
    main_output=f"Your BMI is {result_value}.You are "
    if result_value<18.5:
        result_label.config(text=main_output+"underweight")
    elif result_value>=18.5 and result_value<25.0:
        result_label.config(text=main_output+ "normal")
    elif result_value >= 25.0 and result_value < 30.0:
        result_label.config(text=main_output+ "overweight")
    elif result_value >= 30:
        result_label.config(text=main_output+"overweight")
    return result_label.config()

FONT=('Arial',10,'italic')

weight_label=tkinter.Label(text="Enter your weight (kg) ",font=FONT)
weight_label.pack()

weight_entry=tkinter.Entry()
weight_entry.pack()

height_label=tkinter.Label(text="Enter your height (cm) ",font=FONT)
height_label.pack()

height_entry=tkinter.Entry()
height_entry.pack()

calculator_button=tkinter.Button(text="Calculate",command=calculator,font=FONT)
calculator_button.pack()

result_label=tkinter.Label(text="")
result_label.pack()

window.mainloop()
