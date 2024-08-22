import tkinter
from logging import lastResort

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.config(padx=30,pady=30)

def calculator():
    x = kilo_input.get()
    y = boy_input.get()
    if x=="" or y == "":
        result_label.configure(text="Enter both weight and height!")
    else:
        try:
            result = float(x) / (float(y) / 100)**2
            last_result = display_text(result)
            result_label.configure(text=last_result)
        except:
            result_label.configure(text="Enter a valid number!")

#ui
kilo_label = tkinter.Label(text="Enter Your Weight (kg)")
kilo_label.pack()
kilo_input = tkinter.Entry(width=16)
kilo_input.pack()
kilo_label = tkinter.Label(text="Enter Your Height (cm)")
kilo_label.pack()
boy_input = tkinter.Entry(width=16,)
boy_input.pack()
calculate_button = tkinter.Button(text="Calculate", command= calculator)
calculate_button.pack()
result_label = tkinter.Label(text="",font=("Arial", 9, "normal"))
result_label.pack()

def display_text(result):
    last_result=f"Your BMI is {round(result,2)}. You are "
    if result<=16:
        last_result += "severely thin!"
    elif 16<result <= 17:
        last_result += "moderately thin!"
    elif 17 < result <= 18.5:
        last_result += "mild thin!"
    elif 18.5 < result <= 25:
        last_result += "normal weight"
    elif 25 < result <= 30:
        last_result += "overweight"
    elif 30 < result <= 35:
        last_result += "obese class 1"
    elif 35 < result <= 40:
        last_result += "obese class 2"
    elif 40 < result:
        last_result += "obese class 3"
    return last_result

screen.mainloop()