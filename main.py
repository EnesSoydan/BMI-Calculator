import tkinter

window=tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=20,pady=20)

weight_label=tkinter.Label(text="Enter your weight (kg) ")
weight_label.pack()

weight_entry=tkinter.Entry()
weight_entry.pack()

height_label=tkinter.Label(text="Enter your height (cm) ")
height_label.pack()

height_entry=tkinter.Entry()
height_entry.pack()

def calculator():
    height_value=height_entry.get()
    weight_value=weight_entry.get()
    if height_value=="" or weight_value=="":
        result.config(text="Enter both weight and height")
    else:
        try:
            weight=float(weight_value)
            height=float(height_value)/100
            bmi=weight/(height**2)
            if bmi<18.5:
                result.config(text=f"Your BMI is {bmi}.You are underweight")
            elif bmi>=18.5 and bmi<25.0:
                result.config(text=f"Your BMI is {bmi}.You are normal")
            elif bmi>=25.0 and bmi<30.0:
                result.config(text=f"Your BMI is {bmi}.You are overweight")
            elif bmi>=30:
                result.config(text=f"Your BMI is {bmi}.You are very overweight")

        except ValueError:
            result.config(text="Enter a valid number")

calculator_button=tkinter.Button(text="Calculate",command=calculator)
calculator_button.pack()

result=tkinter.Label()
result.pack()

window.mainloop()
