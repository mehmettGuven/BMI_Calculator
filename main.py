import tkinter
from unittest import removeResult

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.minsize(300,200)

last_result=""
result=""
decimal = float()


kilo_label = tkinter.Label(text="Enter Your Weight (kg)")
kilo_label.place(x=95,y=30)

kilo_input = tkinter.Entry(width=16)
kilo_input.place(x=100,y=52)

kilo_label = tkinter.Label(text="Enter Your Height (cm)")
kilo_label.place(x=95,y=74)

boy_input = tkinter.Entry(width=16,)
boy_input.place(x=100,y=96)


def calculator():
    global last_result, result,decimal
    x = float(kilo_input.get())
    y = float(boy_input.get()) / 100
    result = x / (y * y)
    decimal= "%.2f" % result
    if result <= 18.5:
        last_result = "Underweight"
    elif result <= 25:
        last_result = "Normal Weight"
    elif result <= 30:
        last_result = "Overweight"
    elif result > 30:
        last_result = "Obese Weight"

def display_text():
    calculator()
    global result_label, last_result, result, decimal
    result_label.configure(text=f"Your BMI is {decimal}. You are {last_result}. ")

calculate_button = tkinter.Button(text="Calculate", command= display_text)
calculate_button.place(x=120,y=118)

result_label = tkinter.Label(text="",font=("Arial", 9, "normal"))
result_label.place(x=40,y=160)


screen.mainloop()